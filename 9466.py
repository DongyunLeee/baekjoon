import sys
sys.setrecursionlimit(200000) # 재귀의 깊이를 확장시킴 -> 미선언 할 경우, 런타임에러 발생


def dfs(num):
    global ret
    visited[num] = True # 방문 노드 체크
    team.append(num) # 팀원 구성을 위한 리스트에 추가
    next_num = students[num]

    # 다음 순번이 방문노드인 경우, 해당 순번이 현재 팀에 포함되는지 검사 후
    # 포함되는 경우, 해당 순번부터 팀원으로 구성
    if visited[next_num]:
        if next_num in team:
            ret += team[team.index(next_num):]
        return

    dfs(next_num)


result = list()
N = int(sys.stdin.readline())
for _ in range(N):
    number = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    students.insert(0, 0)
    ret = list()

    # 방문 확인을 위한 리스트는 False로 선언함
    visited = [False] * (number + 1)
    for item in range(1, number + 1):
        if not visited[item]:
            team = list()
            dfs(item)
    # 결과는 리스트에 저장 후, 마지막에 출력
    result.append(number - len(ret))
for i in result:
    print(i)
