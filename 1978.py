# 수의 개수와 수 입력
N = int(input())
L = input().split()

# 소수 찾기
# 3이상의 수는 1씩증가하며 나눈 나머지가 0인 경우, 소수가 아닌것으로 판단
for i in L:
    if int(i) == 1:
        N -= 1
        continue
    if int(i) == 2:
        continue
    for j in range(2, int(i)):
        if int(i)%j == 0:
            N -= 1
            break

# 소수의 개수 출력
print(N)
