def foo():

    text = 'local val'
    print(text)
    print(locals)

text = 'global val'

print(text)
print(globals)
foo()
print(text)