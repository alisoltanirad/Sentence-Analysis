# https://github.com/alisoltanirad/Sentence-Analysis.git
# Dependencies: nltk
import nltk

class WFST():

    def __init__(self, sentence, grammar):
        self.grammar = grammar
        self._tokens, self._n_tokens = self._tokenize(sentence)


    def display(self, trace=False):
        print(' '.join(self._tokens), end='.\n')
        wfst = self._parse(trace)
        print('\nWFST ' +
              ' '.join(('%-4d' % i) for i in range(1, self._n_tokens+1)))
        for i in range(self._n_tokens):
            print('%d   ' % i, end=' ')
            for j in range(1, self._n_tokens+1):
                print('%-4s' % (wfst[i][j] or '.'), end=' ')
            print()


    def _parse(self, trace):
        index = dict((p.rhs(), p.lhs()) for p in self.grammar.productions())
        table = self._build_table()
        for span in range(2, self._n_tokens+1):
            for start in range(self._n_tokens+1-span):
                end = start + span
                for mid in range(start+1, end):
                    nt1, nt2 = table[start][mid], table[mid][end]
                    if nt1 and nt2 and (nt1, nt2) in index:
                        table[start][end] = index[(nt1, nt2)]
                        if trace:
                            print('[%s] %3s [%s] %3s [%s] --> [%s] %3s [%s]' % \
                                  (start, nt1, mid, nt2, end,
                                   start, index[(nt1, nt2)], end))
        return table


    def _build_table(self):
        table = [[None for i in range(self._n_tokens+1)]
                 for j in range(self._n_tokens+1)]
        for i in range(self._n_tokens):
            productions = self.grammar.productions(rhs=self._tokens[i])
            table[i][i+1] = productions[0].lhs()
        return table


    def _tokenize(self, sentence):
        tokens = sentence.split()
        return tokens, len(tokens)


def main():
    pass


if __name__ == '__main__':
    main()