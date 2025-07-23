def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    
    return wrapper

@f1
def f(a):
    print(a)

# wrap = f1(f)
# wrap("Hi")
f("Hello")



def add(x, y):
    return x+y

