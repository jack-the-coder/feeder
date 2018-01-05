# REMINDER: THIS IS PYTHON 2

import feedparser
import os, sys, datetime, re

args = sys.argv[1:]
xml = feedparser.parse(str(args[0]))

headlines = []
descriptions = []

now = datetime.datetime.now()
todaycode = str(now.month) + str(now.day) + str(now.year)

def remove_chars(entry):
    line = entry
    line = re.sub('[@]', r'\@', line)
    line = re.sub('[#]', r'\#', line)
    line = re.sub('[$]', r'\$', line)
    line = re.sub('[%]', r'\%', line)
    line = re.sub('[&]', r'\&', line)
    return line

for entry in xml.entries:
    headlines.append(remove_chars(entry.title))
    descriptions.append(remove_chars(entry.description))

with open('doc_header_f.tex', 'r') as doc_header_f:
    doc_src = doc_header_f.read()

for headline, description in zip(headlines, descriptions):
    doc_src += r'\headline{'
    doc_src += headline
    doc_src += r'}'
    doc_src += "\n\n"

    doc_src += description
    doc_src += "\n\n"

    doc_src += r'\closearticle'

with open('doc_end_f.tex', 'r') as doc_end_f:
    doc_src += doc_end_f.read()


tex_f = open('src' + todaycode + '.tex', 'w+')

try:
    tex_f.write(doc_src.encode('utf8'))
finally:
    tex_f.close()

os.system("pdflatex " + 'src' + todaycode + '.tex')
