def hello(x):
    x = 34              #Here we are changing the value inside the function, it will not affect the value of x i.e;12 outside the function
    print("Before print:",id(x))
    print(x)
    print("After print:",id(x))
    return
x=12                # THis value of 12 is not affected outside the function
hello(x)            # Here we are passing only the copy of the value and not the original value
print(id(x))
hello(13)