#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:26:02 2017

@author: chenrui
"""
import numpy as np
from collections import Counter
from sys import argv
import copy

def update_connections(index, connections):
    for item in connections:
        item[index] = False
    
def dfs(puzzle, vertex, word_list, deep, connections, result, possible_comb):
    if deep == 0:
        if 'exist' in word_list:
            possible_comb.append((result,puzzle))
        else:
            pass
    else:
        for index, node in enumerate(connections[vertex]):
            if node & (puzzle[index] in word_list):
                this_connections = copy.deepcopy(connections)
                this_result = copy.deepcopy(result)
                this_puzzle = copy.deepcopy(puzzle)
                
                this_result += puzzle[index]
                letter = this_puzzle[index]
                this_puzzle[index] = '0'
                update_connections(index,this_connections)
                dfs(this_puzzle, index, word_list[letter], deep-1, this_connections, \
                    this_result, possible_comb)
            
            
            
    
def GetSolution(puzzle, connections, word_list, targets, ans, answers):
    if targets == []:
        print_ans = ''
        for item in ans:
            print_ans += ''.join(item) + ' '
        answers.append(print_ans)
    else:
        for index,letter in enumerate(puzzle):
            possible_comb = []
            if letter == '0':
                continue
            if letter in word_list:
                this_puzzle = copy.deepcopy(puzzle)
                this_puzzle[index] = '0'
                this_connections = copy.deepcopy(connections)
                update_connections(index, this_connections)
                result = letter
                dfs(this_puzzle, index, word_list[letter], int(targets[0])-1, \
                    this_connections, result, possible_comb)
                for res, puz in possible_comb:
                    this_ans = copy.deepcopy(ans)
                    this_ans.append(res)
                    DropDown(puz)
                    GetSolution(puz, BuildConnection(puz), word_list, \
                                targets[1:], this_ans, answers)
                    
                    
       

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
        
def BuildConnection(puzzle):
    nums = len(puzzle)
    size = int(nums ** (1/2))
    connections = [[False]*nums for i in range(nums)]
    for index in range(nums):
        if puzzle[index] != '0':
            row = index // size
            col = index % size
            if col != 0:
                connections[index][index-1] = puzzle[index-1] != '0'
                if row != 0:
                    connections[index][index - size - 1] = puzzle[index - size - 1] != '0'
                if row != size - 1:
                    connections[index][index + size - 1] = puzzle[index + size - 1] != '0'
            if col != size - 1:
                connections[index][index + 1] = puzzle[index + 1] != '0'
                if row != 0:
                    connections[index][index - size + 1] = puzzle[index - size + 1] != '0'
                if row != size - 1:
                    connections[index][index + size + 1] = puzzle[index + size + 1] != '0'
            if row != 0:
                connections[index][index - size] = puzzle[index - size] != '0'
            if row != size - 1:
                connections[index][index + size] = puzzle[index + size] != '0'
    return connections
                
        
# change the word list to trie
first_word_list = open(argv[1]).read().split()
second_word_list = open(argv[2]).read().split()
first_trie, second_trie = {}, {}
for word in first_word_list:
    TrieGenerator(first_trie, word, 0)
for word in second_word_list:
    TrieGenerator(second_trie, word, 0)

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
        for length in line.split():
            lengths.append(len(length))
         # represent the graph
        connection = BuildConnection(input_puzzle)
        solution = []
        solutions = []
        input_puzzle = list(input_puzzle)
        GetSolution(input_puzzle, connection, first_trie, lengths, solution, solutions)
        if len(solutions) == 0:
            solution = []
            GetSolution(input_puzzle, connection, second_trie, lengths, solution, solutions)
        solutions = list(set(solutions))
        solutions.sort()
        solutions = '\n'.join(e for e in solutions)
#hee
        print(solutions)
        print('.')
            
        # at the end we should restart
        input_puzzle = ''
    