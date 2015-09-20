from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def start():
  return render_template('start.html')

@app.route('/test')
def article(link=['www.test.com', 'www.wow.doge', 'www.space.me'], articleTitle=['Formal Verification in Voss', 'So much Wow', 'Where is me?'], facts=['This is for chips.', 'Much text, so doge, wow.', 'Here.']):
  return render_template('index.html', link=link, articleTitle=articleTitle, facts=facts)

if __name__ == '__main__':
  app.debug = True
  app.run()
