# Count 1
def check_prime(num):
    if num <= 1:
        print("Not prime")
        return
    
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("prime")