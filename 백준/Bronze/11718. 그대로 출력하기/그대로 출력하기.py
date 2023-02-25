char = []
while True:
    try:
        char.append(input())
    except EOFError:
        break
[print(char[i]) for i in range(len(char))]