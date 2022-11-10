from sys import stdin


def dfs(n):
    global result
    visited[n] = True # n의 방문기록 업데이트
    next_n = numbers[n] # next_n = n의 두번째줄 정수
    path.append(n) # n을 path에 추가

    # n과 next_n이 같은 경우, n을 결과에 추가하고 탐색 종료
    if n == next_n:
        result.append(n)
        return

    # next_n의 방문 기록을 먼저 확인하고 방문 기록이 존재하는 경우,
    # next_n이 이미 경로에 존재하는 경우, next_n ~ n까지 저장된 경로를 결과에 추가
    # next_n의 path 존재 여부와 상관없이 탐색 종료
    if visited[next_n]:
        if next_n in path:
            result += path[path.index(next_n):]
        return

    dfs(next_n)


num = int(stdin.readline())
numbers = [-1]
visited = [False] * (num+1)
result = []

for _ in range(num):
    numbers.append(int(stdin.readline()))

for item in range(1, num+1):
    # 방문기록이 존재하는 경우, 탐색을 진행하지 않음
    if visited[item] is True:
        continue
    else:
        path = []
        dfs(item)

# 조건을 만족하는 정수의 개수와 포함되는 정수를 오름차순으로 출력
print(len(result))
for i in sorted(result):
    print(i)