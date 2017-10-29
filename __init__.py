from sentence_parser import twitter_scraper
from sentence_parser import parse, sentiment



parser = parse.Parse()
sentiment_calc = sentiment.Sentiment()
twitter_calc = twitter_scraper.Twitter()
biglist = twitter_calc.get_text('Trump', 100)
# biglist = []
bigscorelist = [sentiment_calc.polarity(parser.get_significant_words(i)) for i in biglist]
bigpolar = sum([i[0] for i in bigscorelist])
bigmag = sum([i[0] for i in bigscorelist])
complete = [bigpolar, bigmag]

print(sentiment_calc.polarity_(complete))
