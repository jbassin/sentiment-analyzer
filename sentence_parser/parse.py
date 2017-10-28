import spacy


class Parse:

    def __init__(self):
        self.parser = spacy.load('en')
        return

    def pos_tag(self, sentence):
        corpus = self.parser(sentence)
        for word in corpus:
            print(word.lemma_, word.tag_, word.dep_, word.head.lemma_)
        return

    def pos_adj_stripper(self, sentence):
        corpus = self.parser(sentence)
        for word in corpus:
            if word.pos_ is 'ADJ' and word.tag_ is not 'PRP$':
                print(word.text, word.tag_)
        return

    def get_subtree(self, sentence):
        corpus = self.parser(sentence)
        subtrees = list([w for w in corpus if w.head is w][0].lefts)
        for subtree in subtrees:
            for descendant in subtree.subtree:
                print(descendant)
