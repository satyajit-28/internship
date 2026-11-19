# Count 1

def count_vowels(str:str) -> int:
    count = 0
    for char in str.lower():
        if char in "aeiou":
            count += 1
    return f"Toal vowels in string are {count}"


print(count_vowels('AEIOU'))
print(count_vowels("aniket"))


"""
Time complexity
"""
""