from nltk.corpus import wordnet as wn


class Sentiment:

    def __init__(self):
        self.sentiment = wn
        return

    def test(self, s):
        return self.sentiment.synsets(s)
