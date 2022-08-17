# input number
num = int(input()) - 1

# get result
cnt = 1
while num > 0:
    num -= 6 * cnt
    cnt += 1

# return result
print(cnt)