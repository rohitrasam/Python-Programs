# """ 1st method """

# class Singleton:

#     __instance = None    # class variable

#     @staticmethod
#     def getInstance():
#         if Singleton.__instance is None:
#             Singleton()
        
#         return Singleton.__instance

#     def __init__(self):
#         if Singleton.__instance is not None:
#             raise Exception("Single exists already!")
#         else:
#             Singleton.__instance = self


# s1 = Singleton.getInstance()
# print(s1)
# s2 = Singleton.getInstance()
# print(s2)


""" 2nd method """

class Singleton:

    __instance = None

    # also called when creating an object, called before __init__()
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
    
        return cls.__instance

s1 = Singleton()
print(s1)
s1.y = 10
s2 = Singleton()
print(s2)
print(s2.y)