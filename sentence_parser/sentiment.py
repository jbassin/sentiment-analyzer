from textblob import TextBlob

class Sentiment:

    def __init__(self):
        return

    def get_polarity(self, dictionary):
        return dictionary['negate'] * int(TextBlob(dictionary['word']).sentiment.polarity * 100.0)

    def polarity(self, list):
        polarlist = [self.get_polarity(dictionary) for dictionary in list]
        abslist = [abs(n) for n in polarlist]
        return sum(polarlist)/len(polarlist), sum(abslist)/len(abslist)

    def test(self):
        print('polarity(["hate", "spook"])) should return', self.polarity(["hate", "spook"]))