from newspaper import Article as NewsArticle
import indicoio
import unidecode

class Article(object):

	def __init__(self, url):
		self.url = url

	def get_source(self):
		article = NewsArticle(self.url)

		article.download()
		article.parse()

		punctuation = { 0x2018:0x27, 0x2019:0x27, 0x201C:0x22, 0x201D:0x22 }

		raw_text = article.text.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c","'").replace(u"\u201d", "'")

		raw_text.translate(punctuation).encode('utf-8')

		print raw_text.split('\n\n')

		# print raw_text

		# return article.text


	def get_sentiment(self, text):
		return indicoio.sentiment("TODO FIGURE OUT REPRESENTATION OF DATA")


if __name__ == "__main__":
	myArticle = Article("http://www.theguardian.com/us-news/2015/sep/19/ted-cruz-hillary-clinton-mackinac-republican-leadership-conference")

	myArticle.get_source()