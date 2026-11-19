# Count 1

def remove_duplicate(str:str) -> str:
    seen = set()
    out = []

    for char in str:
        if char not in seen:
            seen.add(char)
            out.append(char)
    return "".join(out)


print(remove_duplicate("programming"))

