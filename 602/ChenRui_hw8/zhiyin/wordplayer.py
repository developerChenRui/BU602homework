# Copyright 2017 jbc@bu.edu

"""Assignment9"""
from sys import argv, exit
from collections import defaultdict
from itertools import combinations


def main():
    "main"
    worddict = defaultdict(lambda: defaultdict(list))

    with open(argv[1]) as dic:
        for word in dic:
            word = word.rstrip()
            worddict[len(word)][''.join(sorted(word))].append(word)

    while 1:
        results = []
        letters, length = input().split()
        length, letters = int(length), ''.join(sorted(letters))
        if length == 0:
            exit(0)
        ltrlen = len(letters)
        if length == ltrlen:
            results = worddict[length][letters]
        elif ltrlen - length < 4:
            comblist = set(list(combinations(letters, length)))
            comblist = [''.join(comb) for comb in comblist]
            for comb in comblist:
                if comb in worddict[length]:
                    for i in worddict[length][comb]:
                        results.append(i)
        else:
            for key in worddict[length]:
                ltrs = list(letters)
                for char in key:
                    if char not in letters:
                        break
                    else:
                        try:
                            ltrs.remove(char)
                        except:
                            break
                else:
                    for ans in worddict[length][key]:
                        results.append(ans)
        if results:
            print('\n'.join(sorted(results)))
        print('.')


if __name__ == '__main__':
    main()
