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

		raw_text = article.text

		# TODO: Paste Byron's unicode parsing shit here

	def get_sentiment(self, text):
		return indicoio.sentiment("TODO FIGURE OUT REPRESENTATION OF DATA")


if __name__ == "__main__":
	myArticle = Article("http://www.theguardian.com/us-news/2015/sep/19/ted-cruz-hillary-clinton-mackinac-republican-leadership-conference")

	myArticle.get_source()