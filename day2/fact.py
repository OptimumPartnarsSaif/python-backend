def factorial(n):
    if n < 0:
        raise ValueError("factorial has no negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    num = int(input("Enter a number!! "))
    fact = factorial(num)
    print("The factorial of " + str(num) + " is:")
    print(fact)
except ValueError as e:
    print("Error:", e)
