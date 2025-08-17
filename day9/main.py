def decorator(func):

    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# we use the decroter here after the func 
@decorator

def greet():
    print("Hello, World!")

greet()