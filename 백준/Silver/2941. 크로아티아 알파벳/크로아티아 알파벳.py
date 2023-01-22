S = input()
cro_char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = len(S)
for i in cro_char:
    if i in S:
        S = S.replace(i, '0')  
print(len(S))