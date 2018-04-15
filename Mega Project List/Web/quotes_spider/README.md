Web scraper that goes on a website to get life quotes, and stores those quotes in a file.
I then use ~./bashrc to give me a quote every terminal session (Why not, right?)

To use the web scraper:

1. sudo apt-get install python3-pip 
2. sudo pip3 install scrapy
3. cd <The quotes_spider directory>
4. scrapy crawl quotes

Should now see a quotes.txt file with many quotes.

If you want, which I would find it unlikely, to see a quote every terminal session add this to the bottom
of you ~/.bashrc file: 
"shuf -n 1 ../quotes_spider/quote.txt"
Don't forget to replace .. with the path to the directory
