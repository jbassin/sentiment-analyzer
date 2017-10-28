from sentence_parser import parse, sentiment

parser = parse.Parse()
parser.get_subtree('Those who find ugly meanings in beautiful things are corrupt without being charming.')


sentiment = sentiment.Sentiment()
print(sentiment.test('dog'))