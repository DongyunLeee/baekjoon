T = int(input())

for case in range(T):
    result = ''
    R, S = input().split(' ')
    for n in S:
        result += (n * int(R))

    print(result)