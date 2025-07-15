#Zadanie 1 suma dwoch liczb 
# Inicjalizuj sumę = 0, num1 = 10, num2 = 20 (PROCES)
# Wprowadź liczby (I / O)
# Dodaj je i zapisz wynik w sumie (PROCES)
# Wydrukuj sumę (I / O)

suma = 0 
number1 = 10 
number2 = 20 
suma = number1 + number2
print("Suma:", suma, "\nLiczba pierwsza:", number1, "\nLiczba druga:", number2)

#zachowawczy enterek dla estetyki
print()

# Zadanie 2 Konwersja temperatury z Fahrenhaita na Celcjusza, oraz na Kelvina
# Zainicjalizuj temp w Farh
# Zainicjalizuj temp w Celcjuszach jako nowa zmienna np: temp_cel i przypisz do niej wynik konwersji 
# Zainicjalizuj temp w Kelwinach jako nowa zmienna np: temp_kel i przypisz do niej wynik konwersji

# przelicznik stopni temperatury: 1°F = -17.22°C = 255.93 K
# Fahrenheit na Celsjusz:°C = (°F - 32) * 5/9
# Fahrenheit na Kelwin: K = (°F - 32) * 5/9 + 273.15

temp = 68 
temp_cel = (68 - 32) * (5/9)
temp_kel = (temp_cel) + 273.15
print(temp, "°F =", temp_cel, "°C =", temp_kel, "K")