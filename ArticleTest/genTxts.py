from newspaper import Article

urls = {"cnn.txt":"http://www.cnn.com/2015/09/16/us/texas-student-ahmed-muslim-clock-bomb/", 
		"guard.txt":"http://www.theguardian.com/us-news/2015/sep/16/homemade-clock-ahmed-mohamed-texas-officials-we-were-right",
		"huff.txt":"http://www.theguardian.com/commentisfree/2015/sep/16/ahmed-mohamed-clock-bigotry-american-muslims",
		"ny.txt":"http://www.nytimes.com/2015/09/19/us/irving-police-chief-defends-response-to-ahmed-mohameds-clock.html"}

for filename in urls:
	url = urls[filename]
	a = Article(url)
	a.download()
	a.parse()

	text = a.text
	encodedText = text.encode('utf-8')
	with open(filename, 'w') as output:
		output.write(encodedText)
