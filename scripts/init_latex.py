#!/usr/bin/env python3
"""Create a new USST thesis LaTeX working project without replacing user files."""
import argparse
import shutil
from pathlib import Path


def escape_tex(text):
    replacements = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '%': r'\%', '&': r'\&', '_': r'\_', '#': r'\#', '$': r'\$', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(replacements.get(c, c) for c in text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path, help='New project folder; must not already exist')
    parser.add_argument('--title', default='论文题目待填写')
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f'Output already exists; preserving it: {args.output}')
    template = Path(__file__).resolve().parents[1] / 'assets' / 'latex'
    shutil.copytree(template, args.output)
    (args.output / 'images').mkdir(exist_ok=True)
    main_tex = args.output / 'main.tex'
    main_tex.write_text(main_tex.read_text(encoding='utf-8').replace('@@TITLE@@', escape_tex(args.title)), encoding='utf-8')
    print(args.output.resolve())


if __name__ == '__main__':
    main()
