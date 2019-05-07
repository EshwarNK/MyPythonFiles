'''When we do pass by reference, we are passing the object itself, we are passing the original variable itself inside the function
So any change in the value of the variable inside the function will be reflected back outside the function also'''
a = [1,2,3,4]
def hello(x):
    print(x)
    x[0] = 12       #Here we directly changing the value at 0th index of a to 12. This will be reflected outside the hello function also.
    print(x)
    return
hello(a)
print(a)
