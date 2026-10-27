import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
SCRIPT = SKILL / 'scripts/init_latex.py'

class LatexStarterTests(unittest.TestCase):
    def run_init(self, dest, title='测试论文'):
        self.assertTrue(SCRIPT.is_file(), 'LaTeX project generator is missing')
        return subprocess.run([sys.executable, str(SCRIPT), str(dest), '--title', title], capture_output=True, text=True)

    def test_creates_self_contained_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'thesis'
            result=self.run_init(dest)
            self.assertEqual(result.returncode,0,result.stderr)
            for name in ['main.tex','usst-thesis.sty','fonts.tex','chapters/chapter01.tex','references.tex','README.md']:
                self.assertTrue((dest/name).is_file(),name)
            self.assertIn('测试论文',(dest/'main.tex').read_text())

    def test_title_is_escaped_as_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'thesis'
            result=self.run_init(dest,r'A&B_50% {test} \input{secret}')
            self.assertEqual(result.returncode,0,result.stderr)
            content=(dest/'main.tex').read_text()
            self.assertIn(r'A\&B\_50\% \{test\} \textbackslash{}input\{secret\}',content)

    def test_existing_project_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'thesis';dest.mkdir()
            (dest/'main.tex').write_text('user work')
            result=self.run_init(dest)
            self.assertNotEqual(result.returncode,0)
            self.assertEqual((dest/'main.tex').read_text(),'user work')

if __name__=='__main__':
    unittest.main()
