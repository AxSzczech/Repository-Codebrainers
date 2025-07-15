d = {}

# klucz (key)
# wartość (value)
# k:v - element słownika (item)

d = {"imię": "Jan",
      "nazwisko": "Kowalski",
        "telefon": 123123123
        }
print("Słownik", d)
print("Słownik - klucze", d.keys())
print("Słownik - wartości", d.values())
print("Słownik items", d.items())

# Wyjmujemy wartosc ze slownika bazujac na kluczu 
example = 'imię'
print("Pierwsza wartosc ze slownika", d["imię"])
print("Pierwsza wartosc ze slownika", d[example])