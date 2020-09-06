funcs = []
def appender(*args, **kwargs):
    def decorator(f):
        # args や kwargsの内容によって処理内容を変えたり変えなかったり
        print(args)
        if kwargs.get('option1'):
            print('option1 is True')

        if kwargs.get('option2'):
            print('option2 is True')

        # 元の関数をfuncsに追加
        funcs.append(f)

    return decorator


@appender('arg1', option1=True)
def hoge():
    print('hoge')

@appender('arg2', option2=True)
def fuga():
    print('fuga')

for f in funcs:
    f()