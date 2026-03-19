A, B = input().split()

a_lst = []
a_num = 0

b_lst = []
b_num = 0

for a in A:
    a_lst.append(a)
for b in B:
    b_lst.append(b)

a_lst = a_lst[::-1]
a_num= ''.join(a_lst)

b_lst = b_lst[::-1]
b_num= ''.join(b_lst)

print(max(a_num, b_num))
