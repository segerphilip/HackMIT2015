import indicoio 
from newspaper import Article

indicoio.config.api_key = 'deb00250e5ee7032eb2ceb562be49c09'


#To be imported from search results
urlCnn = 'http://www.cnn.com/2015/09/16/us/texas-student-ahmed-muslim-clock-bomb/'
urlGuardian = "http://www.theguardian.com/us-news/2015/sep/17/ahmed-mohamed-is-tired-excited-to-meet-obama-and-wants-his-clock-back"
urlNYT = "http://www.nytimes.com/2015/09/17/us/texas-student-is-under-police-investigation-for-building-a-clock.html?_r=0"
urlHuff = "http://www.huffingtonpost.com/entry/9th-grader-arrested-clock_55f96557e4b0b48f6701519c"

articleCnn = Article(urlNYT)
articleGuardina = Article(urlGuardian)
articleNYT = Article(urlNYT)
articleHuff = Article(urlHuff)

articleCnn.download()
articleCnn.parse()


print indicoio.sentiment(articleCnn.text)
print indicoio.political(articleCnn.text)





