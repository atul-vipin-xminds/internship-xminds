import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken:", end - start, "seconds")
    return wrapper

@timer
def test():
    for i in range(1000000):
        pass

test()