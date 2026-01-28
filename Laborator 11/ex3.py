import pandas as pd
import numpy as np

np.random.seed(42)


num_zile = 60
produse_disponibile = ['Laptop', 'Telefon', 'Casti', 'Mouse', 'Tastatura']

vanzari = []

for zi in range(num_zile):
    num_produse_zi = np.random.randint(5, 16)  # numar aleatoriu de produse vandute pe zi
    for _ in range(num_produse_zi):
        produs = np.random.choice(produse_disponibile)
        pret = np.random.normal(40, 8)
        pret = max(1, round(pret, 2))
        promotie = False
        if np.random.rand() < 0.3:  # 30% sanse de promotie
            pret = round(pret * 0.8, 2)
            promotie = True
        cantitate = np.random.randint(1, 11)
        vanzari.append({
            'zi': zi + 1,
            'produs': produs,
            'pret': pret,
            'cantitate': cantitate,
            'promotie': promotie
        })

df = pd.DataFrame(vanzari)


df['total_vanzari'] = df['pret'] * df['cantitate']
df['profit'] = df['total_vanzari'] * 0.3  # marja de profit 30%

#grupam pe zi pentru a obtine totalul vanzarilor si profitului zilnic
vanzari_pe_zi = df.groupby('zi').agg({
    'total_vanzari':'sum',
    'profit':'sum'
}).reset_index()

print("Vanzari si profit pe fiecare zi:")
print(vanzari_pe_zi.head(10))  # afisam primele 10 zile

distributie_preturi = df['pret'].value_counts().sort_index()

distributie_cantitati = df['cantitate'].value_counts().sort_index()

print("\nDistributia preturilor:")
print(distributie_preturi.head(10))

print("\nDistributia cantitatilor vandute:")
print(distributie_cantitati.head(10))



#identificam zilele in care au fost promotii
promotii_pe_zi = df[df['promotie'] == True].groupby('zi').agg({
    'pret':'count'
}).reset_index().rename(columns={'pret':'numar_promotii'})

#calculam impactul promotiei asupra preturilor

pret_mediu_promotie = df[df['promotie']==True]['pret'].mean()
pret_mediu_fara_promotie = df[df['promotie']==False]['pret'].mean()

print("\nNumar promotii pe zi (primele 10 zile):")
print(promotii_pe_zi.head(10))
print(f"\nPret mediu cu promotie: {pret_mediu_promotie:.2f}")
print(f"Pret mediu fara promotie: {pret_mediu_fara_promotie:.2f}")

