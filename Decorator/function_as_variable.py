funcito is first object in python

print(issubclass(int, object))

def foo():
    pass

print(foo.__class__)
print(issubclass(foo.__class__, object))


print('-' * 20)

def add(x, y):
    return x + y
def sub(x, y):
    return x - y

def apply(func, x, y):
    func(x, y)

def main():
    print(apply(add, 1, 3))

if __name__ == "__main__":
    main()
    