list_of_checks = []


def length_check(some_password):
    if not 6 <= len(some_password) <= 10:
        list_of_checks.append("Password must be between 6 and 10 characters")


def letter_and_digit_check(some_password):
    if not some_password.isalnum():
        list_of_checks.append("Password must consist only of letters and digits")


def at_list_two_digits_check(some_password):
    digit_counter = 0
    for character in some_password:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_of_checks.append("Password must have at least 2 digits")

password = input()
password_is_not_valid = [length_check(password), letter_and_digit_check(password), at_list_two_digits_check(password)]

if len(list_of_checks) == 0:
    print("Password is valid")
print("\n".join(list_of_checks))