from sys import stdin

# 카드수량 입력
N = int(stdin.readline())

# 카드리스트 생성
card = []
for i in range(N):
    card.append(i+1)

# 마지막 카드를 구하는 로직
while len(card) > 1:
    num = len(card)
    card = card[1::2]

    if num % 2 != 0:
        card.append(card.pop(0))

print(card[0])