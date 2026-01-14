try:
    word = input("Introdu un cuvant: ").lower()

    if word == word[::-1]:
        print("Cuvantul este palindrom.")
    else:
        print("Cuvantul NU este palindrom.")
except ValueError as e:
    print(f"Eroare: {e}")
