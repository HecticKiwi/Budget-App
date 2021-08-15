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

        total = [f"Total: {self.get_balance()}"]

        return '\n'.join(header + strings + total)

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
    sums = {}

    for category in categories:
        spent = -sum([transaction["amount"] for transaction in category.ledger if transaction["amount"] < 0])
        sums[category.category] = spent
    
    total = sum(sums.values())

    for category in sums.keys():
        sums[category] = sums[category] / total * 100

    print(sums)

    header = ["Percentage spent by category"]

    percentage = 100
    rows = []

    while percentage >= 0:
        row = f"{percentage}|".rjust(4)

        for category in categories:
            row += " o" if sums[category.category] >= percentage else "  "

        rows.append(row)
        percentage -= 10

    bar = ["    " + '-' * (len(categories) * 2 + 2)]

    print('\n'.join(header + rows + bar))

    rows = []
    i = 0
    while i < 4:
        row = [' ' + category.category[i] if 0 <= i <= len(category.category) else "  " for category in categories]
        i += 1
        if row == '      ':
            break
        print(row)

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "asdf")
food.deposit(400, "fff")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
entertainment.deposit(2000, "ferew")
create_spend_chart([food, entertainment])
