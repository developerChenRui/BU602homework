# Copyright 2017 xue hen da

"Assignment10"

from collections import defaultdict
from sys import argv
import numpy as np


def route_finder(steps, size, grid, xcoord, ycoord, length, wdls, route, astkline, order):
    "Find possible routes"
    for i in range(-1, 2):
        for j in range(-1, 2):
            xaxis, yaxis = xcoord + i, ycoord + j
            if xaxis < 0 or xaxis >= size or yaxis < 0 or yaxis >= size:
                continue
            char = astkline[order][length - steps]
            if char != '*':
                if grid[xaxis][yaxis] != char:
                    continue
            if grid[xaxis][yaxis] == '':
                continue
            if (xaxis, yaxis) in route:
                continue
            route.append((xaxis, yaxis))
            temp = ''.join(grid[x][y] for (x, y) in route)
            key = temp[:2]
            if key not in wdls[length]:
                route.pop()
                continue
            else:
                for word in wdls[length][key]:
                    if temp in word:     # !!!!!!!!!!!!
                        break
                else:
                    route.pop()
                    continue
            if steps > 1:
                route = yield from route_finder(steps - 1, size, grid, xaxis, yaxis, length, wdls, route, astkline, order)
            if len(route) == length:
                yield route
            route.pop()
    return route


def answer_finder(grid, size, lenlist, nums, astkline, wdls, result=[]):
    "find answer"
    firstlen = lenlist[0]
    lenlist = lenlist[1:]   # throw the first word
    for xcoord in range(size):   # start from each char
        for ycoord in range(size):
            if grid[xcoord][ycoord] == '':
                continue
            else:
                remaindiv = len(lenlist)
                order = nums - remaindiv - 1   # ????? 
                char = astkline[order][0]
                if char != '*':
                    if grid[xcoord][ycoord] != char:
                        continue
                for route in route_finder(firstlen-1, size, grid, xcoord, ycoord, firstlen, wdls, [(xcoord, ycoord)], astkline, order):
                    word = ''.join(grid[i][j] for i, j in route)
                    result.append(word)
                    if remaindiv > 0:
                        temp = grid.copy()
                        for i, j in route:
                            temp[i][j] = ''
                        new_grid = drop_down(temp)
                        result = yield from answer_finder(new_grid, size, lenlist, nums, astkline, wdls, result)
                    if len(result) == nums:  # get desired # of results
                        yield result   # return
                    result.pop()
    return result


def drop_down(grid):
    "Drop Down the grid, '' for used char"
    drop = np.copy(grid)
    size = len(grid)
    for i in range(size):
        for j in range(size-1, -1, -1):
            if drop[:, i][j] == '':
                for abvch in range(j-1, -1, -1):
                    if drop[:, i][abvch] != '':
                        drop[:, i][j], drop[:, i][abvch] = drop[:, i][abvch], drop[:, i][j]
                        break
    return drop


def main():
    "Read Dict and Input"
    smldict = defaultdict(lambda: defaultdict(list))
    bigdict = defaultdict(lambda: defaultdict(list))

    for filename, dictname in zip([argv[1], argv[2]], [smldict, bigdict]):
        with open(filename) as dic:
            for word in dic:
                word = word.rstrip()
                dictname[len(word)][word[:2]].append(word)

    while 1:
        output = []
        try:
            line = input()
        except EOFError:
            exit()
        size = len(line)
        grid = np.empty([size, size], dtype=str)
        for i in range(size):
            grid[0][i] = line[i]
        for i in range(1, size):
            line = input()
            for j in range(size):
                grid[i][j] = line[j]
        lenlist = []
        astkline = input().split()
        lenlist.extend(len(div) for div in astkline)

        for wdls in [smldict, bigdict]:
            for answer in answer_finder(grid, size, lenlist, len(lenlist), astkline, wdls):
                res = ' '.join(wd for wd in answer)
                if res not in output:
                    output.append(res)
            if output:
                break
        print('\n'.join(ln for ln in sorted(output)))
        print('.')

main()
