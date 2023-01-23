N = int(input())
sentences = [input() for _ in range(N)]

for sentence in sentences:
    if len(sentence) > 2:
        for i in range(len(sentence)-2):
            if (sentence[i+2] != sentence[i+1]) & (sentence[i+2] in sentence[0:i+1]):
                N -=1
                break
print(N)