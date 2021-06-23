# Challenge: https://www.codeabbey.com/index/task_view/sums-in-loop
# Author: Rocken2k

import sys

def read_data():
    return sys.stdin.readlines()
        
def split(line):
    x, y = line.split()
    suma = int(x) + int(y)
    print(suma)

def main():
    data = read_data()
    list(map(split, data))

main()
