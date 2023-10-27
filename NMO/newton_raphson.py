# Newton Raphson method

from math import cos, exp, sin


f = lambda x: exp(x) * cos(x) -1.4 * sin(x) - 0.8
df = lambda x: exp(x) * (cos(x) - sin(x)) - 1.4 * cos(x)
ddf = lambda x: -2 * exp(x) * sin(x) + 1.4 * sin(x)
# f = lambda x: 0.51 * x - sin(x)
# df = lambda x: 0.51 - cos(x)
# ddf = lambda x: sin(x)
# f = lambda x: exp(x) * cos(x) - 1.4
# df = lambda x: exp(x)*(cos(x) - sin(x))
# ddf = lambda x: -2 * exp(x) * sin(x)

if __name__ == '__main__':

    get_x = lambda x: f(x) / df(x)

    def start():
        x1 = float(input("Enter initail guess: "))
        acc = float(input("Accuracy: "))
        converge = (f(x1) - ddf(x1)) / df(x1)**2
        while converge > 1:
            start()
        
        x2 = x1 - get_x(x1)

        while abs(x2 - x1) > acc:
            x1 = x2

            x2 = x1 - get_x(x1)

        print(x2)
    start()