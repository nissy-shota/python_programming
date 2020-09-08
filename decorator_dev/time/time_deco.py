from functools import wraps
import time

def time_elaps(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start

        print("{:.03} ms in {}".format(elapsed_time * 1000, 'example_func'))
        return result

    return wrapper

@time_elaps
def print100():
    
    for i in range(100):
        i += i


print100()