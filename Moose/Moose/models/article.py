from newspaper import Article as NewsArticle
import indicoio

class Article(object):

    def __init__(self, url):
        self.url = url
        self.raw_text = self.get_source()
        self.quotes = self.get_quotes()

    def get_source(self):
        article = NewsArticle(self.url)

        article.download()
        article.parse()

        raw_text = article.text
        raw_text = raw_text.encode("ascii", 'backslashreplace')
        raw_text = raw_text.replace('\\u201d', '"')
        raw_text = raw_text.replace('\\u201c', '"')
        raw_text = raw_text.replace('\\u2019', '\'')
        raw_text = raw_text.replace('\\u2018', '\'')

        return raw_text.split('\n\n')

    def get_sentiment(self, text):
        return (sum(indicoio.sentiment(sentence) for sentence in text))/float(len(text))

    def get_political(self, text):
        return (sum(indicoio.political(sentence) for sentence in text))/float(len(text))

    def check_for_quotes(self, line):
        count = line.count('"')

        if count == 0:
            return None
        elif count % 2 != 0:
            #raise Exception("Quotation marks are not even; error in parsing quotes")
            return None
        
        locations = [i for i, ltr in enumerate(line) if ltr == '"']
        quote_object = [ line[locations[i]:locations[i+1]+1] for i in xrange(0,count,2) ]
        return quote_object

    def get_quotes(self):
        quotes = {}
        potential = []

        for line in self.raw_text:
            if 'said' in line or 'says' in line or 'told' in line:
                potential.append(line)

        for line in potential:
            tmp = self.check_for_quotes(line)
            if tmp != None:
                quotes[line] = tmp

        return quotes

if __name__ == "__main__":
    myArticle = Article("http://www.theguardian.com/us-news/2015/sep/19/ted-cruz-hillary-clinton-mackinac-republican-leadership-conference")

    print myArticle.get_source()

