def reverse_lines(f_in, f_out):
    try:
        f_in = open(f_in, "r")
        lista_linii = f_in.readlines()
        f_in.close()
        f_out = open(f_out, "w")

        for linie in lista_linii:
            # scot spatiile goale de la sfarsit si de la inceput de linie si \n
            linie1 = linie.strip()
            linie_inversa = linie1[::-1]
            f_out.write(linie_inversa + "\n")
        f_out.close()
        print("Textul a fost inversat si scris in fisierul", f_out.name)

    except FileNotFoundError:
        print("Eroare: Fisierul nu exista.")
        return 0

reverse_lines("ex2in", "ex2out")
