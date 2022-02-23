class InsufficientFundsException(Exception):
    def __init__(self, arg):
        self.msg = arg

my_amount = int(input("Enter the money for the withdrawal: "))
my_balance = 10000
if my_amount >= my_balance:
    raise InsufficientFundsException("You cannot withdraw money more than your available balance")
else:
    print(f"You can withdraw Rs {my_amount}")
    my_finalamount = my_balance - my_amount
    print("The total money left in your account is ", my_finalamount)
