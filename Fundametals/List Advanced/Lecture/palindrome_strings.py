def palindrome_check(word):
    if word == word[::-1]:
        return word


text = input().split(" ")
searched_word = input()

all_palindromes = [word for word in text if palindrome_check(word)]
print(all_palindromes)

palindrome_counter = all_palindromes.count(searched_word)
print(f"Found palindrome {palindrome_counter} times")