try:
    user_input = input("Introdu valori separate prin virgula: ")
    elements = tuple(x.strip() for x in user_input.split(","))

    search = input("Cauta valoarea: ")

    if search in elements:
        print(search, "se regaseste in tupla la indexul", elements.index(search))
    else:
        print(search, "NU se regaseste in tupla")

except Exception:
    print("Eroare la procesarea datelor.")
