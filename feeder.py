# REMINDER: THIS IS PYTHON 2

import feedparser # Module for parsing RSS feeds
import os, sys, datetime, re # In order: for calling pdflatex, for getting args, for getting the current time, and for replacing special chars

args = sys.argv[1:] # Get the command-line args
xml = feedparser.parse(str(args[0])) # Download and parse the RSS

headlines = [] # Init some lists
descriptions = []

now = datetime.datetime.now() # Get current time
todaycode = str(now.month) + str(now.day) + str(now.year) # Make a time code

def remove_chars(entry): # Remove special characters that bother LaTeX
    line = entry
    line = re.sub('[@]', r'\@', line)
    line = re.sub('[#]', r'\#', line)
    line = re.sub('[$]', r'\$', line)
    line = re.sub('[%]', r'\%', line)
    line = re.sub('[&]', r'\&', line)
    return line

for entry in xml.entries: # Put the headlines and descriptions into lists
    headlines.append(remove_chars(entry.title))
    descriptions.append(remove_chars(entry.description))

with open('doc_header_f.tex', 'r') as doc_header_f: # Read the top part of the TeX file
    doc_src = doc_header_f.read()

for headline, description in zip(headlines, descriptions): # Add some LaTeX code for each headline
    doc_src += r'\headline{'
    doc_src += headline
    doc_src += r'}'
    doc_src += "\n\n"

    doc_src += description
    doc_src += "\n\n"

    doc_src += r'\closearticle'

with open('doc_end_f.tex', 'r') as doc_end_f: # Add the very end of the TeX file
    doc_src += doc_end_f.read()


tex_f = open('src' + todaycode + '.tex', 'w+') # Open the output TeX file for writing

try:
    tex_f.write(doc_src.encode('utf8')) # Try writing to it
finally:
    tex_f.close() # Close it safely, even if writing fails

os.system("pdflatex " + 'src' + todaycode + '.tex') # Run pdflatex to compile into PDF
