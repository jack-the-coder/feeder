# REMINDER: THIS IS PYTHON 2

## Import modules
import feedparser # For parsing RSS/XML files
import os, datetime # For compiling and getting the date and time, respectively

## Define some functions
def parse(): # Get and parse the feeds
    NBCxml = feedparser.parse('http://feeds.nbcnews.com/feeds/topstories') # Get the NBC feed
    NYTxml = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml') # Get the NYT feed

def create_lists(): # Make lists for use later on
    NBCheadlines = []
    NBCdescriptions = []
    NYTheadlines = []
    NYTdescriptions = []

def get_time(): # Get the current datetime and make a code out of it
    now = datetime.datetime.now()
    todaycode = str(now.month) + str(now.day) + str(now.year) # Make the code

def append_entries(xml, headlines, descriptions): # Put the individual entries in the lists from create_lists()
    for entry in xml.entries:
        headlines.append(entry.title)
        print entry.title # Debugging
        descriptions.append(entry.description)
        print entry.description # Debugging
        print "\n" # Debugging

def make_headlines(doc_src, headlines, descriptions): # Turn the headlines into LaTeX
    for headline, description in zip(headlines, descriptions):
        doc_src += r'\headline{' # Use raw strings to prevent issues with escape chars
        doc_src += headline
        doc_src += r'}'
        doc_src += "\n\n"

        doc_src += description
        doc_src += "\n\n"

        doc_src += r'\closearticle'


def add_end(doc_src): # Add the end of the file from doc_end_f.tex
    with open('doc_end_f.tex', 'r') as doc_end_f:
        doc_src += doc_end_f.read()


def open_for_write(tex_f, newspaper): # Open the files for writing
    tex_f = open(newspaper + todaycode + '.tex', 'w+')

def write_to_tex_f(tex_f, doc_src): # Write the LaTeX code to the files
    try: # Use try/finally to prevent copy-on-write issues
        tex_f.write(doc_src.encode('utf8'))
    finally:
        tex_f.close()

def compile_pdf(newspaper): # Tell pdflatex to compile the PDF files
    os.system("pdflatex " + newspaper + todaycode + '.tex')


## Use the functions
parse()
create_lists()
get_time()

append_entries(NBCxml, NBCheadlines, NBCdescriptions)
append_entries(NYTxml, NYTheadlines, NYTdescriptions)

with open('doc_header_f.tex', 'r') as doc_header_f: # Put the header (and preamble) in the document
    NBCdoc_src = doc_header_f.read()

NYTdoc_src = NBCdoc_src # Since the headers are all the same, set the contents of each document to the same thing

make_headlines(NBCdoc_src, NBCheadlines, NBCdescriptions)
make_headlines(NYTdoc_src, NYTheadlines, NYTdescriptions)

add_end(NBCdoc_src)
add_end(NYTdoc_src)

open_for_write(NBCtex_f, 'NBC')
open_for_write(NYTtex_f, 'NYT')

write_to_tex_f(NBCtex_f, NBCdoc_src)
write_to_tex_f(NYTtex_f, NYTdoc_src)

compile_pdf('NBC')
compile_pdf('NYT')
