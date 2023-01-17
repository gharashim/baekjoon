def sum_numbers(num):
    num_ = str(num)
    for i in range(len(num_)):
        num += int(num_[i])
    return num

A = [i for i in range(10000)]
B = [sum_numbers(i) for i in range(10000)]

[print(sorted(set(A)-set(B))[i]) for i in range(len(sorted(set(A)-set(B))))]