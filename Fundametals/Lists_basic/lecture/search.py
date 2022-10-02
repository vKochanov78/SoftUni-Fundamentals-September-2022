number_of_lines = int(input())
word = input()
first_lst = []
filtered_lst = []

for i in range(number_of_lines):
    current_str = input()
    first_lst.append(current_str)
    if word in current_str:
        filtered_lst.append(current_str)

print(first_lst)
print(filtered_lst)