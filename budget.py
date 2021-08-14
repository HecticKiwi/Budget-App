class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})

        return self.check_funds(amount)

    def get_balance(self):
        return sum([transaction["amount"] for transaction in self.ledger])

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"Transfer to {category.category}"})
            category.deposit(amount, f"Transfer from {self.category}")
        
        return self.check_funds(amount)

    def check_funds(self, amount):
        return amount <= self.get_balance()

def create_spend_chart(categories):
    pass

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900)
food.deposit(400)
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(food.transfer(20, entertainment))
print(entertainment.ledger)
