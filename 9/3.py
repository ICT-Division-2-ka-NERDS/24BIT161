import random

def square():
    
    r = random.sample(range(-15, 16), 10)
    print("random numbers:", r)
    
    s = list(map(lambda x: x**2, r))
    print("squared:", s)
square()
