from circle import aria_cercului, circumferinta_cercului
from rectangle import aria_dreptunghiului, perimetru_dreptunghiului

try:
    r = float(input("Introdu raza cercului: "))
    lungime = float(input("Introdu lungimea dreptunghiului: "))
    latime = float(input("Introdu latimea dreptunghiului: "))

    if r <= 0 or lungime <= 0 or latime <= 0:
        raise ValueError("Valorile trebuie sa fie pozitive")

    print("\nCerc:")
    print("Aria cercului:", aria_cercului(r))
    print("Circumferinta cercului:", circumferinta_cercului(r))

    print("\nDreptunghi:")
    print("Aria dreptunghiului:", aria_dreptunghiului(lungime, latime))
    print("Perimetru dreptunghiului:", perimetru_dreptunghiului(lungime, latime))

except ValueError as e:
    print("Eroare:", e)

