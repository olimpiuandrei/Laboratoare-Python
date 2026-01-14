import random

number = random.randint(1, 20)
attempts = 5

print("Am ales un numar intre 1 si 20. Ai 5 incercari.")

while attempts > 0:
    try:
        guess = int(input("Ghiceste numarul: "))

        if guess < 1 or guess > 20:
            print("Numarul trebuie sa fie intre 1 si 20.")
            continue

        if guess < number:
            print("Prea mic!")
        elif guess > number:
            print("Prea mare!")
        else:
            print("Corect! Ai castigat!")
            break

        attempts -= 1
        print(f"Incercari ramase: {attempts}")

    except ValueError:
        print("Introdu un numar intreg valid.")

if attempts == 0:
    print(f"Ai pierdut! Numarul era {number}")
