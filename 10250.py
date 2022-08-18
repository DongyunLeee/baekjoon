# get testcase
T = int(input())
result = []

# get High, Width, Num
for i in range(T):
    H, W, N = map(int, input().split())
    if (N%H) != 0:
        ret = (N%H*100) + (N//H) + 1
    else:
        ret = H * 100 + (N//H)
    result.append(ret)

# return result
for i in result:
    print(i)
