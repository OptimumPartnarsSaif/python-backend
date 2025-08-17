def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError("All arguments must be positive numbers")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def add(a, b):
    return a + b

@validate_positive
def multiply(a, b, c=1):
    return a * b * c

print(add(5, 3))
print(multiply(2, 3))
print(multiply(2, 3, c=4))
print(add(1,-2))
#
