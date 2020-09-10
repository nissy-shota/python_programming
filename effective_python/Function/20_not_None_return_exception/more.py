
# helper function
def careful_divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Raises:
        ValueError: When the inputs cannnot be divided.
    
    """

    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')


x, y = 5, 2

try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid input')
else:
    print(f'Result is {result}')