'''
Practical challenge — Inventory system
Scenario: A shop needs to track products and prevent selling more stock than it has.
name, price, and stock attributes.
restock(quantity) — accepts only positive whole numbers.
sell(quantity) — rejects invalid quantities or insufficient stock; otherwise reduces stock and returns the sale amount.
display_details() — displays the current stock.
Then create two products and process multiple sales using a loop.
'''
class Product:
    def __init__(self, p_name, p_price, p_stock):
        print(self.__dict__)
        self.p_name = p_name
        self.p_price = p_price
        self.p_stock = p_stock
        print(self.__dict__)



    def restock(self, quantity):
        if type(quantity) is not int or quantity <= 0:
            return "Invalid Quantity"
        self.p_stock += quantity

        
    def sell(self, quantity):
        if type(quantity) is not int or quantity <= 0:
            print("Invalid Quantity")
            #return 0

laptop = Product("Laptop", 55000, 5)
mouse = Product("Mouse", 500, 20)
#command
