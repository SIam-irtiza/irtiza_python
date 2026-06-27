starts_with = lambda string, sub: string.startswith(sub)
text = input("Enter a string: ")
sub = input("Enter a sub-string: ")

if starts_with(text, sub):
    print("The string starts with the given sub-string")
else:
    print("The string does not start with the given sub-string")