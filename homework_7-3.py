import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        self.all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as text:
                self.line = []
                for line in text:
                    for j in line:
                        if j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            line = line.lower().replace(j, '')
                    words = line.split()
                    self.line = self.line + words
            self.all_words[i] = self.line

        return self.all_words

    def find(self, word):
        self.word = word.lower()
        for i in self.all_words:
            line = self.all_words[i]
            if self.word in line:
                k = line.index(self.word) + 1
                fin = {i:k}
        return fin

    def count(self, word):
        self.word = word.lower()
        for i in self.all_words:
            line = self.all_words[i]
            if self.word in line:
                k = line.count(self.word)
                fin = {i:k}
        return fin





finder1 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
print(finder1.get_all_words())
finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
