from flask import Flask
from flask import render_template
import models.query

app = Flask(__name__)

Article = models.query

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/test')
def article(Article):
    return render_template('index.html', Article=Article)

if __name__ == '__main__':
    app.debug = True
    app.run()
