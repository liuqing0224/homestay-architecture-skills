#!/usr/bin/env python3
"""Install the complete homestay architecture skill set without replacing existing skills."""
import argparse
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


def manifest(folder):
    folder = Path(folder)
    if folder.is_symlink():
        raise ValueError(f'Symbolic links are not accepted: {folder}')
    if not folder.is_dir():
        return None
    result = {}
    for path in sorted(folder.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symbolic links are not accepted: {path}')
        if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def source_set(root):
    root = Path(root).resolve()
    catalog = json.loads((root / 'skill-catalog.json').read_text())
    names = sorted(item['name'] for item in catalog)
    if len(names) != 15 or len(set(names)) != 15:
        raise ValueError('Expected 15 unique catalog entries')
    if any(not re.fullmatch(r'homestay-arch-[a-z]+(?:-[a-z]+)*', name) for name in names):
        raise ValueError('Invalid catalog name')
    directories = sorted(p.name for p in (root / 'skills').iterdir())
    if directories != names:
        raise ValueError('Skill directory set does not match the catalog')
    sources = {name: root / 'skills' / name for name in names}
    hashes = {}
    for name, folder in sources.items():
        hashes[name] = manifest(folder)
        if not hashes[name] or 'SKILL.md' not in hashes[name] or 'agents/openai.yaml' not in hashes[name]:
            raise ValueError(f'Incomplete skill: {name}')
    return sources, hashes


def install(root, target, *, check=False, dry_run=False):
    if check and dry_run:
        raise ValueError('Choose --check or --dry-run')
    root = Path(root).resolve()
    target = Path(target).expanduser()
    if target.is_symlink() or (target.exists() and not target.is_dir()):
        raise ValueError('Target must be a directory rather than a link or file')
    if target.resolve() == root or root in target.resolve().parents:
        raise ValueError('Installation target must be outside the source package')
    sources, hashes = source_set(root)
    if check:
        bad = [name for name in sources if manifest(target / name) != hashes[name]]
        if bad:
            raise ValueError('Installed content differs: ' + ', '.join(bad))
        return {'status': 'verified', 'skills': len(sources), 'target': str(target)}
    conflicts = [name for name in sources if (target / name).exists() or (target / name).is_symlink()]
    if conflicts:
        raise ValueError('No files written; existing skill names: ' + ', '.join(conflicts))
    if dry_run:
        return {'status': 'ready', 'skills': len(sources), 'target': str(target)}

    target.parent.mkdir(parents=True, exist_ok=True)
    owned = []
    created_target = False
    with tempfile.TemporaryDirectory(prefix='.homestay-arch-stage-', dir=target.parent) as temp:
        stage = Path(temp)
        for name, source in sources.items():
            shutil.copytree(source, stage / name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            if manifest(stage / name) != hashes[name]:
                raise ValueError(f'Source changed or staging failed: {name}')
        try:
            if not target.exists():
                target.mkdir()
                created_target = True
            for name in sources:
                dest = target / name
                dest.mkdir()  # Exclusive creation also detects a name appearing after preflight.
                owned.append(dest)
                shutil.copytree(stage / name, dest, dirs_exist_ok=True)
            if any(manifest(target / name) != hashes[name] for name in sources):
                raise ValueError('Installed byte verification failed')
        except Exception:
            for folder in reversed(owned):
                shutil.rmtree(folder)
            if created_target:
                try:
                    target.rmdir()
                except OSError:
                    pass
            raise
    return {'status': 'installed-and-verified', 'skills': len(sources), 'target': str(target)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, default=Path.home() / '.codex/skills')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    print(json.dumps(install(Path(__file__).resolve().parent, args.target,
                             check=args.check, dry_run=args.dry_run), ensure_ascii=False))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error))
