class PersegiPanjang:
    # Konstruktor untuk menginisialisasi panjang dan lebar
    def __init__(self, panjang, lebar):
        self.panjang = panjang  # Menyimpan nilai panjang
        self.lebar = lebar      # Menyimpan nilai lebar

    # Metode untuk menghitung keliling
    def keliling(self):
        return (self.panjang + self.lebar) * 2  # Menghitung keliling

    # Metode untuk menghitung luas
    def luas(self):
        return self.panjang * self.lebar  # Menghitung luas

    # Metode untuk mengembalikan representasi string dari objek
    def __str__(self):
        return f"Panjangnya {self.panjang} cm, dan Lebarnya {self.lebar} cm"

# Blok untuk menangani input dari pengguna
try:
    panjang = float(input("Masukkan panjang = "))  # Mengambil input panjang
    lebar = float(input("Masukkan lebar = "))      # Mengambil input lebar

    # Validasi input untuk memastikan nilai positif
    if panjang <= 0 or lebar <= 0:
        print("Nilainya harus positif yah")  # Pesan kesalahan jika input tidak valid
    else:
        # Membuat objek persegi panjang jika input valid
        persegi_panjang = PersegiPanjang(panjang, lebar)
        print(persegi_panjang)  # Mencetak informasi objek
        print("Keliling = ", persegi_panjang.keliling(), "cm")  # Mencetak keliling
        print("Luas = ", persegi_panjang.luas(), "cm^2")  # Mencetak luas

# Menangani kesalahan jika input tidak dapat dikonversi menjadi float
except ValueError:
    print("Error: Input harus berupa angka.")  # Pesan kesalahan untuk input yang tidak valid