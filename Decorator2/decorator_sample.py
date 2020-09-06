def deco(func):
    def wrapper(*args, **kwargs):
        print('--start--')
        print(f'args:{args}')
        print(f'kwargs:{kwargs}')
        func(*args, **kwargs)
        print('--end--')
    return wrapper

@deco
def test():
    print('Hello Decorator')
