def twice(func):
    def wrapper(*args, **kwargs):
        print(f'args : {args}')
        return func(*args, **kwargs) * 2
    return wrapper

@twice
def add(x, y):
    return x + y

print(add(1, 3))