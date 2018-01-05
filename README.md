# Feeder
Automatically create a PDF file with the day's news. Currently version 0.2; still have a long way to go. 

## Installing on your computer
You can easily install Feeder on your computer. First, you'll need the `feedparser` module, which parses the RSS/XML files. Next, it would be helpful to have the entire TeX Live distribution installed on your computer. If you don't, you can *technically* download individual packages and hope it'll work, but doing a (not so) quick `sudo apt install texlive-full` will make your life easier. If you don't have either the bandwidth or the disk space for an entire TeX distro, you can also upload the resulting `.tex` file(s) to Overleaf or ShareLaTeX (along with the `newspaper-mod.sty` file). 

## Usage
Using Feeder is dead simple. Just type `feeder http://path/to/rss/feed.xml`, replacing the link with the actual URL for your RSS feed. You can use http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml for the New York Times front page, for instance. 

## Mailing lists!
I'm thinking about setting up a daily newsletter that sends the PDFs via email every morning. It might at some point have a web interface where you can subscribe, but for now this is still on the table (plenty of bugs to iron out first). 

## OOP
~~The current implementation of multiple newspapers is really shaky.~~ *Edit: Fixed!* I'm thinking about turning the functions branch into an OOP branch (although I forsee a ton of scope errors in my future). This might make it work better with different feed sources. 

## Helping out
More help is always great — this project is barely off the ground and so any bug reports, issues, or pull requests are welcome. 
