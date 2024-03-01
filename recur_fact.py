def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

number = int(input("enter the number: "))

result = fact(number)

print(f"the factorial of {number} is {result}")
