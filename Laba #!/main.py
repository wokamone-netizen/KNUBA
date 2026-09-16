import math


radius = float(input("Введіть радіус основи циліндра: "))
height = float(input("Введіть висоту циліндра: "))


area = math.pi * radius ** 2
volume = area * height


print(f"Площа основи циліндра: {area:.2f}")
print(f"Об'єм циліндра: {volume:.2f}")