def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.call_count} time(s).")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@call_counter
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))
print("Final count:", greet.call_count)


