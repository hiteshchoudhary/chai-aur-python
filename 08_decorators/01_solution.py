import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {round(end-start)} time") #round off the time in a int instead of float.
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)

example_function(2)
