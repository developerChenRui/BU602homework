#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:26:02 2017

@author: chenrui
"""

### 1. 去掉connection
### 2. 加上hint
from collections import Counter
from sys import argv
import copy

    
def dfs(puzzle, vertex, word_list, deep, result, possible_comb):
    if deep == 0:
        if 'exist' in word_list:
            this_puzzle = copy.deepcopy(puzzle)
            possible_comb.append((result,this_puzzle))
        else:
            pass
    else:
        size = int(len(puzzle) ** (1/2))
        # first line
        if vertex-size < 0 :
            # first col
            if vertex % size == 0:
                route = [vertex+1, vertex+size, vertex+size+1]
            else:
                # last col
                if (vertex+1)%size == 0:
                    route = [vertex-1, vertex+size, vertex-1+size]
                else:
                    route = [vertex+size, vertex-1, vertex+1, vertex+size+1,vertex+size-1]
        elif vertex+size > len(puzzle)-1:
            if vertex % size == 0:
                route = [vertex-size, vertex-size+1, vertex+1]
            else:
                if (vertex+1)%size == 0:
                    route = [vertex-1, vertex-size,vertex-size-1]
                else:
                    route = [vertex-1, vertex-size-1, vertex-size, vertex-size+1, vertex+1]
        elif vertex % size == 0:
            route = [vertex-size, vertex-size+1, vertex+1, vertex+size, vertex+size+1]
        elif (vertex+1)%size == 0:
            route = [vertex-size, vertex-size-1, vertex-1, vertex+size-1, vertex+size]
        else:
            route = [vertex-size-1,vertex-size, vertex-size+1,vertex-1,vertex+1,vertex+size-1,\
                     vertex+size, vertex+size+1]
        
        for index in route:        
            if (puzzle[index] != '0') & (puzzle[index] in word_list):                
                result += puzzle[index]
                letter = puzzle[index]
                puzzle[index] = '0'
                dfs(puzzle, index, word_list[letter], deep-1, \
                    result, possible_comb)
                result = result[:-1]
                puzzle[index] = letter

    
def GetSolution(puzzle, word_list, targets, ans, answers, hint, hint_index, hint_nums):    
    if targets == []:
        print_ans = ''
        for item in ans:
            print_ans += ''.join(item) + ' '
        answers.append(print_ans)
    else:
        for index,letter in enumerate(puzzle):
            possible_comb = []
            if hint[]
            if letter == '0':
                continue
            if letter in word_list[targets[0]]:
                puzzle[index] = '0'
                result = letter
                dfs(puzzle, index, word_list[targets[0]][letter], int(targets[0])-1, \
                    result, possible_comb)
                for res, puz in possible_comb:
                    # 这里可以改一下如果puz相同那么!!!!!!!!
                    this_ans = copy.deepcopy(ans)
                    this_ans.append(res)
                    DropDown(puz)
                    GetSolution(puz, word_list, \
                                targets[1:], this_ans, answers)
                puzzle[index] = letter
                    

def DropDown(puzzle):
    size = int(len(puzzle) ** (1/2))
    for i in range(size, len(puzzle)):
        if (puzzle[i] == '0') & (puzzle[i-size] != '0'):
            flag = 1
            while flag:
                puzzle[i-size],puzzle[i] = puzzle[i],puzzle[i-size]
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
    TrieGenerator(first_trie.setdefault(len(word),{}), word, 0)

for word in second_word_list:
    TrieGenerator(second_trie.setdefault(len(word),{}), word, 0)

# initial a str for puzzle
input_puzzle = ''
    
# get the puzzle    
while 1:
    line = input()
    if line == '':
        break
    # judge if it is the end of puzzle
    find_star = Counter(line)
    # if it is still a line of puzzle
    if find_star['*'] <= 0:
        input_puzzle += line
    # if it is a line specify the lengths we begin to solve this puzzle
    else:
        lengths = []
        hint = []
        for length in line.split():
            lengths.append(len(length))
            hint.append(length)
         # represent the graph
        solution = []
        solutions = []
        input_puzzle = list(input_puzzle)
        GetSolution(input_puzzle, first_trie, lengths, solution, solutions, hint, 0, len(hint))
        if len(solutions) == 0:
            solution = []
            GetSolution(input_puzzle, second_trie, lengths, solution, solutions, hint, 0, len(hint))
        solutions = list(set(solutions))
        solutions.sort()
        solutions = '\n'.join(e for e in solutions)

        print(solutions)
        print('.')
            
        # at the end we should restart
        input_puzzle = ''
    