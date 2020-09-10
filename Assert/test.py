def number_test(x):
    try:
        assert x.isdigit(), f'{x} is not a number'
    except AssertionError as ase:
        print('AssertionError :', ase)

num = input('input number : ')
number_test(num)