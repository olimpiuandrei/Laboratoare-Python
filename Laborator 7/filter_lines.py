def filter_lines(f_in, f_out, keyword):
    try:
        f_in = open(f_in, "r")
        lista_linii = f_in.readlines()
        f_in.close()
        f_out = open(f_out, "w")

        for linie in lista_linii:
            if keyword in linie:
                f_out.write(linie)

        f_out.close()
        print("Fisierul filtrat a fost creat in " + f_out.name)

    except FileNotFoundError:
        print("Eroare: Fisierul nu exista.")
        return 0


# apel direct
filter_lines("ex3in", "ex3out", "Python")
