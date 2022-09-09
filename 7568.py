from sys import stdin

# 학생 수 입력
N = int(stdin.readline())
students = []

# 학생의 몸무게 및 키를 입력 후, 리스트에 저장
for item in range(N):
    w, h = map(int, stdin.readline().split())
    students.append((w, h))

# 학생별로 덩치를 비교하여 등수 출력
# 브루트 포스(완전탐색) 알고리즘 사용
for student in students:
    rank = 1
    for other in students:
        if student[0] < other[0] and student[1] < other[1]:
            rank += 1
    print(rank, end=' ')