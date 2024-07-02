import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *files):
        self.file_names = files
    def printus(self):
        print(self.file_names)

    def get_all_words(self):
        self.all_words = {}
        for i in self.file_names:
            with open(i, 'a', encoding='utf-8') as text:
                print(text.readable())
                print(text.writable())

                # for lines in text:
                #     print(lines)
                #     # line = lines.lower().split()
                #     for j in lines:
                #         if j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                #             del(j)
                # print(lines, end = '')
        # print(i)


finder = WordsFinder('file1.txt, file2.txt', 'file3.txt')
txt1 = WordsFinder('7-2-1.txt')
txt2 = WordsFinder('homework_7-1.txt')
txt1.printus()
txt1.get_all_words()