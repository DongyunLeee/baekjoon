from sys import stdin

N = int(stdin.readline())

new_list = []
for num in range(N):
    order = stdin.readline().split()
    if order[0] == "push":
        new_list.append(order[1])
    elif order[0] == "pop":
        if len(new_list) == 0:
            print(-1)
        else:
            print(new_list.pop(0))
    elif order[0] == "size":
        print(len(new_list))
    elif order[0] == "empty":
        if len(new_list) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(new_list) == 0:
            print(-1)
        else:
            print(new_list[0])

    else:
        if len(new_list) == 0:
            print(-1)
        else:
            print(new_list[-1])
