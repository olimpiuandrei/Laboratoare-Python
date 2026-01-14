try:
    user_input = input("Introdu numere separate prin virgula: ")
    numbers = []

    for x in user_input.split(","):
        numbers.append(int(x.strip()))

    if len(numbers) == 0:
        print("Lista este goala.")
    else:
        print("Lista:", numbers)
        print("Maxim:", max(numbers))
        print("Minim:", min(numbers))

except ValueError:
    print("Eroare: Introdu doar numere intregi separate prin virgula.")
