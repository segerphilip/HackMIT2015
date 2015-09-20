from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def start():
  return render_template('start.html')

@app.route('/', methods=['POST'])
def requested_query():
    if request.method == 'POST':
        text = request.form['search']
        if text == '':
            return start()
    
        return article(text)

    return start()

@app.route('/test')
def article(query):
    print query
    return render_template('index.html', link=link, articleTitle=articleTitle, facts=facts)

if __name__ == '__main__':
    app.debug = True
    app.run()
