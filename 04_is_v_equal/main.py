a = 1000
b = 1000
print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = 25
b = 25
print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = -5
b = -5
print(a is b)

a, b = 1000, 1000
print(a == b)
print(a is b)


def func():
    a = 1000
    b = 1000
    print(a is b)

func()
