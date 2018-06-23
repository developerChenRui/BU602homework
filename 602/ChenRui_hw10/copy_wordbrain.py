import numpy as np
import copy
import itertools
from sys import argv, stdin
from collections import Counter

class Trie(object):
    def __init__(self, filename):
        self.tree = {}
        for word in open(filename, "r").read().split():
            tree = self.tree
            for char in word:
                if char not in tree:
                    tree[char] = {}
                tree = tree[char]
            tree['exist'] = True

    def search(self, word):
        tree = self.tree
        for char in word:
            if char not in tree:
                return 0
            tree = tree[char]
        return 1 if 'exist' in tree else 2


def Drop(wordpool, word):
    result = np.copy(wordpool)
    for n in word:
        result[n[0][0]][n[0][1]] = '*'
    for n in range(result.shape[0]-1):
        for m in range(result.shape[1]):
            if(result[n][m] == '*'):
                continue
            else:
                if result[n+1][m] == '*':
                    k = j = n
                    while result[k+1][m] == '*':
                        k = k+1
                        if k == result.shape[0]-1:
                            break
                    while j >= 0:
                        result[j+k-n][m] = result[j][m]
                        result[j][m] = '*'
                        j = j-1
    return result


def word_generator(strings, wordSize, mode):
    size = len(strings)
    relations = {}
    for i in range(size):
        for j in range(size):
            key = (i, j)
            value = set()
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    else:
                        col = (i+x)
                        row = (j+y)
                        if col < 0 or row < 0 or col >= size or row >= size:
                            continue
                        elif strings[col][row] == '*':
                            continue
                        else:
                            value.add((col, row))
            relations[key] = value
    intermediateKeys = {}
    allWordsPossible = []
    for k in relations.keys():
        intermediateKeys[1] = [[k]]
        count = 1
        while count <= wordSize:
            countList = list()
            for item in intermediateKeys[count]:
                temp = ''
                for itm in range(0, count):
                    temp += str(strings[item[itm][0]][item[itm][1]])
                if mode == 0:
                    if small_dict.search(temp) == 0:
                        continue
                else:
                    if large_dict.search(temp) == 0:
                        continue
                lastKey = item[-1]
                values = relations[lastKey]
                for value in values:
                    nodeVisited = False
                    newList = []
                    for data in item:
                        if data == value:
                            nodeVisited = True
                            break
                        newList.append(data)
                    if not nodeVisited:
                        newList.append(value)
                        countList.append(newList)
            count += 1
            intermediateKeys[count] = countList
        allWordsPossible.extend(intermediateKeys[wordSize])
        returnList = []
        for listOfIndices in allWordsPossible:
            word = ''
            listOfSets = []
            for indices in listOfIndices:
                word += str(strings[indices[0]][indices[1]])
                indexSet = (indices, strings[indices[0]][indices[1]])
                listOfSets.append(indexSet)
            if mode == 0:
                if small_dict.search(word) == 1:
                    returnList.append(listOfSets)
            else:
                if large_dict.search(word) == 1:
                    returnList.append(listOfSets)
    if len(returnList) == 0:
        return returnList
    final = []
    dict_catogory = {}
    for i in returnList:
        word = ''
        for j in i:
            word += j[1]
        a = Drop(strings, i).tostring()
        if a in dict_catogory:
            word_family[mapping[a]].append(word)
            dict_catogory[a].append(i)
        else:
            dict_catogory[a] = [i]
            mapping[a] = word
            word_family[word] = [word]
            final.append(i)
    return final


def find_solution(count, wordpool, length_list, prev_result, mode):
    if count == len(length_list):
        yield prev_result
        return
    a = word_generator(wordpool, length_list[count], mode)
    if len(a) == 0:
        return
    for n in a:
        result = copy.deepcopy(prev_result)
        temp = copy.deepcopy(wordpool)
        updated = Drop(temp, n)
        partial_solution = ''
        for m in n:
            partial_solution = partial_solution + m[1]
        result.append(partial_solution)
        yield from find_solution(count+1, updated, length_list, result, mode)


def exe(large_dict, small_dict, word_pool, lengths):
    succeeded = [i for i in find_solution(0, word_pool, lengths, [], 0)]
    if len(succeeded) == 0:
        succeeded = [i for i in find_solution(0, word_pool, lengths, [], 1)]
        succeeded.sort()
        succeeded = list(k for k, _ in itertools.groupby(succeeded))
    for k in succeeded:
        onelist = []
        for i in range(len(k)):
            word_family[k[i]].sort()
            temp = list(k for k, _ in itertools.groupby(word_family[k[i]]))
            onelist.append(temp)
        solution = list(itertools.product(*onelist))
        for i in solution:
            print(' '.join(i))
        print('.')
        
small_dict = Trie(argv[1])
large_dict = Trie(argv[2])
word_family = {}
mapping = {}
result = []

count = 0 
flag_init = 1     
for line in stdin:
    if line == '\n':
        break
    
    find_star = Counter(line)
    size = len(line)
    if find_star['*'] <= 0:
        for letter in line:
            if flag_init:
                word_pool = np.empty([size, size], dtype=str)
                word_pool[count // size][count % size] = letter
                flag_init = 0
            else:
                word_pool[count // size][count % size] = letter
            count += 1        
    else:
        lengths = []
        for length in line.split():
            lengths.append(len(length))
        exe(large_dict, small_dict, word_pool, lengths)
        flag_init = 1
        count = 0

