import math

radius_input = input("Введіть радіус основи циліндра: ")
height_input = input("Введіть висоту циліндра: ")

if radius_input.replace(".", "", 1).isdigit() and height_input.replace(".", "", 1).isdigit():
    radius = float(radius_input)
    height = float(height_input)

    area = math.pi * radius ** 2
    volume = area * height

    print(f"Площа основи циліндра: {area:.2f}")
    print(f"Об'єм циліндра: {volume:.2f}")
else:
    print("Помилка! Потрібно вводити тільки числа.")