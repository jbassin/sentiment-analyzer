from nltk.corpus import wordnet as wn


class Sentiment:

    def __init__(self):
        self.sentiment = wn
        return

    def test(self, s):
        return self.sentiment.synsets(s)

    def sent_sent(self, sentence):
        verbs = [word[1:] for word in sentence if word[0] == 'V']
        adjs = [word[1:] for word in sentence if word[0] == 'A']
        verbscore = []
        adjscore = []

    def adj_sent(self, word):
        test(word[1].a.)

    def verb_sent(self, word):

