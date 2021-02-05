#!/usr/bin/env python
# coding: utf-8
def read_data(prefix):
    output = []
    data_files = ['c', 'w', 'p', 's']
    for file in data_files:
        f = open(f'./datasets/{prefix}_{file}.txt', mode='r').read().strip()
        result = [int(num) for num in f.split('\n')]
        output.append(result)
    return output

def split_to_num(word):
    return [int(char) for char in word]

def join_to_str(arr):
    return ''.join(str(char) for char in arr)
