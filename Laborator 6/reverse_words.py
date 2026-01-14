def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)


try:
    sentence = input("Introdu o propozitie: ")

    if sentence.strip() == "":
        raise ValueError("Propozitia nu poate fi goala.")

    print("Rezultat:", reverse_words(sentence))

except ValueError as e:
    print("Eroare:", e)
