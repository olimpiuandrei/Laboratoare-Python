import pandas as pd

#crearea unui fisier CSV cu date de vanzari
date_vanzari = {
    'produs': ['Laptop', 'Telefon', 'Laptop', 'Casti', 'Telefon', 'Laptop', 'Casti', 'Laptop', 'Telefon', 'Casti'],
    'cantitate vanduta': [5, 10, 3, 20, 5, 2, 15, 7, 8, 25],
    'pret': [3500, 1500, 3500, 200, 1500, 3500, 200, 3500, 1500, 200],
    'data vanzarii': ['02.01.2024','03.01.2024','15.01.2024','20.01.2024','10.02.2024',
                      '12.02.2024','18.02.2024','05.03.2024','12.03.2024','22.03.2024']
}

# transformam datele intr-un DataFrame
df = pd.DataFrame(date_vanzari)

# salvam DataFrame-ul ca fisier CSV in acelasi folder cu scriptul
df.to_csv('vanzari.csv', index=False)

#incarcarea CSV
df = pd.read_csv('vanzari.csv')

#conversia coloanei
df['data vanzarii'] = pd.to_datetime(df['data vanzarii'], dayfirst=True)

df['venit'] = df['cantitate vanduta'] * df['pret']

#adaugarea unei coloane
df['an_luna'] = df['data vanzarii'].dt.to_period('M')

#cele mai vandute produse pe luna
vanzari_luna = df.groupby(['an_luna', 'produs'])['cantitate vanduta'].sum().reset_index()
vanzari_luna = vanzari_luna.sort_values(['an_luna', 'cantitate vanduta'], ascending=[True, False])
print("Cele mai vandute produse pe luna:")
print(vanzari_luna)

#venitul total pe fiecare produs
venit_total_produs = df.groupby('produs')['venit'].sum().reset_index()
venit_total_produs = venit_total_produs.sort_values('venit', ascending=False)
print("\nVenitul total pe fiecare produs:")
print(venit_total_produs)

#filtrarea vanzarilor intre doua date
start_date = '2024-01-01'
end_date = '2024-03-31'
df_filtrat = df[(df['data vanzarii'] >= start_date) & (df['data vanzarii'] <= end_date)]
print(f"\nVanzarile intre {start_date} si {end_date}:")
print(df_filtrat)

#venitul mediu lunar
venit_mediu_lunar = df.groupby('an_luna')['venit'].mean().reset_index()
print("\nVenitul mediu lunar:")
print(venit_mediu_lunar)
