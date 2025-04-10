class Kucing:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Umur  : {self.umur} tahun")
        print(f"{self.nama} bersuara 'Meow!'")
        print(f"{self.nama} suka memanjat.")


class Dinosaurus:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Umur  : {self.umur} tahun")
        print(f"{self.nama} berteriak 'ROARRRRRRR!!!'")
        print(f"{self.nama} predator yang ganas!")


class Kelinci:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Umur  : {self.umur} tahun")
        print(f"{self.nama} mengeluarkan suara purring.")
        print(f"{self.nama} melompat dengan lincah.")


kucing = Kucing("Zuzu", "Kucing persia", 2)
dino = Dinosaurus("Lulu", "T-rex", 15)
kelinci = Kelinci("Nunu", "Kelinci Anggora", 3)

hewan_list = [kucing, dino, kelinci]

for hewan in hewan_list:
    hewan.tampilkan_info()
    print("-" * 35)