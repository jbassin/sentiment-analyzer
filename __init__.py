from sentence_parser import parse, sentiment
import pprint

parser = parse.Parse()
sentiment_calc = sentiment.Sentiment()
for dictionary in parser.get_significant_words('I don\'t hate not loving life'):
    pprint.pprint(dictionary)
    sentiment_calc.get_polarity(dictionary)


# parser = parse.Parse()
# # parser.get_significant_words('Those who find ugly meanings in beautiful things are corrupt without being charming.')
# pprint.pprint(parser.get_significant_words('I don\'t hate not loving life'))

# from textblob import TextBlob
# testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
# print(testimonial.sentiment.polarity)
# print(boots.similarity(hippos))