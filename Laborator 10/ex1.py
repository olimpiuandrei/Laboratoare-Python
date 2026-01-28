def imparte(a, b):
    if b == 0:
        return None
    return a / b


try:
    primul_numar = float(input("Scrie primul numar: "))
    al_doilea_numar = float(input("Scrie al doilea numar: "))
    rezultat = imparte(primul_numar, al_doilea_numar)

    if rezultat is None:
        print("Eroare: Nu se poate imparti la zero!")
    else:
        print("Rezultatul impartirii este:", rezultat)

except ValueError:
    print("Te rog sa introduci doar numere valide!")
