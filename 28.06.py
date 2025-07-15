# Biorąc pod uwagę ciąg o nieparzystej długości większej niż 7,
# zwróć łańcuch złożony z trzech środkowych znaków danego ciągu:
# Dane wejściowe:
#     `str1 = "Datatypes"`
# Oczekiwany wynik:\
#     `aty`

print("#1")
str1 = 'Datatypes'
print(str1[3:6])

print("#2")
str2 = 'Datatypes'
srodek = int(len(str1)/2)
print(str1[(srodek - 1):srodek+ 2])

print(str1.isalpha())
print(str2.isalpha())