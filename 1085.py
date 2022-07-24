# 입력 받아 변수 저장
x, y, w, h = map(int, input().split(' '))

# 직사각형 경계선 까지의 최솟값 계산
result = min(x, y, w-x, h-y)

# 출력
print(result)