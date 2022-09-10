from sys import stdin

# 좌표의 수 입력
N = int(stdin.readline())

# 좌표 입력
coordinates = []
for item in range(N):
    x, y = map(int, stdin.readline().split())
    coordinates.append((y, x))

# 좌표 정렬 및 출력
for coord in sorted(coordinates):
    print(coord[1], coord[0])
