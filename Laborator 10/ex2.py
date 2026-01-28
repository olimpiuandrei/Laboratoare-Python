def suma_numerelor_din_fisier(fisier):
    total = 0

    try:
        with open(fisier, "r") as f:
            for nr_linie, linie in enumerate(f, 1):
                linie = linie.strip()
                try:
                    valoare = float(linie)
                    total += valoare
                except ValueError:
                    print(f"[Linia {nr_linie}] : Nu este un numar valid.")

        return total

    except FileNotFoundError:
        print(f"Eroare: fisierul '{fisier}' nu a fost gasit!")
        return None
    except Exception as e:
        print(f"A aparut o eroare la citirea fisierului: {e}")
        return None

nume_fisier = "numere"

rezultat = suma_numerelor_din_fisier(nume_fisier)

if rezultat is not None:
    print(f"\nSuma numerelor valide din fisier este: {rezultat}")
