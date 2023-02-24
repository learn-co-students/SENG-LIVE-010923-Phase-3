class Owner():
    
    def __init__(self, first_name, last_name, age, account_balance=1000.00):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = account_balance

    # Decorator
    def balance_calculator(func):
        
        def report_balance(owner):
            print(f"{owner.first_name}'s Account Balance: ${owner.account_balance}")
            final_balance = func(owner)
            print(f"{owner.first_name}'s New Account Balance = ${final_balance}")

        return report_balance
        
    # $100 Cost
    @balance_calculator
    def vet_visit(self, bill=100):
        # Deduct $100 From Account / Report Final Account Balance
        print(f"Deducting {bill} from Account...")
        self.account_balance -= bill
        
        return '{:.2f}'.format(self.account_balance)
        

    # $50 Cost 
    @balance_calculator
    def weekly_food(self, bill=50):
        # Deduct $50 From Account / Report Final Account Balance
        print(f"Deducting {bill} from Account...")
        self.account_balance -= bill
        
        return '{:.2f}'.format(self.account_balance)
        

    # $75 Cost
    @balance_calculator
    def weekly_housing(self, bill=75):
        # Deduct $75 From Account / Report Final Account Balance
        print(f"Deducting {bill} from Account...")
        self.account_balance -= bill
        
        return '{:.2f}'.format(self.account_balance)