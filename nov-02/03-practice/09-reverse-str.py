# Count 1
def reverse_str(str:str) -> str:
    rev = ''
    for char in str:
        rev = char + rev
    
    return rev.lower()


print(reverse_str("Satyajit"))
