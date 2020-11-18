# https://github.com/alisoltanirad/Sentence-Analysis.git
# Dependencies: nltk
import nltk

def main():
    grammar = nltk.data.load('file:grammar.cfg')
    sentence = 'Mary saw Bob'.split()
    rd_parser = nltk.RecursiveDescentParser(grammar)
    for tree in rd_parser.parse(sentence):
        print(tree)


if __name__ == '__main__':
    main()