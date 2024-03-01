def cal_square(num):
    return num**2


arr = [1, 2, 3, 4]

result = map(cal_square, arr)

print(result)

for i in result:
    print(i)
