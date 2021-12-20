
def _calculate(a, b, c):
    if a * b > c:
        raise Exception("HATA!")

    return a * b


def debug_func(number1, number2, limit):
    limit = min(limit, 10)
    return _calculate(number1, number2, limit)


print(debug_func(4, 3, 12))
