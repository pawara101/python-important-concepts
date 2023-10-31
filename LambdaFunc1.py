def Cube(y):
    return y**3

lambda_Cube = lambda y:y**3

print("Using function defined with `def` keyword, cube:", Cube(5))
 
# using the lambda function
print("Using lambda function, cube:", lambda_Cube(5))