some_variable = 1


# This function has local variable with the same name as outer 'some_variable'
# Local variable has no connection with outer variable with same name, they are 2 different variables
# Changing one of them doesn't affect other one
# Local variable shadows outer variable, and each statement inside of function will use this local variable only
def some_function():
    some_variable = 3
    print(some_variable)  # This will print local variable


print(some_variable)  # This will print outer variable
