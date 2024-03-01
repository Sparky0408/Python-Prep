get_number = int(input("enter a number: "))

is_prime = True

if get_number <= 1:
    is_prime = True

for i in range(2, get_number):
    if get_number % i == 0:
        is_prime = False

if is_prime == True:
    print(get_number, "is prime number")

else:
    print(get_number, "is not prime number")
