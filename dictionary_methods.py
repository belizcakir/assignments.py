arabaAudi = {
    "marka" : "Audi",
    "model" : "A5",
    "yil" : 2019,
}
# değerlere erişme

# sonuc = arabaAudi["marka"]
# sonuc =arabaAudi.get("marka")


# sorgulama işlemleri

# sonuc = "marka" in arabaAudi

# sonuc = len(arabaAudi)

# ekleme işlemleri

# arabaAudi["renk"] = "siyah"

# silme işlemleri

# arabaAudi.pop("yil")

# arabaAudi.popitem()  #popitem son elemanı siler

# del arabaAudi["marka"]
# del arabaAudi
# arabaAudi.clear()

# objeyi kopyalama

# araba =arabaAudi.copy()

# araba["marka"] = "mercedes"

# değer güncelleme

arabaAudi.update({
    "marka" : "BMW",
    "renk" : "beyaz"


})

print(arabaAudi)