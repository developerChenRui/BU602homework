# Copyright 2017 ChenRui ruirui@bu.edu
# Copyright 2017 mengxi wang wmx@bu.edu
# Copyright 2017 lyz lyz95222@bu.edu
"""assignment 8"""
from sys import argv
from collections import defaultdict
from itertools import combinations


def contain(word_indict, input_word):
    "contain"
    for i in word_indict:
        if i not in input_word:
            return False
        input_word = input_word.replace(i, "", 1)
    return True


def main():
    "main"
    worddict = defaultdict(lambda: defaultdict(list))

    with open(argv[1]) as file:
        for line in file:
            line = line[:-1]
            worddict[len(line)][tuple(sorted(line))].append(line)

    while True:
        result = []
        line = input().split(' ')
        length = int(line[1])
        letter = sorted(line[0])
        if int(line[1]) == 0:
            break
        if len(line[0]) == int(line[1]):
            result = worddict[int(line[1])][tuple(sorted(line[0]))]
        elif (len(line[0]) - int(line[1])) < 5:
            comblist = set(combinations(letter, length))
            comblist = [tuple(comb) for comb in comblist]
            for comb in comblist:
                if comb in worddict[length]:
                    result.extend(worddict[length][comb])
        else:
            word_same_num = worddict[length]
            for word in word_same_num:
                if contain(word, line[0]):
                    result.extend(word_same_num[word])
        for item in sorted(result):
            print(item)
        print('.')

if __name__ == '__main__':
    main()
