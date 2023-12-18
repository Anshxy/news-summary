from flask import Flask, render_template, request
from newspaper import Article
import nltk

# Download NLTK resources if not downloaded
nltk.download('punkt')

app = Flask(__name__)

def get_article_info(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return {
        'title': article.title,
        'summary': article.summary,
        'authors': article.authors
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    article_info = {}
    if request.method == 'POST':
        url = request.form['url']
        article_info = get_article_info(url)
    return render_template('index.html', article_info=article_info)

if __name__ == '__main__':
    app.run(debug=True)
