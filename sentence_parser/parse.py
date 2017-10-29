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

    def sanitize_sentence(self, sentence):
        tokens = self.parser(sentence)
        output_tokens = [x if x.text != 'n\'t' else self.parser('not')[0] for x in tokens]
        return output_tokens

    def get_subtree(self, sentence):
        token_collection = {}
        for token in self.sanitize_sentence(sentence):
            pos = self.parser(token.text)[0].pos_
            if pos is 'ADJ' or pos is 'VERB' or pos is 'ADV' or pos is 'CCONJ' or pos is 'DET' or pos is 'ADP':
                token_collection[token] = list()
                for dependent_token in self.tokens_to_root(token):
                    token_collection[token].append(dependent_token)
                token_collection[token] = list(set(token_collection[token]))
        return token_collection

    def get_significant_words(self, sentence):
        token_collection = self.get_subtree(sentence)
        significant_words = []
        for k in token_collection.keys():
            local_dictionary = dict()
            local_dictionary['word'] = str(k.text)
            significant_words.append(local_dictionary)
        for k in token_collection.keys():
            pos = self.parser(k.text)[0].pos_
            if pos == 'DET' or (pos == 'CCONJ' and self.parser(k.text)[0].text[0].lower() == 'n'):
                for value in token_collection[k]:
                    pos_local = self.parser(value.text)[0].pos_
                    if pos_local is 'ADJ' or pos_local is 'ADV' or pos_local is 'VERB':
                        for dictionary in significant_words:
                            if dictionary['word'] == value.text:
                                dictionary['negate'] = -1
            if pos == 'ADJ' or pos == 'ADV' or pos == 'VERB':
                for value in token_collection[k]:
                    pos_local = self.parser(value.text)[0].pos_
                    if pos_local == 'ADP' and self.parser(value.text)[0].text[0].lower() == 'w':
                        for dictionary in significant_words:
                            if dictionary['word'] == k.text:
                                dictionary['negate'] = -1
        cleaned_significant_words = significant_words.copy()
        for dictionary in significant_words:
            if self.parser(dictionary['word'])[0].pos_ == 'DET' or self.parser(dictionary['word'])[0].pos_ == 'CCONJ' or self.parser(dictionary['word'])[0].pos_ == 'ADP':
                cleaned_significant_words.remove(dictionary)
        for dictionary in cleaned_significant_words:
            if 'negate' not in dictionary:
                dictionary['negate'] = 1
        return cleaned_significant_words


    def tokens_to_root(self, token):
        tokens_to_root = []
        while token.head is not token:
            tokens_to_root.append(token)
            token = token.head
            tokens_to_root.append(token)
        return tokens_to_root
