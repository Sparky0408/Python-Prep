import math


def Calculate_area_cirum(radius):
    area = round(math.pi * radius**2, 2)
    circum = round(2 * math.pi * radius, 2)

    return area, circum


number = int(input("enter the radius of circle: "))

area, circum = Calculate_area_cirum(number)

print(f"area of the circle is {area} and circumfarence is {circum}")
