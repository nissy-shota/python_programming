def log(msg, *values):
    if not values:
        print(msg)
    else:
        values_str = ','.join(str(x) for x in values)
        print(f'{msg}: {values_str}')

log('My numbers are', 1, 2)
log('Hi there')