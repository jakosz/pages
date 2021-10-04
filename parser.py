import re
import sys


with open('_/html_template.html', 'r') as f:
    html = f.read()

with open('_/page_template.html', 'r') as f:
    page = f.read()


KW = {'@page\n', '\n'}


try:

    res = ''
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if line not in KW:
                res += page.replace('THINGS', line)

except IndexError: 

    res = ''
    for line in sys.stdin.readlines():
        if line not in KW: 
            res += page.replace('THINGS', line)


sys.stdout.write(html.replace('THINGS', res))
