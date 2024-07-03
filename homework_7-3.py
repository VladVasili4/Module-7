import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *files):
        self.file_names = files
        print(self.file_names)

    def get_all_words(self):
        self.all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as text:
                for line in text:
                    lines = line.lower()
                    for j in lines:
                        if j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            lines = lines.lower().replace(j, '')
                    words = lines.split()
                    self.all_words[i] = words
                    print(self.all_words)
        return self.all_words


txt1 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
txt1.get_all_words()

#     for j in lines:
#         if j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
#             del(j)
# print(lines, end = '')
# print(i)                #     for j in lines:
#                 #         if j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
#                 #             del(j)
#                 # print(lines, end = '')
#         # print(i)

