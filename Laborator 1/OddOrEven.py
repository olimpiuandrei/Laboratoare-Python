try:
    number = int(input("Introdu un numar intreg: "))

    if number % 2 == 0:
        print(f"Numarul {number} este PAR.")
    else:
        print(f"Numarul {number} este IMPAR.")

except ValueError:
    print("Eroare: Trebuie sa introduci un numar intreg.")
