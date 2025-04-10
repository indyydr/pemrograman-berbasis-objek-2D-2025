class Manusia:

    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama}, {self.umur} tahun, tinggal di {self.alamat}, sedang berjalan.")

    def berlari(self):
        print(f"{self.nama}, {self.umur} tahun, tinggal di {self.alamat}, sedang berlari.")


Manusia1 = Manusia("Indy", 19, "Surabaya")
Manusia2 = Manusia("Diana", 15, "Malang")
Manusia3 = Manusia("Rosyada", 20, "Jakarta")
Manusia4 = Manusia("Mawar", 30, "Bandung")
Manusia5 = Manusia("Tarzan", 23, "Hutan")

Manusia1.berjalan()
Manusia2.berlari()
Manusia3.berjalan()
Manusia4.berlari()
Manusia5.berjalan()