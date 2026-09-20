# Newton Raphson method

from math import cos, exp, sin


f = lambda x: x*exp(x) - 3.1*cos(x)
df = lambda x: x*exp(x) + exp(x) + 3.1*sin(x)
ddf = lambda x: x*exp(x) + 2*exp(x) + 3.1*cos(x)
# f = lambda x: x**3 + x**2 + 3*x +4
# df = lambda x: 3*x**2 +2*x + 3 
# ddf = lambda x: 6*x + 2
# f = lambda x: x**3 - 8*x**2 + 17*x +4
# df = lambda x: 3*x**2 - 16*x + 17 
# ddf = lambda x: 6*x - 16
# f = lambda x: cos(x) - 1.3*x
# df  = lambda x: -sin(x) - 1.3
# ddf = lambda x: -cos(x)
# f = lambda x: x*sin(x) + cos(x)
# df = lambda x: x*cos(x) 
# ddf = lambda x: -(x*sin(x)) + cos(x)
# f = lambda x: x**4 + x**3 - 3*x**2 - x + 2
# df = lambda x: 4*x**3 + 3*x**2 - 6*x-1 
# ddf = lambda x: 12*x**2 +6*x - 6
# f = lambda x: exp(x) * cos(x) -1.4 * sin(x) - 0.8
# df = lambda x: exp(x) * (cos(x) - sin(x)) - 1.4 * cos(x)
# ddf = lambda x: -2 * exp(x) * sin(x) + 1.4 * sin(x)
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
        acc = int(input("Accuracy in deimcal places: "))
        converge = (f(x1) * ddf(x1)) / df(x1)**2
        while converge > 1:
            start()
        
        x2 = x1 - get_x(x1)

        while abs(x2 - x1) > 1/(10**acc):
            x1 = x2

            x2 = x1 - get_x(x1)

        print(f"The root of the equation is {round(x2, acc)}")
    start()