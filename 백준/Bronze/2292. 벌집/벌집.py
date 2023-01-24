def cal_root_2nd(a, b, c):
    return (-b + (b**2 - 4 * a * c ) ** 0.5) / (2 * a)
print(int(-(-cal_root_2nd(3, -3, 1 - int(input()))//1)))