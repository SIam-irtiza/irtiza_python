def palindrome(word):

    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


text = input("Enter a word: ")

palindrome(text)