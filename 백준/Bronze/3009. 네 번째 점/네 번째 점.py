num_ = [list(map(int, input().split())) for _ in range(3)]
x = [num_[i][0] for i in range(3)]
y = [num_[i][1] for i in range(3)]

def get_min(x):
    return {
        k : v for k, v in zip([x.count(sorted(set(x))[i]) for i in range(2)], sorted(set(x)))
    }[1]

print(get_min(x), get_min(y))