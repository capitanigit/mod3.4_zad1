#Mod 3 Zad 1
print("Mod 3 zad 1") 
print()
d = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"],
    }
suma = 0
for k in d:
    temp = [v.capitalize() for v in d[k]]
    print(f"Idę do {k.capitalize()} kupię tu naspępujące rzeczy {temp}")
    suma = suma + len(d[k])   
print(f"W sumie kupuję {suma} produktów")
print()
print("commit1")
print("commit2")
print("pozdrowienia dla Mentora ;]")