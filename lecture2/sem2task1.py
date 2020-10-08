def new_line():
    print('*')


# 1 * 3 = 3
def three_lines():
    new_line()
    new_line()
    new_line()


# 3 * 3 = 9
def nine_lines():
    three_lines()
    three_lines()
    three_lines()


# 9 + 9 + 3 + 3 + 1 = 25
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()


print('=====================================')
clear_screen()
print('=====================================')