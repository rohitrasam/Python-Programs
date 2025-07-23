# people = [
#     ("Rohit Rasam", "Male"),
#     ("Ameya Thopte", "Female"),
#     ("Omar Mapkar", "Male"),
#     ("Vaishanvi Gosavi", "Female"),
#     ("Amaan Khan", "Male"),
#     ("Peter Parker", "Male"),
#     ("Mary Jane", "Female"),
#     ("Harry Osborn", "Male"),
#     ("Rashmi Rasam", "Female"),
#     ]
# r_names = list(filter(lambda x: 'R' in x[0] or 'r' in x[0], people))
# females = list(filter(lambda x: x[1] == "Female", people))

# print(f"{len(males)}\n{len(females)}")
# print(f"{r_names}")

# def salutation(prefix, name, gender):
#     return {"Name": f"{prefix} {name}", "Gender": gender}

# def convert(data: list[tuple[str]]):
#     if data[1] == 'Male':
#         return salutation("Mr.", data[0], data[1])
#     return salutation("Mrs.", data[0], data[1])
    

# x = list(map(convert, people))
# print(x)


# import time
# import timeit

# print(timeit.timeit(stmt='', setup='', timer='', number=1, globals=''))


# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# def fib(n):
#     arr = [0, 1]
#     for i in range(2, n+1):
#         arr.append(arr[i-1] + arr[i-2])
#     return arr

# print(*fib(20))
# num = int(input())
# for i in range(num):
#     print(fib(i), end=" ")
# arr = [1, 2, 3]
# print(arr.pop())


# # Wrapper functions
# def f1(func):
#     def wrapper(*args, **kwargs):
#         print('Started')
#         func(*args, **kwargs)
#         print('Ended')
#     return wrapper

# @f1
# def f(a, b=9):
#     print(a, b)
    
# f1(f) -----> <function __main__.f1.<locals>.wrapper()>
# f1(f)()

# x = f1(f)  => using decorator instead of this line
# x()

# f("Hi!")



# def func(*args, **kwargs):
#     print(args, kwargs)

# s = ['Rohit', 'Rasam']
# d = {'a': 'Rohit', 'b': 'Rasam'}
# func(*s, d, key=69, abc=123)


# import time

# def func(seconds):
#     print(f'Sleeping for {seconds} seconds')
#     time.sleep(seconds)

# t1 = time.time()
# func(4)
# func(3)
# func(2)
# t2 = time.time()
# print(t2 - t1)
# from manim import *


# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(RED, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # show the circle on screen

# import os

# for x in os.listdir("py_games/gameTut/data/images/tiles/decor"):
#     print(x)


# class a:
#     def __init__(self, val) -> None:
#         self.val1 = val
#         self.val2 = self.val1
    
#     def update(self, val):
#         self.val2 = val


# ob = a(3)
# print(ob.val1, ob.val2)
# ob.update(4)
# print(ob.val1, ob.val2)

from time import time


nums = list(range(100000000))

start = time()

total = sum(nums) % 10
end = time()

print(f"Using sum(): {end-start} secs")

total = 0
start = time()
for num in nums:
    total = (total + num) % 10
end = time()
print(f"Using for loop: {end-start} secs")

n = len(nums) -1
left, right = 0, n
total = 0
start = time()
while left < right:
    total = (total + nums[left] + nums[right]) % 10
    left += 1
    right -= 1
end = time()
print(f"Using two pointers: {end-start} secs")
