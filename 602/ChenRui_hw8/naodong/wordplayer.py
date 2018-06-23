# Copyright 2017 Jiaxin Tang jxtang@bu.edu
# Copyright 2017 Ziran Li zrli@bu.edu
import sys
import itertools

dic = {}
words = open(sys.argv[1]).read()
for line in words.split():
    key1 = len(line)
    key2 = tuple(sorted(line))
    dic.setdefault(key1, {})
    dic[key1].setdefault(key2, [])
    dic[key1][key2].append(line)


def contain(l1, s1):
    for i in l1:
        if i not in s1:
            return False
        s1 = s1.replace(i, "", 1)
    return True

while(True):
    result = []
    char, num = input().split()
    chars = sorted(char)
    nums = int(num)
    if nums <= 0:
        exit(0)
    if nums in dic:
        if nums > 0.25 * len(chars) and nums < 0.75 * len(chars):
            for i in dic[nums]:
                if contain(i, char):
                    result.extend(dic[nums][i])
        else:
            combinelist = set(itertools.combinations(''.join(chars), nums))
            for i in combinelist:
                if i in dic[nums]:
                    result.extend(dic[nums][i])
    if result:
        print(('\n'.join(sorted(result))))
    print('.')
