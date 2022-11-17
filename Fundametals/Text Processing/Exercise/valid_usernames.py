def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def symbols_are_valid(username):
    for symbol in username:
        if not (symbol.isalnum() or symbol == "-" or symbol == "_"):
            return False
    return True


def redundant_symbols(username):
    if ' ' in username:
        return False
    return True


def username_validation(username):
    if length_is_valid(username) and symbols_are_valid(username) and redundant_symbols(username):
        print(username)


names = input().split(", ")
for name in names:
    if username_validation(name):
        print(name)