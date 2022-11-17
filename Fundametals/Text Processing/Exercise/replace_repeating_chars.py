some_string = input()
replaced_text = ""
last_letter = ""

for current_letter in some_string:
    if current_letter != last_letter:
        replaced_text += current_letter
        last_letter = current_letter

print(replaced_text)