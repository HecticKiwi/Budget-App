# Budget-App
This app contains a `Category` class that instantiates objects according to different budget categories like *food*, *clothing*, and *entertainment*. It will track transactions made in a ledger.
When objects are created, they are passed in the name of the category.

## Methods
Method|Description
-|-
deposit(self, amount, description)|Accepts an amount and description. If no description is given, defaults to an empty string. Records the deposit in the object's ledger
withdraw(self, amount, description)|Similar to the deposit method. If there are not enough funds, nothing wil be recorded on the object's ledger. Will return True if the withdrawal took place, False otherwise
get_balance(self)|Returns the current balance of the budget category based on the deposits and withdrawals that have occurred
transfer(self, amount, category)|Accepts an amount and another budget category as arguments. Adds a withdrawal to the object's ledger and adds a deposit to the given category's ledger. If there are not enough funds, nothing wil be recorded. Will return True if the transactions took place, False otherwise
check_funds(self, amount)|Returns True if the balance of the budget category is greater than the given amount, False otherwise

Printing a budget object will display its recorded transactions as shown in this example output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Outside the `Category` class, a `create_spend_chart` function will take a list of category objects and return a bar chart as shown in this example output:
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
