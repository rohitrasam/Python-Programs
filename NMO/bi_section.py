# Bi-section method
from math import cos, exp, sin

# f = lambda x : x * exp(x) - 3.1 * cos(x) 
f = lambda x : x**3 - x**2 - x - 1 
# f = lambda x : -0.9 * x**2 + 1.7 * x + 2.5

if __name__ == '__main__':

    def start():
        x1, x2 = map(float, input("Enter 2 guesses: ").split())
        accuracy = float(input("Accuracy: "))

        if not x1 and not x2:
            x1 = 0
            x2 = 1
    
        f1 = f(x1)
        f2 = f(x2)

        while f1 * f2 > 0:
            start()
        
        x3 = (x2 + x1) / 2
        while abs(x2 - x1) > accuracy:
            
            f3 = f(x3)

            if f3 * f1 > 0:
                x1 = x3
                f1 = f3
            else:
                x2 = x3
                f2 = f3
            x3 = (x2 + x1) / 2
            print(x3)
        print(x3)
    
    start()
            