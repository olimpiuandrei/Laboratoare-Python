def count_words_in_file(filename):
    try:
        file = open(filename, "r")
        text = file.read()
        file.close()

        words = text.split()
        return len(words)

    except FileNotFoundError:
        print("Eroare: Fisierul nu exista.")
        return 0


numar_cuvinte = count_words_in_file("ex_1")
print(numar_cuvinte)
