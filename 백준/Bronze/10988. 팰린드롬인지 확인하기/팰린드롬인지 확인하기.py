char_ = input()
if char_ == ''.join([char_[i] for i in range(-1,-len(char_)-1,-1)]):
    print(1)
else:
    print(0)
