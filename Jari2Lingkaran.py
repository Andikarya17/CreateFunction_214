import math

# Fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: 3.14 * r ** 2

# Contoh penggunaan:
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
print(f"Luas lingkaran adalah: {luas_lingkaran(jari_jari):.2f}")
