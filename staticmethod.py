class A:
    @staticmethod
    def f1(a, b):
        print("f1")

    @staticmethod
    def f2(self):
        print("f2")


obj1 = A()
obj1.f1(1, 2)


A.f2(1)
