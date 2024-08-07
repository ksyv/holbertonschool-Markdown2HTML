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
import re

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
    # Improve markdown2html.py by parsing Headings Markdown
    # syntax for generating HTML heading level
    with open(markdown_file, "r") as md_f:
        with open(html_file, "w") as html_f:
            in_ul_list = False
            in_ol_list = False
            for line in md_f:
                line = re.sub(r'^(#{1}) (.*)', r'<h1>\2</h1>', line)
                line = re.sub(r'^(#{2}) (.*)', r'<h2>\2</h2>', line)
                line = re.sub(r'^(#{3}) (.*)', r'<h3>\2</h3>', line)
                line = re.sub(r'^(#{4}) (.*)', r'<h4>\2</h4>', line)
                line = re.sub(r'^(#{5}) (.*)', r'<h5>\2</h5>', line)
                line = re.sub(r'^(#{6}) (.*)', r'<h6>\2</h6>', line)
                # Improve markdown2html.py by parsing Unordered listing syntax
                # for generating HTML:
                # Syntax: (you can assume it will be strictly this syntax)
                # - Hello
                # - Bye
                # Html generated:
                # <ul>
                # <li>Hello</li>
                # <li>Bye</li>
                # </ul>
                if re.match(r'^- ', line):
                    if not in_ul_list:
                        if in_ol_list:
                            html_f.write('</ol>\n')
                            in_ol_list = False
                        html_f.write('<ul>\n')
                        in_ul_list = True
                    line = re.sub(r'^- (.*)', r'<li>\1</li>', line)
                else:
                    if in_ul_list:
                        html_f.write('</ul>\n')
                        in_ul_list = False
                # Improve markdown2html.py by parsing Ordered listing syntax for generating HTML:
                # Syntax: (you can assume it will be strictly this syntax)
                # Markdown:
                # * Hello
                # * Bye
                # HTML generated:
                # <ol>
                # <li>Hello</li>
                # <li>Bye</li>
                # </ol>
                if re.match(r'^\* ', line):
                    if not in_ol_list:
                        if in_ul_list:
                            html_f.write('</ul>\n')
                            in_ul_list = False
                        html_f.write('<ol>\n')
                        in_ol_list = True
                    line = re.sub(r'^\* (.*)', r'<li>\1</li>', line)
                else:
                    if in_ol_list:
                        html_f.write('</ol>\n')
                        in_ol_list = False
                
                html_f.write(line)
            # Close the list if the file ends while in_list is True
             # Close any open lists at the end of the file
            if in_ul_list:
                html_f.write('</ul>\n')
            if in_ol_list:
                html_f.write('</ol>\n')
    sys.exit(0)
