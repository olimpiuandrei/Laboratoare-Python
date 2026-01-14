def run_length_encoding(text):
    result = ""
    count = 1

    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
        else:
            result = result + text[i] + str(count)
            count = 1

    return result


try:
    text = input("Introdu un sir de caractere: ")

    if text == "":
        raise ValueError("Sirul nu poate fi gol.")

    print("Rezultat:", run_length_encoding(text))

except ValueError as e:
    print("Eroare:", e)
