import spacy


class Parse:

    def __init__(self):
        self.parser = spacy.load('en')
        return
