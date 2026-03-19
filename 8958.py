N = int(input())

for _ in range(N):

    arr = input()
    cnt = 0
    total = 0

    for i in arr:
        if i == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0

    print(total)