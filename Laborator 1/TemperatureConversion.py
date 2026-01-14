try:
        celsius = float(input("Introdu temperatura in grade Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(f"Temperatura in Fahrenheit este: {fahrenheit:.2f}")

except ValueError:
        print("Eroare: Introdu o valoare numerica valida.")