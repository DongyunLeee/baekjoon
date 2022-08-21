# 시간초과 문제로 input 대신 sys 라이브러리 사용
import sys

# 수의 개수 입력
N = int(input())

# 수의 개수만큼 숫자 입력
# 입력값을 하나하나 리스트에 등록할 경우, 메모리 에러 발생
result = [0] * 10001
for i in range(N):
    result[int(sys.stdin.readline())] += 1

# 오름차순 정렬 후, 출력
for num in range(1, 10001):
    if result[num] != 0:
        for i in range(result[num]):
            print(num)