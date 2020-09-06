def one(*args):
    print(args)

one()
one(1, 2, 3)

def two(x, y, *args):
    print(x)
    print(y)
    print(args)

two('a', 'b', 'c')

def add(x, y):
    return x + y

lst = [1,2]
print(add(lst[0], lst[1]))
print(add(*lst))

def foo(**kwargs):
    print(kwargs)
    
foo()
foo(x=1, y=2)

dct = {'x': 1, 'y': 2}
def bar(x, y):
    return x + y

print(bar(**dct))