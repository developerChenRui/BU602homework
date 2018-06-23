'''a'''
# Copyright 2017 ChenRui ruirui@bu.edu
# Copyright 2017 mengxi wang wmx@bu.edu
# Copyright 2017 lyz lyz95222@bu.edu
# Copyright 2017 Yuchen Wang wangyc95@bu.edu
from collections import Counter
from sys import argv
import copy


def dfs(puzzle, vertex, word_list, deep, result,
        possible_comb, dfs_hint, dfs_hint_index):
    '''a'''
    if deep == 0:
        this_puzzle = copy.deepcopy(puzzle)
        possible_comb.append((result, this_puzzle))
    else:
        size = int(len(puzzle) ** (1/2))
        if vertex-size < 0:
            if vertex % size == 0:
                route = [vertex+1, vertex+size, vertex+size+1]
            else:
                if (vertex + 1) % size == 0:
                    route = [vertex-1, vertex+size, vertex-1+size]
                else:
                    route = [vertex+size, vertex-1,
                             vertex+1, vertex+size+1, vertex+size-1]
        elif vertex+size > len(puzzle)-1:
            if vertex % size == 0:
                route = [vertex-size, vertex-size+1, vertex+1]
            else:
                if (vertex + 1) % size == 0:
                    route = [vertex-1, vertex-size, vertex-size-1]
                else:
                    route = [vertex-1, vertex-size-1,
                             vertex-size, vertex-size+1, vertex+1]
        elif vertex % size == 0:
            route = [vertex-size, vertex-size+1,
                     vertex+1, vertex+size, vertex+size+1]
        elif (vertex + 1) % size == 0:
            route = [vertex-size, vertex-size-1, vertex-1,
                     vertex+size-1, vertex+size]
        else:
            route = [vertex-size-1, vertex-size, vertex-size+1, vertex-1,
                     vertex+1, vertex+size-1,
                     vertex+size, vertex+size+1]
        for index in route:
            if (dfs_hint[dfs_hint_index] != '*') & \
               (puzzle[index] != dfs_hint[dfs_hint_index]):
                continue
            if (puzzle[index] != '0') & (puzzle[index] in word_list):
                result += puzzle[index]
                letter = puzzle[index]
                puzzle[index] = '0'
                dfs(puzzle, index, word_list[letter], deep-1,
                    result, possible_comb, dfs_hint, dfs_hint_index+1)
                result = result[:-1]
                puzzle[index] = letter


def get_solution(puzzle, word_list, targets, ans, answers, hint, hint_nums):
    '''a'''
    if targets == []:
        print_ans = ''
        for item in ans:
            if item != '':
                print_ans += ''.join(item) + ' '
        if print_ans != '':
            answers.append(print_ans)
    else:
        if targets[0] not in word_list:
            return
        for index, letter in enumerate(puzzle):
            possible_comb = []
            if (hint[hint_nums - len(targets)][0] != '*') \
               & (letter != hint[hint_nums-len(targets)][0]):
                continue
            if letter == '0':
                continue
            if letter in word_list[targets[0]]:
                puzzle[index] = '0'
                result = letter
                dfs(puzzle, index, word_list[targets[0]][letter],
                    int(targets[0])-1,
                    result, possible_comb, hint[hint_nums-len(targets)], 1)
                for res, puz in possible_comb:
                    this_ans = copy.deepcopy(ans)
                    this_ans.append(res)
                    drop_down(puz)
                    get_solution(puz, word_list,
                                 targets[1:], this_ans, answers,
                                 hint, hint_nums)
                puzzle[index] = letter


def drop_down(puzzle):
    '''a'''
    size = int(len(puzzle) ** (1/2))
    for i in range(size, len(puzzle)):
        if (puzzle[i] == '0') & (puzzle[i-size] != '0'):
            flag = 1
            while flag:
                puzzle[i-size], puzzle[i] = puzzle[i], puzzle[i-size]
                i = i - size
                if (i < size) | ((i >= size) & (puzzle[i - size] == '0')):
                    flag = 0


def trie_generator(trie, word, index):
    '''a'''
    if index == len(word)-1:
        trie.setdefault(word[index], {})['exist'] = True
    else:
        trie_generator(trie.setdefault(word[index], {}), word, index+1)


FIRST_WORD_LIST = open(argv[1]).read().split()
SECOND_WORD_LIST = open(argv[2]).read().split()

FIRST_TRIE = {}
SECOND_TRIE = {}
for q in FIRST_WORD_LIST:
    trie_generator(FIRST_TRIE.setdefault(len(q), {}), q, 0)

for q in SECOND_WORD_LIST:
    trie_generator(SECOND_TRIE.setdefault(len(q), {}), q, 0)

INPUT_PUZZLE = ''
while 1:
    try:
        LINE = input()
    except EOFError:
        exit()
    FIND_STAR = Counter(LINE)
    if FIND_STAR['*'] <= 0:
        INPUT_PUZZLE += LINE
    else:
        LENGTHS = []
        HINT = []
        for length in LINE.split():
            LENGTHS.append(len(length))
            HINT.append(length)
        SOLUTION = []
        SOLUTIONS = []
        get_solution(list(INPUT_PUZZLE), FIRST_TRIE, LENGTHS, SOLUTION,
                     SOLUTIONS, HINT, len(HINT))
        if len(SOLUTIONS) == 0:
            SOLUTION = []
            get_solution(list(INPUT_PUZZLE), SECOND_TRIE, LENGTHS, SOLUTION,
                         SOLUTIONS, HINT, len(HINT))
        if SOLUTIONS != []:
            SOLUTIONS = list(set(SOLUTIONS))
            SOLUTIONS.sort()
            SOLUTIONS = '\n'.join(e for e in SOLUTIONS)
            print(SOLUTIONS)
        print('.')
        INPUT_PUZZLE = ''
