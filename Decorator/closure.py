
def outer():
    x = 1

    def inner():
        print(x)

    return inner

foo = outer()
# print(foo.func_closure)
print(foo.__closure__)