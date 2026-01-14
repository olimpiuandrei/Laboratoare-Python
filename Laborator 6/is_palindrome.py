def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text == text[::-1]


try:
    text = input("Introdu un text: ")

    if text.strip() == "":
        raise ValueError("Textul nu poate fi gol.")

    print("Este palindrom?", is_palindrome(text))

except ValueError as e:
    print("Eroare:", e)
