def is_prime(num):
    if num <= 1:
        return "Not prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not prime"
    return "Prime"



print(is_prime(2))
print(is_prime(4))
print(is_prime(17))