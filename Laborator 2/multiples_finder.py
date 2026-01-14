try:
    x = int(input("Introdu numarul x: "))
    y = int(input("Introdu numarul y: "))

    if x == 0:
        raise ValueError("x nu poate fi 0.")

    print(f"Multiplii lui {x} mai mici decat {y} sunt:")

    for i in range(x, y, x):
        print(i,'')

except ValueError as e:
    print(f"Eroare: {e}")
