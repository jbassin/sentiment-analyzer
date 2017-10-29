import time

from textblob import Word

from textblob.wordnet import Synset

from nltk.corpus import wordnet as wn

start_time = time.time()


like = Word("like")
like_def = [i for i in like.synsets if str(i)[len(like) + 9] == 'v' and str(i)[8:12] == "like"]
hate = Word("hate")
hate_def = [i for i in hate.synsets if str(i)[len(hate) + 9] == 'v']
bad = Word("bad")
bad_def = [i for i in bad.synsets if str(i)[len(bad) + 9] == 'a']
good = Word("good")
good_def = [i for i in good.synsets if str(i)[len(good) + 9] == 'a' and str(i)[8:12] == "good"]


# print(like_def)

# likesyn = [wn.synset(i) for i in like_def]

# print(likesyn)


def synonyms_a(word):
    set1 = wn.synsets(word)
    set2 = list(set([str(i)[8:-7] for i in set1 if str(i)[-6] == "s"]))
    return set2

def synonyms_v(word):
    set1 = wn.synsets(word)
    set2 = list(set([str(i)[8:-7] for i in set1 if str(i)[-6] == "s"]))
    return set2


print(synonyms_a('good'))

okay = wn.synset('bad.a.01')
okayl = okay.lemma_names()

print([synonyms_a(i) for i in synonyms_a('good')])

def loopy_a(word):
    i = synonyms_a(word)
    while good not in i:
        i = [synonyms_a(f) for f in i]
    print(i)

loopy_a('')

dog = wn.synset('sour.a.01')
# print(dog.hyponyms())


liked = wn.synset('good.a.01')
liked2 = liked.lemma_names()
# print(liked.lemma_names())

# print(wn.synset(like).lemma_names())

# print(synonyms_a('chair'))

# synonyms = [i.lemma_names for i in doggy]

# print(synonyms)


# print(good_def)
# print(bad_def)
# print(like_def)
# print(hate_def)

def good(word):
    scorelist = [i.path_similarity(Synset(str(word) + '.a.01')) for i in good_def]
    scorelistrev = [i for i in scorelist if isinstance(i, int)]
    if scorelistrev == []:
        return 0
    else:
        bestword = max[scorelistrev]
        return bestword


def like(word):
    scorelist = [i.path_similarity(Synset(str(word) + '.v.01')) for i in like_def]
    print(scorelist)
    scorelistrev = [i for i in scorelist if isinstance(i, int)]
    if scorelistrev == []:
        return 0
    else:
        bestword = max[scorelistrev]
        return bestword


def hate(word):
    scorelist = [i.path_similarity(Synset(str(word) + '.v.01')) for i in hate_def]
    print(scorelist)
    # scorelistrev = [i for i in scorelist if isinstance(i, int)]
    # if scorelistrev == []:
    #     return 0
    # else:
    bestword = max[scorelist]
    return bestword


liked = Synset("like.v.01")

enjoy = Synset('enjoy.v.01')

adore = Word('adore')

hate = Word("jump")

# print(like(adore))
# print(like(hate))
#
# print(wn.synsets('good'))

elapsed_time = time.time() - start_time

import nltk

from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))


print(elapsed_time)
print('KILL ME PLEASE')