# feeder
Automatically create a PDF file with the day's news 
Currently version 0.1a; don't expect anything to work right

## Installing on your computer
You can easily install Feeder on your computer. First, you'll need the `feedparser` module, which parses the RSS/XML files. Next, it would be helpful to have the entire TeX Live distribution installed on your computer. If you don't, you can *technically* download individual packages and hope it'll work, but doing a (not so) quick `sudo apt install texlive-full` will make your life easier. If you don't have either the bandwidth or the disk space for an entire TeX distro, you can also upload the resulting `.tex` file(s) to Overleaf or ShareLaTeX (along with the `newspaper-mod.sty` file). 

## Mailing lists!
I'm thinking about setting up a daily newsletter that sends the PDFs via email every morning. It might at some point have a web interface where you can subscribe, but for now this is still on the table (plenty of bugs to iron out first). 

## OOP
The current implementation of multiple newspapers is really shaky. I'm thinking about turning the functions branch into an OOP branch (although I forsee a ton of scope errors in my future). Hopefully this will make my program *not* a candidate for the "most obfuscated Python" contest. 

## Helping out
More help is always great -- this project is barely off the ground and so bug reports, issues, and pull requests are welcome. 
