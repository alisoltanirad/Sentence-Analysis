# https://github.com/alisoltanirad/Sentence-Analysis.git
# Dependencies: nltk
import nltk

class WFST():

    def __init__(self, sentence, grammar):
        tokens, n_tokens = self._tokenize(sentence)
        table = self._build_table(tokens, n)


    def _tokenize(self, sentence):
        tokens = sentence.split()
        return tokens, len(tokens)


def main():
    grammar = nltk.data.load('file:grammar.cfg')
    sentence = 'Mary saw a dog'.split()
    sr_parser = nltk.ShiftReduceParser(grammar, trace=2)
    for tree in sr_parser.parse(sentence):
        print(tree)


if __name__ == '__main__':
    main()