class Line:
    def __init__(self, len):
        self.length = len

    def showLenght(self):
        print(self.length)

    def __add__(self, other):
        return Line(self.length + other.length)


l1 = Line(10)
l2 = Line(20)
l3 = l1 + l2  # without override you cannot use + operator in between two objects

l3.showLenght()
