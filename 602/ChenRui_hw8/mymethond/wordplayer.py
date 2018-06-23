# Copyright 2017 ChenRui ruirui@bu.edu
# dictionary
from collections import defaultdict
import copy
from sys import argv


class Node(object):
    def __init__(self, id_):
        self.id = id_
        self.children = []
        self.deep = 0
        self.judge = []

    def __repr__(self):
        return "Node: [%s]" % self.id

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def get_id(self):
        return self.id

    def equals(self, node):
        return node.id == self.id

    def set_deep(self, deep):
        self.deep = deep

    def get_deep(self):
        return self.deep

    def get_word(self):
        return self.judge

    def set_word(self, word):
        self.judge = word


def process_file(filename):
    dic_list = defaultdict(list)
    file = open(filename)
    for line in file:
        line = line[:-1]
        num = len(line)
        dic_list[num].append(line)
    return dic_list


def traversal_and_cut(words_trie, word):
    stack = [words_trie]
    ans = []
    word_copy = list(word)
    nodes = ""
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        if cur_node.get_deep() == 1:
            nodes = cur_node.get_id()
        elif cur_node.get_deep() != 0:
            nodes = nodes[0:cur_node.get_deep()-1] + cur_node.get_id()
        if cur_node.get_id() == "root":
            for child in cur_node.get_children():
                word_copy = list(word)
                if child.get_id() in word_copy:
                    stack.insert(0, child)
                    node_id = child.get_id()
                    word_copy.remove(node_id)
                    child.set_word(word_copy)
        else:
            if cur_node.get_children() == []:
                ans.append(nodes)
            else:
                for child in cur_node.get_children():
                    temp = copy.deepcopy(cur_node.get_word())
                    if child.get_id() in temp:
                        stack.insert(0, child)
                        node_id = child.get_id()
                        temp.remove(node_id)
                        child.set_word(temp)
    return ans


def list_to_tree(processed_file, length):
    root = Node("root")
    words = processed_file[length]
    for word in words:
        cur_parent = root
        for index, letter in enumerate(word):
            flag = 1
            for child in cur_parent.get_children():
                if child.get_id() == letter:
                    cur_parent = child
                    flag = 0
            if flag:
                cur_node = Node(letter)
                cur_node.set_deep(index+1)
                cur_parent.add_child(cur_node)
                cur_parent = cur_node
    return root


def print_ans(processed_file, word, word_len):
    ans_list = traversal_and_cut(processed_file[word_len], word)
    list.sort(ans_list)
    for item in ans_list:
        print(item)
    print('.')


def main(argv):
    processed_file = process_file(argv[1])
    flag = 1
    transferred_list = []
    while flag:
        info = input()
        info = info.split(' ')
        if int(info[-1]) == 0:
            flag = 0
        else:
            word = info[0]
            required_len = info[1]
            if int(required_len) not in transferred_list:
                transferred_list.append(int(required_len))
                root = list_to_tree(processed_file, int(required_len))
                processed_file[int(required_len)] = root
                print_ans(processed_file, word, int(required_len))

            else:
                print_ans(processed_file, word, int(required_len))

if __name__ == '__main__':
    main(argv)
