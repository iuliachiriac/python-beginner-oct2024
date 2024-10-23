def my_func(a):
    b = 3  # a and b are local variables
    return a + b + X


def other_func(a):
    X = 0  # local variable that shadows global variable
    print("test", a, X)


X = 100  # global variable

print(X)
print(my_func(1), my_func(2))

other_func(7)
print(X)
