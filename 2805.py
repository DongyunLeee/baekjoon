from sys import stdin

# 이분탐색 활용
N, M = map(int, stdin.readline().split())
tree = list()
tree = list(map(int, stdin.readline().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for item in tree:
        if item > mid:
            cnt += (item - mid)

    if cnt < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)