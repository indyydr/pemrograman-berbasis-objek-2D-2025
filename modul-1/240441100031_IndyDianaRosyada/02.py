class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Alamat  : {self.alamat}")
        print("-")

mahasiswa_list = []
for i in range(3):
    print(f"Masukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    jurusan = input("Jurusan: ")
    alamat = input("Alamat: ")
    print()
    
    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    mahasiswa_list.append(mahasiswa)

print("\nData Mahasiswa:")
for mahasiswa in mahasiswa_list:
    mahasiswa.tampilkan_info()