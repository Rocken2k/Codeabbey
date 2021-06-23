# Challenge: https://www.codeabbey.com/index/task_view/min-of-two
# Author: Rocken2k

import sys

def read_data():
    return sys.stdin.readlines()

def mini(line):
    x, y = line.split()
    result = min(int(x), int(y))
    print(result)

def main():
    data = read_data()
    list(map(mini, data))

main()
