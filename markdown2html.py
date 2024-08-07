#!/usr/bin/python3
"""Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
Requirements:

If the number of arguments is less than 2: print in STDERR Usage:
 ./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn’t exist:
print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0"""
import sys
import os
import markdown

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    if not os.path.exists(markdown_file):
        print("Missing {}".format(markdown_file), file=sys.stderr)
        sys.exit(1)

    html_file = sys.argv[2]
    sys.exit(0)
