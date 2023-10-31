x = 5
y = "hello"

try:
    z = x + y # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'
except:
    print("error is :",TypeError)
