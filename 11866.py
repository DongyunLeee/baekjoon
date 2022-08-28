# 인원(N), 순번(K) 입력
N, K = map(int, input().split())

# 기본 순열 리스트 새성
L = []
for i in range(N):
    L.append(i+1)

# 요르푸스 순열 도출
S = 0
Ret = []
for i in range(N):
    S += (K-1)
    if S >= N:
        S %= N
    Ret.append(L.pop(S))
    N -= 1

# 결과출력
print("<", end="")
for i in Ret:
    if i != Ret[N-1]:
        print(i, end=", ")
    else:
        print(i, end="")
print(">", end="")