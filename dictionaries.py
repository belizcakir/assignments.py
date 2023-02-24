
# # 34 => İstanbul
# # 35 => İzmir

# sehirler = ["İstanbul", "İzmir"]
# plakalar = [34,35]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(sehirler.index("İstanbul"))
# print(plakalar[sehirler.index("İstanbul")])
# print(plakalar[sehirler.index("İzmir")])

# key - value

# plakalar ={"İzmir": 35, "İstanbul": 34}

# print(plakalar["İzmir"])
# print(plakalar["İstanbul"])

# plakalar["Eskişehir"] = 26
# plakalar["Bursa"] = 14
# print(plakalar)

urunler = {
    100: {
        "urunadi" : "Monitör",
        "urunAciklamasi" : "16 inç",
        "garantiSuresi" : 3,
        "fiyati" : 800,
    },
        101: {
        "urunadi" : "SSD",
        "urunAciklamasi" : "256 GB",
        "garantiSuresi" : 2,
        "fiyati" : 1500,
    }
}

sonuc = urunler[100]["urunadi"]
print(sonuc)



