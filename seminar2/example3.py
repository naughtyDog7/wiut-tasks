# Variables created in function are accessible only inside this function
def some_function():
    unreachable_variable = 1


# The NameError happens when we try to use variable that is out of scope
print(unreachable_variable)
