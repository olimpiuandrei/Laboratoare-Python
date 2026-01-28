import pandas as pd
import numpy as np

np.random.seed(42)

num_zile = 60
produse_disponibile = ['Laptop', 'Telefon', 'Casti', 'Mouse', 'Tastatura']
vanzari = []

#generarea datelor pentru fiecare zi
for zi in range(num_zile):
    num_produse_zi = np.random.randint(5, 16)

    for _ in range(num_produse_zi):
        #alegem un produs random
        produs = np.random.choice(produse_disponibile)

        #generam pretul
        pret = np.random.normal(40, 8)
        pret = max(1, round(pret, 2))  # nu vrem preturi negative sau zero

        #simulam promotii cu probabilitate de 30%: reducere 20%
        if np.random.rand() < 0.3:
            pret = round(pret * 0.8, 2)

        #generam cantitatea vanduta
        cantitate = np.random.randint(1, 11)

        #salvare
        vanzari.append({
            'zi': zi + 1,
            'produs': produs,
            'pret': pret,
            'cantitate': cantitate
        })

df = pd.DataFrame(vanzari)

df['total_vanzari'] = df['pret'] * df['cantitate']
df['profit'] = df['total_vanzari'] * 0.3
pret_mean = df['pret'].mean()
pret_max = df['pret'].max()
pret_min = df['pret'].min()

cant_mean = df['cantitate'].mean()
cant_max = df['cantitate'].max()
cant_min = df['cantitate'].min()

profit_mean = df['profit'].mean()
profit_max = df['profit'].max()
profit_min = df['profit'].min()


total_vanzari = df['total_vanzari'].sum()
profit_total = df['profit'].sum()


print("Statistici generale:")
print(f"Preturi - media: {pret_mean:.2f}, maxim: {pret_max}, minim: {pret_min}")
print(f"Cantitati - media: {cant_mean:.2f}, maxim: {cant_max}, minim: {cant_min}")
print(f"Profit - media: {profit_mean:.2f}, maxim: {profit_max:.2f}, minim: {profit_min:.2f}")
print(f"Total vanzari pe 60 de zile: {total_vanzari:.2f}")
print(f"Profit total pe 60 de zile: {profit_total:.2f}")


vanzari_pe_zi = df.groupby('zi').agg({'total_vanzari': 'sum', 'profit': 'sum'}).reset_index()
print("\nTotal vanzari si profit pe fiecare zi:")
print(vanzari_pe_zi.head(10))


