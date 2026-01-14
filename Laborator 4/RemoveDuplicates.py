try:
    user_input = input("Introdu numere separate prin virgula: ")
    numbers = []

    for x in user_input.split(","):
        numbers.append(int(x.strip()))

    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    print("Lista fara duplicate:", unique_numbers)

except ValueError:
    print("Eroare: Introdu doar numere intregi separate prin virgula.")
