from Decorators3 import*
def split_string(function):
    def hidden():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return hidden
@split_string
@uppercase_decorator
def say_hi():
    return "Hello Pawara"

print(say_hi())