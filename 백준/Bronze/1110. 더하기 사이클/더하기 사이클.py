input_ = input()
if len(input_) < 2: input_ = '0' + input_

ab = input_
iter = 0

while(1):
    b_ = str(int(ab[0])+int(ab[-1]))[-1]
    a_ = ab[-1]
    ab = a_ + b_
    iter += 1
    if (ab == input_): break
print(iter)