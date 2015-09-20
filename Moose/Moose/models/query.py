import urllib
import requests
import os
import json

API_KEY = os.getenv('GOOGLE_API')

SEARCH_ENGINE_ID = '015040051912301786117:ukzldfl328w'


class Query(object):
    def __init__(self, query):
        self.query = query.replace(' ','+')

    def generate_query(self, iteration):
        if iteration != 0:
            template = ['https://www.googleapis.com/customsearch/v1?highrange&start=', str(iteration), '&key=',API_KEY,'&cx=',SEARCH_ENGINE_ID,'&q=', self.query]
        else: 
            template = ['https://www.googleapis.com/customsearch/v1?highrange&key=',API_KEY,'&cx=',SEARCH_ENGINE_ID,'&q=', self.query]

        url = ''.join(template)
        return url
        
    def sort_urls(self, urls):
        ret = {'cnn':[], 'guardian':[], 'huffington':[], 'nytimes':[]}
        for i in urls:
            if 'cnn' in i:
                ret['cnn'].append(i)
            elif 'guardian' in i:
                ret['guardian'].append(i)
            elif 'huffington' in i:
                ret['huffington'].append(i)
            elif 'nytimes' in i:
                ret['nytimes'].append(i)
        
        return ret

    def get_urls(self):
        # Returns a dictionary object with links as the values
        urls = []
        for i in xrange(5):
            url = self.generate_query( 10 * i )
            response = requests.get(url)
            response = json.loads(response.content)
            if 'error' in response.keys():
                raise Exception("Error")

            for i in response['items']:
                urls.append(i['link'])

        return self.sort_urls(urls)

if __name__ == '__main__':
    test = Query('ahmed mohamed')
    urls = test.get_urls()
