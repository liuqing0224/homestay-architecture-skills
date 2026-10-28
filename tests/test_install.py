import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('homestay_installer', ROOT / 'install.py')
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.target = self.base / 'installed'

    def tearDown(self):
        self.temp.cleanup()

    def test_dry_run_leaves_target_absent(self):
        result = installer.install(ROOT, self.target, dry_run=True)
        self.assertEqual(result['skills'], 15)
        self.assertFalse(self.target.exists())

    def test_complete_install_and_check(self):
        result = installer.install(ROOT, self.target)
        self.assertEqual(result['status'], 'installed-and-verified')
        self.assertEqual(len(list(self.target.iterdir())), 15)
        self.assertEqual(installer.install(ROOT, self.target, check=True)['status'], 'verified')

    def test_conflict_prevents_partial_install(self):
        name = 'homestay-arch-site'
        folder = self.target / name
        folder.mkdir(parents=True)
        (folder / 'local.txt').write_text('keep')
        with self.assertRaises(ValueError):
            installer.install(ROOT, self.target)
        self.assertEqual(sorted(p.name for p in self.target.iterdir()), [name])
        self.assertEqual((folder / 'local.txt').read_text(), 'keep')

    def test_modified_install_is_detected(self):
        installer.install(ROOT, self.target)
        (self.target / 'homestay-arch-site/SKILL.md').write_text('edited')
        with self.assertRaises(ValueError):
            installer.install(ROOT, self.target, check=True)

    def test_extra_install_file_is_detected(self):
        installer.install(ROOT, self.target)
        (self.target / 'homestay-arch-site/unexpected.txt').write_text('extra')
        with self.assertRaises(ValueError):
            installer.install(ROOT, self.target, check=True)

    def test_source_symlink_is_rejected_before_writes(self):
        source = self.base / 'source'
        shutil.copytree(ROOT / 'skills', source / 'skills')
        shutil.copyfile(ROOT / 'skill-catalog.json', source / 'skill-catalog.json')
        (source / 'skills/homestay-arch-site/linked').symlink_to(ROOT / 'README.md')
        with self.assertRaises(ValueError):
            installer.install(source, self.target)
        self.assertFalse(self.target.exists())

    def test_target_symlink_is_rejected(self):
        actual = self.base / 'actual'
        actual.mkdir()
        self.target.symlink_to(actual, target_is_directory=True)
        with self.assertRaises(ValueError):
            installer.install(ROOT, self.target)
        self.assertEqual(list(actual.iterdir()), [])

    def test_copy_failure_removes_owned_partial_directories(self):
        real_copy = installer.shutil.copytree
        copied = {'count': 0}

        def fail_during_publish(source, destination, *args, **kwargs):
            dest = Path(destination)
            if dest.parent == self.target:
                copied['count'] += 1
                if copied['count'] == 2:
                    (dest / 'partial.txt').write_text('partial')
                    raise OSError('simulated copy failure')
            return real_copy(source, destination, *args, **kwargs)

        with patch.object(installer.shutil, 'copytree', side_effect=fail_during_publish):
            with self.assertRaises(OSError):
                installer.install(ROOT, self.target)
        self.assertFalse(self.target.exists())

    def test_unrelated_existing_skill_survives_rollback(self):
        self.target.mkdir()
        keep = self.target / 'other-skill'
        keep.mkdir()
        (keep / 'SKILL.md').write_text('keep')
        original_manifest = installer.manifest

        def bad_installed_manifest(folder):
            folder = Path(folder)
            if folder.parent == self.target:
                return {'wrong': 'hash'}
            return original_manifest(folder)

        with patch.object(installer, 'manifest', side_effect=bad_installed_manifest):
            with self.assertRaises(ValueError):
                installer.install(ROOT, self.target)
        self.assertEqual(sorted(p.name for p in self.target.iterdir()), ['other-skill'])
        self.assertEqual((keep / 'SKILL.md').read_text(), 'keep')

    def test_catalog_mismatch_stops_preflight(self):
        source = self.base / 'source'
        shutil.copytree(ROOT / 'skills', source / 'skills')
        catalog = json.loads((ROOT / 'skill-catalog.json').read_text())
        catalog.pop()
        (source / 'skill-catalog.json').write_text(json.dumps(catalog))
        with self.assertRaises(ValueError):
            installer.install(source, self.target)
        self.assertFalse(self.target.exists())


if __name__ == '__main__':
    unittest.main()
