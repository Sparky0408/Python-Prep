def deco_result(func):
    def distinction(marks):
        for m in marks:
            if m > 75:
                print(m, "distiction")
        func(marks)

    return distinction


@deco_result
def result(marks):
    for m in marks:
        if m > 30:
            print("pass")


marks = [35, 34, 76, 84, 87]

result(marks)
