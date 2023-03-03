def divisor(X):
    result = []
    for iter_ in range(1, X + 1):
        if iter_ > X // iter_: break
        if X % iter_ == 0:
            result.append(iter_)
            result.append(X // iter_)
    return sorted(result)

num_ = []
while(1):
    num_.append(int(input()))
    if num_[-1] == -1: break

for i in range(len(num_)-1):
    divisors = divisor(num_[i])
    divisors_type_str = [str(divisors[i]) for i in range(len(divisors))]
    if sum(divisors[0:-1]) == divisors[-1]:
        print('{} ='.format(divisors_type_str[-1]), ' + '.join(divisors_type_str[0:-1]))
    else: print('{} is NOT perfect.'.format(divisors[-1]))