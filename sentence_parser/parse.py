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
        corpus = (list(self.parser(sentence).sents)[0])
        children = list(corpus.root.children)
        print(self.get_children(children))
        # for child in children:
        #     children1 = list(child.children)
        #     if not children1:
        #         print('AHH')
        #     else:
        #         for child1 in children1:
        #             children2 = list(child1.children)
        #             print(children2)

    def get_children(self, parents):
        if not parents:
            return None
        for parent in parents:
            child = list(parent.children)
            if not child:
                return '({})'.format(parent)
            else:
                return self.get_children(child)

    def tokens_to_root(self, token):
        """
        Walk up the syntactic tree, collecting tokens to the root of the given `token`.
        :param token: Spacy token
        :return: list of Spacy tokens
        """
        tokens_to_r = []
        while token.head is not token:
            tokens_to_r.append(token)
            token = token.head
            tokens_to_r.append(token)

        return tokens_to_r

