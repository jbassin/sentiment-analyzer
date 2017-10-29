from textblob import TextBlob

class Sentiment:

    def __init__(self):
        return

    def get_polarity(self, dictionary):
        return dictionary['negate'] * int(TextBlob(dictionary['word']).sentiment.polarity * 100.0)
