from sys import stdin

# 이분탐색 활용
K, N = map(int, stdin.readline().split())
Lan = []

for item in range(K):
    Lan.append(int(stdin.readline()))

start = 1
end = max(Lan)
while True:
    mid = (start+end)//2
    cnt = 0
    for item in Lan:
        cnt += item//mid

    if cnt >= N:
        start = mid+1
    else:
        end = mid-1

    if start > end:
        print(end)
        break

