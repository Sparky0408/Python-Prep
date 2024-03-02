class test:
    def f1(self):
        print("first fucntion")


class test2(test):
    def f1(self):
        # super().f1()
        print("second function")


t2 = test2()  # here which is method is called whoes object is made

t2.f1()
