#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:55:33 2017

@author: chenrui
"""
import numpy as np
from collections import Counter
from sys import argv, stdin

def buildConnection(strMaze, n):
    connection = [0] * (n ** 2)
    for i in range(n ** 2):
        connection[i] = [False] * (n ** 2)
    for i in range(len(strMaze)):
        if strMaze[i] == '0':
            continue
        col = i // n
        row = i % n
        if row != 0:
            connection[i][i - 1] = True and strMaze[i - 1] != '0'
            if col != 0:
                connection[i][i - n - 1] = True  and strMaze[i - n - 1] != '0'
            if col != n - 1:
                connection[i][i + n - 1] = True and strMaze[i + n - 1] != '0'
        if row != n - 1:
            connection[i][i + 1] = True and strMaze[i + 1] != '0'
            if col != 0:
                connection[i][i - n + 1] = True and strMaze[i - n + 1] != '0'
            if col != n - 1:
                connection[i][i + n + 1] = True and strMaze[i + n + 1] != '0'
        if col != 0:
            connection[i][i - n] = True and strMaze[i - n] != '0'
        if col != n - 1:
            connection[i][i + n] = True and strMaze[i + n] != '0'
    return connection
def searchWord(i, counter, m, strMaze, connect, bD, result, unVist, curW):
    if strMaze[i] in bD:
        unVist[i] = False
        curW = curW + chr(i)
        if counter == m - 1:
            if 'exist' in bD[strMaze[i]]:
                result.append(curW)
            return
        for it in range(len(strMaze)):
            if connect[i][it] and unVist[it]: 
                searchWord(it, counter + 1, m, strMaze, connect, bD[strMaze[i]], result, unVist, curW)
                unVist[it] = True

def dropDown(strMaze, preRe, n):
    for i in preRe:
        strMaze[ord(i)] = '0'
    for j in range(n):
        for k in range(n):
            flag = False
            for i in range(n - 1, k - 1, - 1):
                if strMaze[j * n + i] == '0':
                    flag = True
                if strMaze[j * n + i] != '0' and flag:
                    strMaze[j * n + i], strMaze[j * n + i + 1] = strMaze[j * n + i + 1], strMaze[j * n + i]


def searchSolution(searchDeep, strMazeC, connectionC, bD, curSoluC, solution):
    for start in range(len(strMazeC)):
        if strMazeC[start] == '0':
            continue
        result = []
        unVistited = [True] * (n ** 2)
        searchWord(start, 0, lengths[searchDeep], strMazeC, connectionC, bD, result, unVistited, '')
        for nextWordInx in result:
            nextWord = ''
            curSolu = curSoluC
            for i in nextWordInx:
                nextWord = nextWord + strMazeC[ord(i)]
            curSolu = curSolu + ' ' + nextWord
            if searchDeep == len(lengths) - 1:
                solution.append(curSolu)
            else:
                strMaze = strMazeC[:]
                connection = [0] * len(strMaze)
                dropDown(strMaze, nextWordInx, n)
                connection = buildConnection(strMaze, n)
                searchSolution(searchDeep + 1, strMaze, connection, bD, curSolu, solution)

def insert_word(trie, word, index):
    if index == len(word)-1:
        trie.setdefault(word[index],{})['exist'] = True
    else:
        insert_word(trie.setdefault(word[index],{}), word, index+1)
    

    # change small list to trie
first_word_list = open(argv[1]).read().split()
second_word_list = open(argv[2]).read().split()
first_trie, second_trie = {}, {}
for word in first_word_list:
    insert_word(first_trie, word, 0)
for word in second_word_list:
    insert_word(second_trie, word, 0)
input_puzzle = ''
for line in stdin:
    if line == '\n':
        break
    find_star = Counter(line)
    if find_star['*'] <= 0:
        input_puzzle += line[:-1]      
        n = len(line[:-1])
    else:
        lengths = []
        solution = []
        input_puzzle = list(input_puzzle)
        for length in line.split():
            lengths.append(len(length))
        connection = buildConnection(input_puzzle, n)
        searchSolution(0, input_puzzle, connection, first_trie, '', solution)
        if len(solution) == 0:
            searchSolution(0, input_puzzle, connection, second_trie, '', solution)
        for i in range(len(solution)):
            solution[i] = solution[i][1:len(solution[i])]
        solution = list(set(solution))
        solution.sort()
        solution = '\n'.join(e for e in solution)
        #answer.write(solution)
        #answer.write('.')
        print(solution)
        print('.') 
        input_puzzle = ''

