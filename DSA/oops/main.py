class Item:
    def __init__(self,name : str,price : int,quantity : int):
        # Run validation
        assert type(price)==int and price >= 0, "Price must be float and greater than or equal to zero"
        assert type(quantity)==int and quantity >= 0, "Quantity must be integer and greater than or equal to zero"

        # Assigning to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def calculate_total_price(self):
        return self.price*self.quantity


item  = Item("laptop", 10000, 5)

print(item.calculate_total_price())

