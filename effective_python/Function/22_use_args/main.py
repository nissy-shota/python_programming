def log(msg, *values):
    if not values:
        print(msg)
    else:
        values_str = ','.join(str(x) for x in values)
        print(f'{msg}: {values_str}')

def log2(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ','.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')

def my_generator():
    for i in range(10):
        yield i
def my_func(*args):
    print(args)

log('My numbers are', 1, 2)
log('Hi there')

# not slice, using catch all unpack
favorites = [7, 33, 99]
log('Facorite colors', *favorites)

it = my_generator()
my_func(*it)

log2('Favorite numbers', 7, 33)