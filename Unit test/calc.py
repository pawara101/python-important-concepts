def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y

def divide(x,y):
    if y==0:
        raise ValueError("Cannot divide by 0")
    else:
        return x/y