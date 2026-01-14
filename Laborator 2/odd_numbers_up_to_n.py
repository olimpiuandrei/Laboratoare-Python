try:
    n = int(input("Introdu numarul n: "))

    if n < 1:
        raise ValueError("n trebuie sa fie mai mare decat 0.")

    print(f"Numerele impare pana la {n} sunt:")

    for i in range(1, n + 1, 2):
        print(i,)

except ValueError as e:
    print(f"Eroare: {e}")
