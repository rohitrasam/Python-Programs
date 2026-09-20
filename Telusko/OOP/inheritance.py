class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B:  # B is a sub class of A

    def __init__(self):
        # super().__init__()   # calls the init method of class A
        print('in B init')

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):   # MRO(Method Resolution Order)
    def __init__(self):
        super().__init__()  # calls init of class A since A is 1st
        print('in C init')

    def feat(self):
        super().feature2()  # to represent super class we use super method


b1 = B()  # object of class B will call the constructor/init of class A because B does not have it's own
# constructor/init method
c1 = C()
c1.feat()


# class C(B):  # Multilevel inheritance
#     def feature5(self):
#         print("Feature 5 working")
#
#
# class D(B, C):  # Multiple inheritance
#     def feature6(self):
#         print("Feature 6 working")

