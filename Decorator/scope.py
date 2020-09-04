def foo(arg):
    x = 10
    print(locals())

y = 10
print(globals())

print(foo([20, 30]))