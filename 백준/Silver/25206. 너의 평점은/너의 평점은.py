class_point = 0
score = 0
for _ in range(20):
    input_ = list(input().split())
    if input_[2] != 'P':
        class_point += float(input_[1])
        if input_[2] == 'A+':
            score += 4.5 * float(input_[1])
        elif input_[2] == 'A0':
            score += 4.0 * float(input_[1])
        elif input_[2] == 'B+':
            score += 3.5 * float(input_[1])
        elif input_[2] == 'B0':
            score += 3.0 * float(input_[1])
        elif input_[2] == 'C+':
            score += 2.5 * float(input_[1])
        elif input_[2] == 'C0':
            score += 2.0 * float(input_[1])
        elif input_[2] == 'D+':
            score += 1.5 * float(input_[1])
        elif input_[2] == 'D0':
            score += 1.0 * float(input_[1])
        elif input_[2] == 'F':
            score += 0 * float(input_[1])
print(score / class_point)