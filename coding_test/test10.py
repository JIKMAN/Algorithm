# n = int(input())
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * i)

num_list = []
for i in range(9):
    num_list.append(int(input()))
print(max(num_list))
print(num_list.index(max(num_list)))