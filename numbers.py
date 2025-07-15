int_value = 5
var1 = 2
var2 = 5
var3 = var1 + var2
print("Var3", var3)
print("Var3 type:", type(var3))

char1="tekst"
print("Char1:", char1)
print("Char1 type:", type(char1))

var4 = float(var1) + float(var2)
print("Var4:", var4)
print("Var4 type:", type(var4))
print(f"{var4:.2f}") # Wyświetla var4 z dwoma miejscami po przecinku

float_value = 4.70
complex_value = 1 + 2j
print(int_value)
print(float_value)
print(complex_value)
print("complex_value type:", type(complex_value))

#/konwersja liczby zmiennoprzecinkowej na liczbę całkowitą
f1 = 5.6
f2 = 5.5
f3 = 5.4

i1 = int(f1)
print("i1:",i1)

i2 = int(f2)
print("i2:",i2)

i3 = int(f3)
print("i3:",i3)

#zaokrąglanie liczby zmiennoprzecinkowej round(x)
print("Zaokrąglenie 5.6:",round(f1))
print("Zaokrąglenie 5.5:",round(f2))
print("Zaokrąglenie 5.4:",round(f3))