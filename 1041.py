import sys

# 본 문제는 N이 1인 경우를 제외하고, 정해진 공식으로 문제 풀이가 가능했다.(result 부분 참조)

# 주사위의 크기(N), 주사위의 구성 숫자(arr) 입력
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 주사위의 크기가 1일 경우, 주사위의 가장 큰 숫자를 제외한 모든 숫자를 더함
if N == 1:
    result = sum(arr) - max(arr)

# 주사위의 크기가 2이상인 경우, 한 주사위당 3개의 숫자까지 사용된다.
# 최대 3개까지의 가장 작은 숫자 구성을 탐색한다.
else:

    # 각 마주보는 주사위의 숫자 중, 작은 숫자를 저장하여 오름차순 정렬
    min_list = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])]
    min_list.sort()

    # 표현되는 주사위 면의 개수에 따른 최솟 값을 계산
    min_1 = min_list[0]
    min_2 = sum(min_list[0:2])
    min_3 = sum(min_list)

    # 입력값 N에 필요한 최솟 값을 표현되는 면의 수에 따라 계산
    result_1 = min_1 * (((N-2) * (N-2) * 5) + ((N-2) * 4))
    result_2 = min_2 * (((N-2) * 8) + 4)
    result_3 = min_3 * 4

    result = result_1 + result_2 + result_3

print(result)
