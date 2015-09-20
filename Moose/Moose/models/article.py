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
        raw_text = raw_text.replace('\\u2026', '...')
        raw_text = raw_text.replace('\\u2013', '-')

        return raw_text.split('\n\n')

    def get_sentiment(self, text):
        return (sum(indicoio.sentiment(sentence) for sentence in text))/float(len(text))


    def check_for_quotes(self, line):
        count = line.count('"')

        if count == 0:
            return None
        elif count % 2 != 0: # TODO: This will be an edge case, ignore for now
            return None
        
        locations = [i for i, ltr in enumerate(line) if ltr == '"']
        quote_object = [ line[locations[i]:locations[i+1]+1] for i in xrange(0,count,2) ]
        return quote_object

    def get_quotes(self):
        quotes = {}
        potential = []

        # Get potential quotes
        keywords = ['said', 'says', 'told']
        for line in self.raw_text:
            if [ True for i in keywords if i in line ]: 
                potential.append(line)

        # Extract only the sentence with the quote in it
        new = []
        for line in potential:
            while( line.find('.') < line.find('"') ):
                print "Yup"
                line = line[line.find('.')+1:].strip()
                new.append(line)
            else:
                line = line.strip()
                new.append(line)
        potential = new

        # Extract just the quoted section to check for redundancy later on
        for line in potential:
            tmp = self.check_for_quotes(line)
            if tmp != None:
                # TODO: Might switch tmp : line, so that quoted section can call full sentence
                quotes[line] = tmp 

        return quotes

if __name__ == "__main__":
    myArticle = Article("http://www.theguardian.com/us-news/2015/sep/19/ted-cruz-hillary-clinton-mackinac-republican-leadership-conference")

    #print myArticle.get_source()
    for i in myArticle.quotes:
        print i
        print
