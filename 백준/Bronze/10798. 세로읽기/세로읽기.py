char_ = [input() for _ in range(5)]
output = []
for j in range(max([len(x) for x in char_])):
    for i in range(len(char_)):
        try: output.append(char_[i][j])
        except: continue
print(''.join(output))