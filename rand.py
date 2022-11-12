tablica = "zwykly,, tekst ,,  zwykly tekst"

print(tablica[0])
print(tablica.split(","))
print(tablica[:-1])
print(tablica.replace(',,',','))


kolekcja=['a','b','c','d']
for i in range(len(kolekcja)):
	if i == 2:
		kolekcja[i]="tekst"

print(kolekcja)


zero=["  xx  ",
      " x  x ",
      "x    x",
      "x    x",
      "x    x",
      " x  x ",
      "  xx  "]

jeden=["   xx ",
       "  xxx ",
       " x xx ",
       "   xx ",
       "   xx ",
       "   xx ",
       " xxxxx"]

a = input("podaj liczbę:")

for i in range(len(a)):
    if a[i] == "1": 
        tekst_do_wypisania+=jeden[j]


for i in range(7):
    tekst_do_wypisania=zero[i]+" "+jeden[i]
    print(tekst_do_wypisania)