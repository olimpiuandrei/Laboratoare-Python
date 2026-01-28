class GestionarInventar:
    def __init__(self):
        # Inventarul initial cu produse
        self.stoc = {
            "mere": 50,
            "pere": 30,
            "apa": 100,
            "paine": 20
        }

    def actualizeaza_stoc(self, produs, cantitate):
        if cantitate < 0:
            raise ValueError("Cantitatea nu poate fi negativa!")
        self.stoc[produs] = cantitate

    def verifica_stoc(self, produs):
        return self.stoc[produs]


# Cream obiectul pentru magazin
magazin = GestionarInventar()

try:
    print(f"Produsele existente in stoc: {list(magazin.stoc.keys())}")

    print("Pasul 1: Adaugam sau actualizam un produs")
    produs_nou = input("Introdu numele produsului: ")
    cantitate_noua = int(input("Introdu cantitatea: "))

    # Adaugam sau actualizam produsul
    magazin.actualizeaza_stoc(produs_nou, cantitate_noua)
    print("Produsul a fost salvat/actualizat cu succes!")

    print("\nPasul 2: Verificam stocul unui produs")
    produs_cautat = input("Ce produs vrei sa cauti? (ex: 'mere' sau ce ai adaugat): ")

    stoc_gasit = magazin.verifica_stoc(produs_cautat)
    print(f"Produsul '{produs_cautat}' are in stoc: {stoc_gasit}")

except ValueError:
    print("Eroare: Ai introdus o cantitate negativa sau invalida!")
except KeyError:
    print("Eroare: Produsul cautat nu exista in inventar!")
