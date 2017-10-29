import nltk
from nltk.corpus import wordnet

from textblob import TextBlob

def syn_(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms


# [for syn in wordnet.synsets("good")] [l.name() for l in syn.lemmas]

# print([l.name() for l in [syn.lemmas for syn in wordnet.synsets("good")]])

print(syn_('good'))

sentence = TextBlob('hate')

print(sentence.sentiment.polarity)

# print(set(synonyms))
# print(set(antonyms))


# synonyms = [for syn in wordnet.synsets("good")]

# print([wordnet.synsets(i) for i in synonyms])
