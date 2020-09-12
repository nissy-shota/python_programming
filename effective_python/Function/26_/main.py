from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
            f'-> {result!r}')

        return result
    return wrapper

@trace
def fibonacci(n):
    """return the n-th Fibonacci number

    Args:
        n ([type]): [description]
    """

    if n in (0,1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

print(fibonacci(4))
print(help(fibonacci))
