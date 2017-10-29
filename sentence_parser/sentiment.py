from textblob import TextBlob

class Sentiment:

    def __init__(self):
        return

    def get_polarity(self, dictionary):
        return int((dictionary['negate'] * TextBlob(dictionary['word']).sentiment.polarity * 100))

    def polarity(self, list):
        polarlist = [self.get_polarity(dictionary) for dictionary in list if self.get_polarity(dictionary) != 0]
        abslist = [abs(n) for n in polarlist]
        if len(polarlist) == 0:
            return 0,0
        return [sum(polarlist)/len(polarlist), sum(abslist)/len(abslist)]

    def polarity_(self, num):
        indifferent = 10
        weak = 30
        mild = 50
        decisive = 20
        somewhatd = 37
        neutral = 62
        somewhatm = 80

        if num[0] > 0:
            pol = 'positive '
            if abs(num[0]) >= mild:
                mod = 'strong '
            elif abs(num[0]) >= weak:
                mod = 'mild '
            elif abs(num[0]) >= indifferent:
                mod = 'weak '
            else:
                pol = ''
                mod = 'indifferent '

        elif num[0] < 0:
            pol = 'negative '
            if abs(num[0]) >= mild:
                mod = 'strong '
            elif abs(num[0]) >= weak:
                mod = 'mild '
            elif abs(num[0]) >= indifferent:
                mod = 'weak '
            else:
                pol = ''
                mod = 'indifferent '
        else:
            mod = 'very '
            pol = 'indifferent '

        if num[1] >= somewhatm:
            mag = 'mixed, but '
        elif num[1] >= neutral:
            mag = 'somewhat mixed, but '
        elif num[1] >= somewhatd:
            mag = 'neither decisive nor mixed, but '
        elif num[1] > decisive:
            mag = 'somewhat decisive, but '
        else:
            mag = 'decisive, but '
        return mag + mod + pol

