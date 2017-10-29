from sentence_parser import twitter_scraper
from sentence_parser import parse, sentiment


class TotalParse:

    def __init__(self):
        self.parser = parse.Parse()
        self.sentiment_calc = sentiment.Sentiment()
        self.twitter_calc = twitter_scraper.Twitter()

    def check_keyword(self, query, count):
        biglist = self.twitter_calc.get_text(query, count)
        bigscorelist = [self.sentiment_calc.polarity(self.parser.get_significant_words(i)) for i in biglist]
        bigpolar = sum([i[0] for i in bigscorelist])
        bigmag = sum([i[0] for i in bigscorelist])
        complete = [bigpolar, bigmag]
        return self.sentiment_calc.polarity_(complete)


parser = TotalParse()
parser.check_keyword('Clinton', 100)
