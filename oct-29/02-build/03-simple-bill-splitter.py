'''
@Author:    satyajit 

@Goal:      To implement a simple bill splitter

@Date:      29th Oct 2026

'''

def bill_splitter():
    print("-" * 50)
    print("Your Bill Splitter Is Here!")
    print("-" * 50)


bill_splitter()


total_amount = float(input("Enter your total bill amount: "))
people = int(input("Enter total number of peoples invloved in the bill: "))


def splitter(total_amount, people):
    if people < 0:
        return "Number of peoples should be > 0"
    else:
        return f"Each person should pay Rs: {total_amount / people}"


print(splitter(total_amount, people))