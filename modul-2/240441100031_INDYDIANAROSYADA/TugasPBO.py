class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.validasi_sks(sks):
            self.kode = kode
            self.nama = nama
            self.sks = sks
        else:
            print(f"SKS tidak Valid")

    @staticmethod
    def validasi_sks(sks):
        return sks == 2 or sks == 3

class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if Mahasiswa.validasi_nim(nim):
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.mata_kuliah = []
            Mahasiswa.jumlah_mahasiswa += 1
        else:
            print(f"NIM tidak Valid")

    def tambah_matkul(self, matkul):
        self.mata_kuliah.append(matkul)

    def tampilkan_info(self):
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for mk in self.mata_kuliah:
            print(f"  - {mk.nama} ({mk.kode}), SKS: {mk.sks}")

    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return len(nim) == 10 and nim.isdigit() and nim[:2] == "23"

class Kampus:
    def __init__(self, nama, alamat):
        if self.validasi_nama(nama):
            self.nama = nama
            self.alamat = alamat
            self.jumlah_mahasiswa = Mahasiswa.total_mahasiswa()
        else:
            print(f"Nama Tidak Valid")

    def info_kampus(self):
        print(f"\nNama Kampus: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Total Mahasiswa: {self.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama(nama):
        return all(char.isalpha() or char.isspace() for char in nama)

daftar_matkul = [
    MataKuliah("MK101", "Matematika", 3),
    MataKuliah("MK102", "Fisika", 3),
    MataKuliah("MK103", "Bahasa Indonesia", 2),
    MataKuliah("MK104", "Pemrograman", 3),
    MataKuliah("MK105", "Basis Data", 3),
    MataKuliah("MK106", "Sistem Operasi", 3),
    MataKuliah("MK107", "Jaringan Komputer", 2),
    MataKuliah("MK108", "Kalkulus", 3)
]

mahasiswa_list = [
    Mahasiswa("Indy", "2352345678", "Informatika"),
    Mahasiswa("Diana", "2312345679", "Sistem Informasi"),
    Mahasiswa("Rosyada", "2312345680", "Teknik Komputer"),
    Mahasiswa("Ana", "2312345681", "Informatika"),
    Mahasiswa("Rosya", "2312345682", "Sistem Informasi"),
    Mahasiswa("Dasya", "2312345683", "Teknik Komputer")
]

for i in range(len(mahasiswa_list)):
    mhs = mahasiswa_list[i]
    if mhs:
        mhs.tambah_matkul(daftar_matkul[i % len(daftar_matkul)])
        mhs.tambah_matkul(daftar_matkul[(i + 1) % len(daftar_matkul)])
        mhs.tambah_matkul(daftar_matkul[(i + 2) % len(daftar_matkul)])
        mhs.tambah_matkul(daftar_matkul[(i + 3) % len(daftar_matkul)])

kampus = Kampus("Universitas Trunojoyo Madura", "Jl. Trunojoyo")

print("\n--- Data Mahasiswa ---")
for mhs in mahasiswa_list:
    if mhs:
        mhs.tampilkan_info()

print("\n--- Data Kampus ---")
if kampus:
    kampus.info_kampus()
    print(f"Nama Kampus Valid: {Kampus.validasi_nama(kampus.nama)}")