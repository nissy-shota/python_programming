def my_decorator(target_function):
    def wrapper_function(*args, **kwargs):
        kwargs['test_key'] = 'デコレータで書き換えられた値'
        return target_function(*args, **kwargs)
    return wrapper_function

@my_decorator
def my_method(*args, **kwargs):
    if 'test_key' in kwargs:
        print('test_keyの値は、[{}]'.format(kwargs['test_key']))
    else:
        print('test_keyに値は、入っていません。')

my_method()
my_method(test_key="テスト用の値")