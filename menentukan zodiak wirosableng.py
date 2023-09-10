list_nama = {
    "A": "PENGEMIS",
    "B": "DEWI",
    "C": "GADIS",
    "D": "IBLIS",
    "E": "PEMANAH",
    "F": "TOPENG",
    "G": "DATUK",
    "H": "PEMETIK",
    "I": "SANG",
    "J": "BUJANG",
    "K": "DEWA",
    "L": "KAKEK",
    "M": "PENCABUT",
    "N": "SI",
    "O": "NYAI",
    "P": "DEWI",
    "Q": "SEPASANG",
    "R": "BAYANGAN",
    "S": "PANGERAN",
    "T": "BAJAK LAUT",
    "U": "BIDADARI",
    "V": "PENDEKAR",
    "W": "PADUKA",
    "X": "SILUMAN",
    "Y": "EYANG",
    "Z": "RADEN",
}

list_tanggal_lahir= ["MUKA", "TONGKAT", "MURKA", "BUNGA", "KEPALAN", "BUDUK", "SINAR", "KUTILANG", "BODONG", "KELINCI", "OMBAK", "NISAN", "GILA", "TAPAK", "KUNYUK",
        "SEGALA", "CAWAT", "NAGA", "KUKU", "PAKU", "PAKU", "CAKAR", "ULAR", "MAUT", "MAUT", "WIRO", "KAPAK", "PUCAT", "GAJAH", "ANGIN", "KANCUT", "BIBIR", "MERAH"]

list_bulan = {
    "1": "BUSUK",
    "2": "ANGET",
    "3": "SABLENG",
    "4": "MAYAT",
    "5": "BELANG",
    "6": "NGOMPOL",
    "7": "ULAR",
    "8": "SAKTI",
    "9": "BAU",
    "10": "BANGKAI",
    "11": "GENDENG",
    "12": "TUAK",
}

nama = input("Nama?")
tanggal = int(input("Lahir Tanggal?"))
bulan = input("Lahir Bulan?")

print()
print("ciaaatttt.....!!")
print("salam pendekar", list_nama[nama[:1]],
      list_tanggal_lahir[tanggal-1], list_bulan[bulan])
