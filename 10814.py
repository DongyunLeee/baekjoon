# 나이순 정렬
import sys

# 회원수 입력
N = int(sys.stdin.readline())

# 회원 리스트 생성
L = []
for i in range(201):
    L.append([])

# 회원 정보 입력
for i in range(N):
    num, K = sys.stdin.readline().split()
    L[int(num)].append(K)

# 회원 정렬 및 출력
for num, i in enumerate(L):
    for j in i:
        print(f"{num} {j}")