def careful_divide(x, y):

    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError('Invalid input')

x, y = 5, 2

try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid input')
else:
    print(f'Result is {result}')