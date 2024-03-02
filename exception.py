# here we have to use correct class name for exception handling which may can occurs in program execution
# else block will run when no exceptions in happen
# finally block will always run regadless exception is occur or not

try:
    number1 = int(input("enter a first number: "))
    number2 = int(input("enter a first number: "))

    divide = number1 / number2

    print(divide)

except ZeroDivisionError as e:
    print(e)

except ValueError as r:
    print(r)

else:
    print("no exception occurs")

finally:
    print("finally block")
