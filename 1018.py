# 체스판 사이즈 입력
N, M = map(int, input().split())
L = []
Default = 8
Cnt = float('inf')

# 체스판 입력
for i in range(N):
    L.append(input())

# 체스판 계산
for i in range(N-(Default-1)):
    for j in range(M-(Default-1)):
        Cnt_B = 0
        Cnt_W = 0
        for x in range(i, i+Default):
            for y in range(j, j+Default):
                if (x+y)%2 == 0:
                    if L[x][y] == 'B': Cnt_W += 1
                    else: Cnt_B += 1
                else:
                    if L[x][y] == 'B': Cnt_B += 1
                    else: Cnt_W += 1
        Cnt = min(Cnt, Cnt_B, Cnt_W)

# 최솟값 출력
print(Cnt)