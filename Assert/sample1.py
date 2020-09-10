
expect = 1

user_input = 0

try:
    assert expect == user_input, f'expect{expect}, your input is {user_input}' 
except AssertionError as e:
    print('AssertionError :', e)

