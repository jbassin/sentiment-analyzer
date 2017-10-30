from sentence_parser import twitter_scraper
from sentence_parser import parse, sentiment
import flask
from flask import Flask, Response, request, render_template, redirect, url_for


class TotalParse:

    def __init__(self):
        self.parser = parse.Parse()
        self.sentiment_calc = sentiment.Sentiment()
        self.twitter_calc = twitter_scraper.Twitter()

    def check_keyword(self, query, count):
        biglist = self.twitter_calc.get_text(query, count)
        bigscorelist = [self.sentiment_calc.polarity(self.parser.get_significant_words(i)) for i in biglist if self.sentiment_calc.polarity(self.parser.get_significant_words(i)) != (0, 0)]
        bigpolar = sum([i[0] for i in bigscorelist])/len([i[0] for i in bigscorelist])
        bigmag = sum([i[1] for i in bigscorelist])/len([i[1] for i in bigscorelist])
        complete = [bigpolar, bigmag]
        return self.sentiment_calc.polarity_(complete)


parser = TotalParse()
result = parser.check_keyword('Trump', 100)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



# @app.route('/search')
# def search():

@app.route('/search', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        key = request.form.get('key')
        quant = 250
        if len(key) != 0:
            res, res1, res2, res3 = parser.check_keyword(key, quant)
            return render_template('index.html', message=res, message1=res1, message2=res2, message3=res3)
    else:
        return render_template('search.html')


# @app.route('/results')
# def index():


if __name__ == "__main__":
    app.run()
