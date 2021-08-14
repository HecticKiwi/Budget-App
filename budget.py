class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        header = [self.category.center(30, '*')]

        strings = []
        for transaction in self.ledger:
            description = transaction["description"] if len(transaction["description"]) <= 23 else transaction["description"][:23]
            amount = f"{transaction['amount']:.2f}"

            strings.append(description.ljust(23) + amount.rjust(7))

        total = []

        return '\n'.join(header + strings)

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

food.deposit(900, "asdf")
food.deposit(400, "fff")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(str(food))
print(f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33")
