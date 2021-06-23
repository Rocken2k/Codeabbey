# Challenge: https://www.codeabbey.com/index/task_view/sum-in-loop
# Author: Rocken2k

def sum_in_loops():
    inputs = input().split()
    result = 0
    for x in inputs:
        result += int(x)
    print(result)

sum_in_loops()
