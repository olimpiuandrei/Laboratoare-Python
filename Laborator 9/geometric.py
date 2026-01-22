import math

class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def __str__(self):
        area_value = self.area()
        return f"Circle with radius {self.radius} has area {round(area_value, 2)}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"


try:
    print("=== Calculator Forme Geometrice ===")
    print("\n1. Cerc")
    print("2. Dreptunghi")

    choice = input("Alege o forma: ")

    if choice == "1":
        radius_input = input("Introdu raza cercului: ")

        if radius_input == "":
            print("Eroare! Nu ai introdus raza.")
        else:
            radius = float(radius_input)

            if radius < 0:
                print("Eroare! Raza nu poate fi negativa.")
            else:
                circle = Circle(radius)
                print(circle)

    elif choice == "2":
        width_input = input("Introdu latimea dreptunghiului: ")
        height_input = input("Introdu inaltimea dreptunghiului: ")

        if width_input == "" or height_input == "":
            print("Eroare! Nu ai introdus dimensiunile.")
        else:
            width = float(width_input)
            height = float(height_input)

            if width < 0 or height < 0:
                print("Eroare! Dimensiunile nu pot fi negative.")
            else:
                rectangle = Rectangle(width, height)
                print(rectangle)

    else:
        print("Optiune invalida!")

except ValueError:
    print("Eroare! Te rog introdu valori numerice valide.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
