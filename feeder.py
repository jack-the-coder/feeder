# REMINDER: THIS IS PYTHON 2
import feedparser
import os, datetime



NBCxml = feedparser.parse('http://feeds.nbcnews.com/feeds/topstories')
NYTxml = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')

NBCheadlines = []
NBCdescriptions = []
NYTheadlines = []
NYTdescriptions = []

now = datetime.datetime.now()
todaycode = str(now.month) + str(now.day) + str(now.year)

for entry in NBCxml.entries:
    NBCheadlines.append(entry.title)
    print entry.title
    #authors.append(entry.dc:creator)
    #print entry.dc:creator
    NBCdescriptions.append(entry.description)
    print entry.description
    print "\n"

for entry in NYTxml.entries:
    NYTheadlines.append(entry.title)
    print entry.title
    #authors.append(entry.dc:creator)
    #print entry.dc:creator
    NYTdescriptions.append(entry.description)
    print entry.description
    print "\n"

with open('doc_header_f.tex', 'r') as doc_header_f:
    NBCdoc_src = doc_header_f.read()
    
NYTdoc_src = NBCdoc_src


for headline, description in zip(NBCheadlines, NBCdescriptions):
    NBCdoc_src += r'\headline{'
    NBCdoc_src += headline
    NBCdoc_src += r'}'
    NBCdoc_src += "\n\n"

    NBCdoc_src += description
    NBCdoc_src += "\n\n"

    NBCdoc_src += r'\closearticle'

for headline, description in zip(NYTheadlines, NYTdescriptions):
    NYTdoc_src += r'\headline{'
    NYTdoc_src += headline
    NYTdoc_src += r'}'
    NYTdoc_src += "\n\n"

    NYTdoc_src += description
    NYTdoc_src += "\n\n"

    NYTdoc_src += r'\closearticle'

with open('doc_end_f.tex', 'r') as doc_end_f:
    NBCdoc_src += doc_end_f.read()

with open('doc_end_f.tex', 'r') as doc_end_f:
    NYTdoc_src += doc_end_f.read()

NBCtex_f = open('NBC' + todaycode + '.tex', 'w+')
NYTtex_f = open('NYT' + todaycode + '.tex', 'w+')

try:
    NBCtex_f.write(NBCdoc_src.encode('utf8'))
finally:
    NBCtex_f.close()

try:
    NYTtex_f.write(NYTdoc_src.encode('utf8'))
finally:
    NBCtex_f.close()

os.system("pdflatex " + 'NBC' + todaycode + '.tex')
os.system("pdflatex " + 'NYT' + todaycode + '.tex')
