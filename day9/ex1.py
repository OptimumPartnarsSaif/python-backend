def multiplier_generator(base):
    def multiply(value):
        if base == 0:
            return value ** 2
        return value * base
    return multiply

doubler = multiplier_generator(2)
tripler = multiplier_generator(3)
squarer = multiplier_generator(0)

print(doubler(5))
print(tripler(4))
print(squarer(6))

