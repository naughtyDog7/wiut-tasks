some_unique_name = 1


# Function with argument that has the same name as outer variable
# The problem is that argument will shadow outer variable,
# and instead of using outer variable function will use only this argument
def some_function(some_unique_name):
    print(some_unique_name)


# This will print 2, even if inside of function we try to print outer variable 1
some_function(2)
