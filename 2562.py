max_num = 0
cnt = 0

for i in range(1, 10):

    num = int(input())

    if max_num < num:
        max_num = num
        cnt = i

print(max_num)
print(cnt)