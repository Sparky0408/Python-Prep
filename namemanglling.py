class test:
    a = 10
    __b = 20

    def __init__(self):
        self.__a = 100


t = test()
print(t.a)  ## output 10

# print(t.__b) error you cannot acces hidden variables directly from outside class


print(
    t._test__b
)  # here we have use class name ._ classname and then . varible name  ##output 20

print(t._test__a)
