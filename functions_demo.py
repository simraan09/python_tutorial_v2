def cube(number):
    return pow(number, 3)


# print(cube(20))

def max_number(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number1 and number2 > number3:
        return number2
    else:
        return number3


def max_number_alt(number1, number2, number3):
    number_list = [number1, number2, number3]
    number_list.sort()
    return number_list[2]
