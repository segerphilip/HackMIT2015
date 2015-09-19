import indicoio
import os

indicoio.config.api_key = os.environ.get('INDICO_KEY')

keywords = []

# single example
article = open('../ArticleTest/cnn.txt')

for line in article:
	print indicoio.keywords(line)

