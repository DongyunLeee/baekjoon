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
    # 하나의 숫자로 구성할 수 있는 최솟값
    min_1 = min(arr)
    min_idx = arr.index(min_1)
    idx = len(arr) - min_idx - 1

    del arr[max(min_idx, idx)]
    del arr[min(min_idx, idx)]

    # 두 개의 숫자로 구성할 수 있는 최솟값(min_1 + 연관된 가장 작은 숫자)
    min_2 = min_1 + min(arr)
    min_idx = arr.index(min(arr))
    idx = len(arr) - min_idx - 1

    del arr[max(min_idx, idx)]
    del arr[min(min_idx, idx)]

    # 세 개의 숫자로 구성할 수 있는 최솟값(min_2 + 연관된 가장 작은 숫자)
    min_3 = min_2 + min(arr)

    result = (min_3 * 4) + (min_2 * (((N-2) * 8) + 4)) + (min_1 * (((N-2) * (N-2) * 5) + ((N-2) * 4)))

print(result)