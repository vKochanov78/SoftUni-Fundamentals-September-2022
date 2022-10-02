lst = []

for _ in range(3):
    current_str = input()
    lst.append(current_str)

lst[0], lst[2] = lst[2], lst[0]
print(lst)