def palindrome_checker(num):

    for palindrome in range(len(numbers)):
        current_number = num[palindrome][::-1]
        if current_number == num[palindrome]:
            print(True)
        else:
            print(False)


numbers = input().split(", ")
palindrome_checker(numbers)