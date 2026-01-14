try:
    principal = float(input("Introdu suma initiala (principal): "))
    rate = float(input("Introdu rata anuala a dobanzii (%): "))
    time = float(input("Introdu timpul (ani): "))

    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Valorile nu pot fi negative.")

    interest = (principal * rate * time) / 100
    print(f"Dobanda calculata este: {interest:.2f}")

except ValueError as e:
    print(f"Eroare: {e}")