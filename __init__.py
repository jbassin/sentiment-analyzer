from sentence_parser import parse, sentiment
from textblob import TextBlob
import pprint

parser = parse.Parse()
sentiment_calc = sentiment.Sentiment()
for dictionary in parser.get_significant_words('I don\'t hate not loving life'):
    pprint.pprint(dictionary)
    pprint.pprint(sentiment_calc.get_polarity(dictionary))

pprint.pprint(int(TextBlob('I don\'t hate not loving life').sentiment.polarity * 100.0))

# pprint.pprint(parser.get_significant_words('I don\'t hate not loving life'))


# parser = parse.Parse()
# # parser.get_significant_words('Those who find ugly meanings in beautiful things are corrupt without being charming.')
# pprint.pprint(parser.get_significant_words('I don\'t hate not loving life'))

# from textblob import TextBlob
# testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
# print(testimonial.sentiment.polarity)
# print(boots.similarity(hippos))