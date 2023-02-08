import sys

# 배열의 크기(N), 배열의 원소, 교환 가능 횟수(S) 입력
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())

# 가장 큰 수가 앞으로 올수록 사전 순서가 빨라진다.

# 배열의 수-1 만큼 반복하며 원소 교환을 진행한다.
for i in range(N-1):
    # 교환 가능 횟수가 0이되는 경우, 탈출
    if S == 0:
        break

    # 반복문을 돌며, 현재 위치(i)에 올 수 있는 가장 큰 원소를 탐색한다.
    mx, idx = arr[i], i
    for j in range(i+1, min(N, i+1+S)):
        if mx <= arr[j]:
            mx = arr[j]
            idx = j

    # 가장 큰 원소를 가져오기 위해 필요한 교환 횟수를 차감한다.
    S -= idx-i

    # 탐색된 가장 큰 원소를 현재 위치(i)로 이동하고 나머지 원소를 한칸씩 뒤로 미룬다.
    arr.pop(idx)
    arr.insert(i, mx)

result = ' '.join(map(str, arr))
print(result)