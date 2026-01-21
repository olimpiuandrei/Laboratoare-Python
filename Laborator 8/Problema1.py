import math

try:

    num = int(input("Introdu un numar intreg pozitiv: "))
    angle = float(input("Introdu un unghi in grade: "))

    if num < 0:
        raise ValueError("Factorialul este definit doar pentru numere pozitive.")
    radacina = math.sqrt(num)
    factorial = math.factorial(num)
    sinus = math.sin(math.radians(angle))
    print("\nRezultate:")
    print(f"Radacina patrata a lui {num} este: {radacina}")
    print(f"Factorialul lui {num} este: {factorial}")
    print(f"Sinusul unghiului de {angle} grade este: {sinus}")

except ValueError as ve:
    print("Eroare de valoare:", ve)

