import os

def check_for_quotes(line):

    count = line.count('"')

    if count == 0:
        return None
    elif count % 2 != 0:
        raise Exception("Quotation marks are not even; error in parsing quotes")
    
    locations = [i for i, ltr in enumerate(line) if ltr == '"']

    quote_object = [ line[locations[i]:locations[i+1]+1] for i in xrange(0,count,2) ]

    return quote_object


def getQuotes( text ):
    quotes = {}
    potential = []

    for line in text:
        if 'said' in line or 'says' in line or 'told' in line:
            potential.append(line)

    for line in potential:
        tmp = check_for_quotes(line)
        if tmp != None:
            quotes[line] = tmp

    return quotes

if __name__ == '__main__':
    directory = 'ArticleTest/'
    articles = ['cnn.txt','guard.txt','huff.txt', 'ny.txt']
    articles = [ os.path.join(directory, i) for i in articles]
    
    master = {}
    master['articles'] = []

    for article in articles:
        article_dict = {}
        article_dict['name'] = article
        with open(article, 'r') as f:
            article_dict['quotes'] = getQuotes( f )

        master['articles'].append(article_dict)
