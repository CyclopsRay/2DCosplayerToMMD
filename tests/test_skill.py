"""Packaging checks: metadata must load and local reference links must resolve."""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class SkillPackageTests(unittest.TestCase):
    def test_frontmatter_and_interface(self):
        text = (ROOT/'SKILL.md').read_text()
        metadata = yaml.safe_load(text.split('---', 2)[1])
        self.assertRegex(metadata['name'], r'^[a-z0-9-]+$')
        self.assertLess(len(metadata['name']), 64)
        self.assertIsInstance(metadata['description'], str)
        interface = yaml.safe_load((ROOT/'agents/openai.yaml').read_text())['interface']
        self.assertIn('$' + metadata['name'], interface['default_prompt'])

    def test_local_references_exist(self):
        for path in ROOT.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((path.parent/target.split('#')[0]).is_file(), (path, target))

    def test_no_asset_formats_are_in_skill(self):
        forbidden = {'.vmd','.vpd','.pmx','.pmd','.blend','.glb','.fbx','.zip','.mp3','.mp4'}
        self.assertFalse([p.name for p in ROOT.rglob('*') if p.is_file() and p.suffix in forbidden])


if __name__ == '__main__':
    unittest.main()
