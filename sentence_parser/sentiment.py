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
        return [sum(polarlist)/len(polarlist) * 1.4, sum(abslist)/len(abslist)]

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

        stockString = ''
        if num[0] > 40:
            stockString = 'There\'s very high opinion of this topic right now! Value is expected to rise.'
        elif num[0] > -40:
            stockString = 'Opinion tends towards the middle, value is expected to level out'
        else:
            stockString = 'There\'s very low opinion of this topic right now! Value is expected to drop.'


        return (mag + mod + pol), 'The value our algorithm assigned to the polarity was {} (-100 to 100).'.format(round(num[0], 2)), 'The value our algorithm assigned to the decisiveness was {} (0 to 100)'.format(round(num[1], 2)), stockString

