# Count 1

def is_palindrome(str:str) -> bool:
    rev = ''
    for char in str:
        rev = char + rev
    return "Palindrome" if str == rev else "Not Palindrome"


print(is_palindrome("madam"))
print(is_palindrome("hello"))