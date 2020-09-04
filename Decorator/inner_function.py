def outer():
    def inner():
        print("Inside inner")
    return inner

foo = outer()

print(foo)
print(foo())
