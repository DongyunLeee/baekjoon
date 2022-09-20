from sys import stdin

N = int(stdin.readline())
seq = list()
stack = list()
item = list()
ret = ""

for i in range(N):
    seq.append(int(stdin.readline()))
    stack.append(N-i)

while len(seq) > 0:
    if len(item) == 0:
        item.append(stack.pop())
        ret += "+\n"

    if len(stack) == 0 and item[-1] != seq[0]:
        ret = "NO"
        break

    if item[-1] == seq[0]:
        item.pop()
        seq.pop(0)
        ret += "-\n"
    else:
        item.append(stack.pop())
        ret += "+\n"

print(ret)