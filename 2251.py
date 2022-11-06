# BFS 알고리즘을 이용하여 풀이를 진행함.
from collections import deque


def pour(a, b):
    if not visited[a][b]:
        visited[a][b] = True
        q.append((a,b))


def bfs():
    while q:
        a, b = q.popleft()
        c = C - (a + b)

        # A물통이 비어있는 경우, C물통에 남은 물의 양을 저장함
        if a == 0:
            ret.append(c)

        # A -> B
        water = min(a, B - b)
        pour(a - water, b + water)
        # A -> C
        water = min(a, C - c)
        pour(a - water, b)
        # B -> A
        water = min(b, A - a)
        pour(a + water, b - water)
        # B -> C
        water = min(b, C - c)
        pour(a, b - water)
        # C -> A
        water = min(c, A - a)
        pour(a + water, b)
        # C -> B
        water = min(c, B - b)
        pour(a, b + water)


A, B, C = map(int, input().split())

ret = list()    # 결과저장 리스트
visited = [[False] * (B+1) for _ in range(A+1)]    # 방문여부 저장 리스트
visited[0][0] = True # 초기 (a, b)값 방문ㅊ처리
q = deque()    # 경우의 수 저장 큐
q.append((0, 0))    # 초기 (a, b)값 입력

bfs()
ret.sort()
for item in ret:
    print(item, end=" ")