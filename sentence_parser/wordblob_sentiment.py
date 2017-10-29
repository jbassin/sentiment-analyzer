import time

from textblob import Word

from textblob.wordnet import Synset

start_time = time.time()


like = Word("like")

like_def = [i for i in like.synsets if str(i)[len(like) + 9] == 'v']


dislike = Word("dislike")

dislike_def = [i for i in dislike.synsets if str(i)[len(dislike) + 9] == 'v']


bad = Word("bad")

bad_def = [i for i in bad.synsets if str(i)[len(bad) + 9] == 'a']


good = Word("good")

good_def = [i for i in good.synsets if str(i)[len(good) + 9] == 'a']


# like = Synset("like.v.01")
#
# enjoy = Synset('enjoy.v.01')
#
# print(like.path_similarity(enjoy))

elapsed_time = time.time() - start_time

print(elapsed_time)