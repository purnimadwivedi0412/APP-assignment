def decorator(func):
    def wrapper(*args, **kwargs):
        print("Addition of two numbers:")
        result = func(*args, **kwargs)
        print("Result =", result)
    return wrapper

# Function to add two numbers
@decorator
def add(a, b):
    return a + b
add(10, 20)
