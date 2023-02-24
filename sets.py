# sets => indekslenemez, sıralanamaz

markalar = {"Audi","Mercedes","Bmw","Honda"}
markalar2 = {"Renault", "Toyota", "Mazda"}
# sonuc = markalar[0]

#sorgulama 

sonuc="Bmw" in markalar


markalar.add("Opel")
markalar.update(["Toyota","Scoda"])

# sonuc = len(markalar)

# markalar.remove("Opel")

# sonuc = markalar.pop()

# markalar.clear()

sonuc= markalar.union(markalar2)

print(sonuc)