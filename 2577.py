a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)

num_lst = [0]*10

for i in num:
    num_lst[int(i)] += 1

for j in num_lst:
    print(j)

# =======================

# '1' = 0
# '2' = 0
# '3' = 0
# '4' = 0
# '5' = 0
# '6' = 0
# '7' = 0
# '8' = 0
# '9' = 0

# for i in num:
#     if i == 1:
#         '1' += 1
#     elif i == 2:
#         '2' += 1
#     elif i == 3:
#         '3' += 1
#     elif i == 4:
#         '4' += 1
#     elif i == 5:
#         '5' += 1
#     elif i == 6:
#         '6' += 1
#     elif i == 7:
#         '7' += 1
#     elif i == 8:
#         '8' += 1
#     elif i == 9:
#         '9' += 1

# print('1')
# print('2')
# print('3')
# print('4')
# print('5')
# print('6')
# print('7')
# print('8')
# print('9')
