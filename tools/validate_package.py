#!/usr/bin/env python3
"""Validate skill format, discovery metadata, resource links and source provenance."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml


def validate(root, validator):
    root = Path(root).resolve()
    catalog = json.loads((root / 'skill-catalog.json').read_text())
    names = [entry['name'] for entry in catalog]
    if len(names) != 15 or len(set(names)) != 15:
        raise ValueError('Expected 15 unique skills')
    if sorted(p.name for p in (root / 'skills').iterdir()) != sorted(names):
        raise ValueError('Catalog and skill directories differ')
    if not validator.is_file():
        raise ValueError('Official validator is unavailable: ' + str(validator))
    results = []
    internal_links = 0
    for name in names:
        folder = root / 'skills' / name
        skill = folder / 'SKILL.md'
        text = skill.read_text()
        data = yaml.safe_load(text.split('---', 2)[1])
        if data['name'] != name:
            raise ValueError('Frontmatter name differs: ' + name)
        interface = yaml.safe_load((folder / 'agents/openai.yaml').read_text())['interface']
        if not 25 <= len(interface['short_description']) <= 64:
            raise ValueError('UI description length is invalid: ' + name)
        if '$' + name not in interface['default_prompt']:
            raise ValueError('UI prompt does not identify skill: ' + name)
        official = subprocess.run([sys.executable, str(validator), str(folder)],
                                  capture_output=True, text=True)
        if official.returncode:
            raise ValueError(name + ': ' + official.stdout + official.stderr)
        checked = 0
        for doc in folder.rglob('*.md'):
            content = doc.read_text()
            if re.search(r'\bTODO\b|\[INSERT|\[PLACEHOLDER', content, re.I):
                raise ValueError('Unfinished scaffold: ' + str(doc))
            for href in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', content):
                if '://' in href or href.startswith('#'):
                    continue
                dest = (doc.parent / href.split('#')[0]).resolve()
                if not dest.exists() or root / 'skills' not in dest.parents:
                    raise ValueError('Missing or outside-suite reference: ' + str(doc) + ' -> ' + href)
                checked += 1
        internal_links += checked
        results.append({'name': name, 'official_format': 'passed', 'discovery_metadata': 'passed',
                        'internal_links_checked': checked})
    sources = json.loads((root / 'source-register.json').read_text())
    if len(sources) != 5:
        raise ValueError('Expected five source repositories')
    upstream = (root / 'skills/homestay-arch-orchestrator/references/upstream-methods.md').read_text()
    for source in sources:
        if not re.fullmatch(r'[0-9a-f]{40}', source['commit']):
            raise ValueError('Source commit is not fixed')
        license_path = root / 'skills/homestay-arch-orchestrator/references/licenses' / (source['id'] + '.txt')
        if hashlib.sha256(license_path.read_bytes()).hexdigest() != source['license_sha256']:
            raise ValueError('License copy differs: ' + source['id'])
        if source['commit'][:12] not in upstream or source['id'] not in upstream:
            raise ValueError('Source attribution is missing')
        for source_file in source['files']:
            if not re.fullmatch(r'[0-9a-f]{64}', source_file['sha256']) or not source_file['adopted_at']:
                raise ValueError('Source file has incomplete provenance')
            if source['commit'] not in source_file['source_url']:
                raise ValueError('Source file URL is not pinned')
    return {'date': '2026-10-28', 'status': 'passed', 'skills': results,
            'official_formats_passed': len(results), 'internal_links_checked': internal_links,
            'repositories': len(sources), 'reviewed_source_skill_files': sum(len(x['files']) for x in sources),
            'license_copies_verified': len(sources),
            'scope': 'Package structure, official format, metadata, local references and saved provenance; not design behavior.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--official-validator', type=Path,
                        default=Path.home() / '.codex/skills/.system/skill-creator/scripts/quick_validate.py')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    result = validate(Path(__file__).resolve().parents[1], args.official_validator)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'skills'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
