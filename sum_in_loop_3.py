def sum_in_loop_3():
    inputs = input().split()
    num_list = []
    for i in inputs:
        num_list.append(int(i))
    print(sum(num_list))
sum_in_loop_3()