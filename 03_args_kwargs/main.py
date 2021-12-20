
def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number

    return result


def func(a, b, *args, **kwargs):
    result = a + b
    if kwargs.get("multiply", False):
        result += multiply(*args)
    return f"{kwargs.get('prefix', '')}{result}"


print(func(2, 3, 5, 6, multiply=True, prefix="Result : "))
print(func(2, 3, 5, 6, multiply=False, prefix="Result : "))


