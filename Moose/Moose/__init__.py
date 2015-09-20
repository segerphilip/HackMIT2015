from flask import Flask
from flask import render_template
from models.query import Query

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/test')
def article():
    query = Query('')
    # facts, title, url, sentiment, political, summary
    query.create_fake()
    return render_template('index.html', facts=query.facts, articles=query.articles)

if __name__ == '__main__':
    app.debug = True
    app.run()
