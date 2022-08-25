# 좌표 정렬
import sys

# 좌표수 입력
N = int(sys.stdin.readline())

# 좌표 리스트 생성
L = []
for i in range(200001):
    L.append([])

# 좌표 정보 입력
for i in range(N):
    num, K = sys.stdin.readline().split()
    L[int(num)+100000].append(int(K))

# 좌표 정렬 및 출력
for num, i in enumerate(L):
    for j in sorted(i):
        print(f"{num-100000} {j}")