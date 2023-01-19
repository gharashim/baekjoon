input_ = input().upper()
char = sorted(set(input_))
num = [0]*len(char)
num_dict = dict(zip(char,num))

for k, v in num_dict.items():
    for j in range(len(input_)):
        if k == input_[j]: v+=1
    num_dict[k] = v

try:
    num_dict = sorted(num_dict.items(), key = lambda x : x[1], reverse = True)[:2]
    if num_dict[0][1] == num_dict[1][1]:
        print('?')
    else: print(num_dict[0][0])
except IndexError:
    print(char[0])