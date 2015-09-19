from newspaper import Article
import unicodedata
import os

def get_text(filename, directory):
    url = urls[filename]
    a = Article(url)
    a.download()
    a.parse()

    text = a.text

    text = text.encode("ascii", 'backslashreplace')
    text = text.replace('\\u201d', '"')
    text = text.replace('\\u201c', '"')
    text = text.replace('\\u2019', '\'')

    return text.split('\n\n')


if __name__ == '__main__':
    urls = {"cnn.txt":"http://www.cnn.com/2015/09/16/us/texas-student-ahmed-muslim-clock-bomb/", 
            "guard.txt":"http://www.theguardian.com/us-news/2015/sep/16/homemade-clock-ahmed-mohamed-texas-officials-we-were-right",
            "huff.txt":"http://www.theguardian.com/commentisfree/2015/sep/16/ahmed-mohamed-clock-bigotry-american-muslims",
            "ny.txt":"http://www.nytimes.com/2015/09/19/us/irving-police-chief-defends-response-to-ahmed-mohameds-clock.html"
            }

    for filename in urls:
        print filename
        text = get_text(filename, 'ArticleTest')
        print text
        print len(text)
        exit()

        with open(os.path.join(directory,filename), 'w') as output:
            output.write(text)
