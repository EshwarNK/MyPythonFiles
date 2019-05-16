def fib(c):
    a,b =0,1
    for i in range(c):
        a,b = b, a+b
    return a
print(fib(5))