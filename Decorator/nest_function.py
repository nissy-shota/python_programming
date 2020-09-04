def outer():
    x = 1
    def inner():
        print(locals())
        print(globals())
        print(x)
    inner()

print(outer())