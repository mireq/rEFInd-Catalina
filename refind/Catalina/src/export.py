#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess
from pathlib import Path


DPI = 96
DEST_DIR = os.pardir


def convert_svg():
	svg_files = [os.path.splitext(filename)[0] for filename in Path('.').glob('**/*.svg')]
	for filename in svg_files:
		out_dir = os.path.join(DEST_DIR, os.path.dirname(filename))
		out_filename = os.path.join(DEST_DIR, filename + '.png')
		os.makedirs(out_dir, exist_ok=True)
		if not os.path.exists(out_filename):
			cmd_args = ['inkscape', filename + '.svg', '-e', out_filename, '-d', str(DPI)]
			subprocess.call(cmd_args)
			cmd_args = ['optipng', '-o7', out_filename]
			subprocess.call(cmd_args)
			cmd_args = ['advpng', '-z', '-4', out_filename]
			subprocess.call(cmd_args)
			cmd_args = ['pngout-static', '-k0', out_filename]
			subprocess.call(cmd_args)

def main():
	convert_svg()


if __name__ == "__main__":
	main()
