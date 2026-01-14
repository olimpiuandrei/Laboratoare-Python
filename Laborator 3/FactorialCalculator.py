try:
    n = int(input("Introdu un numar intreg: "))

    if n < 0:
        raise ValueError("Numarul nu poate fi negativ.")

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"Factorialul lui {n} este: {factorial}")

except ValueError as e:
    print(f"Eroare: {e}")
