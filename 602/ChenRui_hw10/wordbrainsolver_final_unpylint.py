# Copyright 2017 ChenRui ruirui@bu.edu
# Copyright 2017 mengxi wang wmx@bu.edu
# Copyright 2017 lyz lyz95222@bu.edu
from collections import Counter
from sys import argv
import copy
 
def dfs(puzzle, vertex, word_list, deep, result, possible_comb, dfs_hint, dfs_hint_index):
    if deep == 0:
        this_puzzle = copy.deepcopy(puzzle)
        possible_comb.append((result, this_puzzle))
    else:
        size = int(len(puzzle) ** (1/2))
        # first line
        if vertex-size < 0:
            # first col
            if vertex % size == 0:
                route = [vertex+1, vertex+size, vertex+size+1]
            else:
                # last col
                if (vertex+1)%size == 0:
                    route = [vertex-1, vertex+size, vertex-1+size]
                else:
                    route = [vertex+size, vertex-1, vertex+1, vertex+size+1, vertex+size-1]
        elif vertex+size > len(puzzle)-1:
            if vertex % size == 0:
                route = [vertex-size, vertex-size+1, vertex+1]
            else:
                if (vertex+1)%size == 0:
                    route = [vertex-1, vertex-size, vertex-size-1]
                else:
                    route = [vertex-1, vertex-size-1, vertex-size, vertex-size+1, vertex+1]
        elif vertex % size == 0:
            route = [vertex-size, vertex-size+1, vertex+1, vertex+size, vertex+size+1]
        elif (vertex+1)%size == 0:
            route = [vertex-size, vertex-size-1, vertex-1, 
                     vertex+size-1, vertex+size]
        else:
            route = [vertex-size-1, vertex-size, vertex-size+1, vertex-1, 
                     vertex+1,vertex+size-1,
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

def GetSolution(puzzle, word_list, targets, ans, answers, hint, hint_nums):
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
            if (hint[hint_nums-len(targets)][0]!='*') \
            & (letter != hint[hint_nums-len(targets)][0]):
                continue   
            if letter == '0':
                continue
            if letter in word_list[targets[0]]:
                puzzle[index] = '0'
                result = letter
                dfs(puzzle, index, word_list[targets[0]][letter], int(targets[0])-1, 
                    result, possible_comb, hint[hint_nums-len(targets)], 1)
                for res, puz in possible_comb:
                    # 这里可以改一下如果puz相同那么!!!!!!!!
                    this_ans = copy.deepcopy(ans)
                    this_ans.append(res)
                    DropDown(puz)
                    GetSolution(puz, word_list, 
                                targets[1:], this_ans, answers, 
                                hint, hint_nums)
                puzzle[index] = letter

def DropDown(puzzle):
    size = int(len(puzzle) ** (1/2))
    for i in range(size, len(puzzle)):
        if (puzzle[i] == '0') & (puzzle[i-size] != '0'):
            flag = 1
            while flag:
                puzzle[i-size], puzzle[i] = puzzle[i], puzzle[i-size]
                i = i - size
                if (i < size) | ((i >= size) & (puzzle[i-size]=='0')):
                    flag = 0
            

def TrieGenerator(trie, word, index):
    if index == len(word)-1:
        trie.setdefault(word[index],{})['exist'] = True
    else:
        TrieGenerator(trie.setdefault(word[index],{}), word, index+1)
                
        
# change the word list to trie
first_word_list = open(argv[1]).read().split()
second_word_list = open(argv[2]).read().split()

first_trie= {}
second_trie = {}
for word in first_word_list:
    TrieGenerator(first_trie.setdefault(len(word), {}), word, 0)

for word in second_word_list:
    TrieGenerator(second_trie.setdefault(len(word), {}), word, 0)

input_puzzle = ''  
while 1:
    try:
        line = input()
    except EOFError:
        exit()
    find_star = Counter(line)
    if find_star['*'] <= 0:
        input_puzzle += line
    else:
        lengths = []
        hint = []
        for length in line.split():
            lengths.append(len(length))
            hint.append(length)
        solution = []
        solutions = []
        input_puzzle = list(input_puzzle)
        GetSolution(input_puzzle, first_trie, lengths, solution, 
                    solutions, hint, len(hint))
        if len(solutions) == 0:
            solution = []
            GetSolution(input_puzzle, second_trie, lengths, solution, 
                        solutions, hint, len(hint))
        if solutions != []:
            solutions = list(set(solutions))
            solutions.sort()
            solutions = '\n'.join(e for e in solutions)
            print(solutions)
        print('.')
        input_puzzle = ''
    