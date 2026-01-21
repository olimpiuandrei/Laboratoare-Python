import math_operations

try:
    a = float(input("Introdu primul numar: "))
    b = float(input("Introdu al doilea numar: "))

    print("Adunare:", math_operations.adunare(a, b))
    print("Scadere:", math_operations.scadere(a, b))
    print("Inmultire:", math_operations.inmultire(a, b))

    if b == 0:
        raise ZeroDivisionError("Nu se poate imparti la zero")

    print("Impartire:", math_operations.impartire(a, b))

except ValueError:
    print("Eroare: trebuie sa introduci numere valide")

