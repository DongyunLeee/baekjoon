from sys import stdin

M, N = map(int, stdin.readline().split())

# 에라토스테네스의 체
# 목표 수보다 큰 제곱근까지의 소수로 나누어지지 않는 수 = 소수
ret = [True] * (N+1)

ret[1] = False
for item in range(2, int(N**(1/2)) + 1):
    if ret[item] == True:
        for i in range(item + item, (N+1), item):
            ret[i] = False

result = ""
for i in range(M, (N+1)):
    if ret[i] == True:
        result += f"{i}\n"

print(result)