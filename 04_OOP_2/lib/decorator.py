# 1. ✅ First Class Functions
# "[We can] assign them to variables, store them in data structures, pass them as arguments
# to other functions, and even return them as values from other functions."
# See more => http://bit.ly/3YQh8KR

    # Create functions to be used as callbacks 

# def walk(pet):
#     print(f'{pet} has been walked!')

# def feed(pet):
#     print(f'{pet} has been fed!')

    # Create a higher-order function that will take a callback as an argument

# Higher Order Function => Accepts a Function
# def execute_task(func):
    
#     # Callback Function Invocation
#     return func("Rose")

# # execute_task(walk)
# execute_task(feed)

# 2. ✅ Create a higher-order function that returns a function

# def execute_task():
#     def feed(pet="Rose"):
#         print(f'{pet} has been fed!')

#     # def walk(pet="Rose"):
#     #     print(f'{pet} has been walked!')
    
#     return feed

    # return feed, walk => Returns a Tuple of Function References

# feed = execute_task() # => feed Function Reference

# feed() #=> "Rose has been fed!"
# feed("Spot") #=> "Spot has been fed!""

# execute_task()("Rose")

# 3. ✅ Decorator

# Create a function that:
    # - takes a function as an argument
    # - has an inner function defined 
    # - returns the inner function

# Tools:

    # .format() => Method (String)
    # https://www.geeksforgeeks.org/python-string-format-method/

    # .round() => Format Actual Calculation of Discount
    # https://www.geeksforgeeks.org/round-function-python/

# Decorator
def coupon_calculator(func):
    
    # Inner Function
    def report_price():
        print('Initial Price = $35.00')
        final_price = func(35.00)
        print(f'Newly Discounted Price = ${final_price}')

    return report_price

# Callback Function to Calculate New Price
# def calculate_price(price):
    
#     # We end up with a Floating Point Number Rounded to the Nearest
#     # Hundreth
#     # .2f => Two Decimal Point Floating Number
#     return '{:.2f}'.format(round(price / 2, 2))

# Try using a decorator with / without pie syntax '@'

# Without pie syntax 

# report_price = coupon_calculator(calculate_price)
# report_price()

# With pie syntax

@coupon_calculator
def calculate_price(price):
    
    # We end up with a Floating Point Number Rounded to the Nearest
    # Hundreth
    # .2f => Two Decimal Point Floating Number
    return '{:.2f}'.format(round(price / 2, 2))

calculate_price()

# @coupon_calculator
# def some_other_function():
#     return "Something"

# some_other_function()

# @coupon_calculator
# def some_other_function():
#     return "Something"

# some_other_function()