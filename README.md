# Feeder
Automatically create a PDF file with the day's news. Currently version 0.2; still have a long way to go.

## Installing on your computer
You can easily install Feeder on your computer. First, you'll need the `feedparser` module, which parses the RSS/XML files. Next, it would be helpful to have the entire TeX Live distribution installed on your computer. If you don't, you can *technically* download individual packages and hope it'll work, but doing a (not so) quick `sudo apt install texlive-full` will make your life easier. If you don't have either the bandwidth or the disk space for an entire TeX distro, you can also upload the resulting `.tex` file(s) to Overleaf or ShareLaTeX (along with the `newspaper-mod.sty` file).

## Usage
Using Feeder is dead simple. Just type `feeder http://path/to/rss/feed.xml`, replacing the link with the actual URL for your RSS feed. You can use http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml for the New York Times front page, for instance.

## Roadmap
### Mailing lists!
I'm thinking about setting up a daily newsletter that sends the PDFs via email every morning. It's still on the table as I have plenty of other things to work on and other issues to iron out.

The mailing lists feature will...

- Have a web interface for subscribing
- Send PDFs
- Allow each user to choose their own list of feeds to subscribe to
- Be a separate Python script so that you can still use Feeder standalone

### Web interface
Another possible addition, either combined or separate from the mailing lists, would be an easy web interface. Instead of having to install `feedparser`, TeX Live, and Feeder itself on your computer before you could user Feeder, a web interface would let you simply select the feed you want to use and would immediately display the PDF.


## Helping out
More help is always great — this project is barely off the ground and so any bug reports, issues, or pull requests are welcome.
