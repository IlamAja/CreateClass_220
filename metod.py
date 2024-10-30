class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

panjang = float(input("Masukkan panjang (cm): "))
lebar = float(input("Masukkan lebar (cm): "))

persegi_panjang = PersegiPanjang(panjang, lebar)

print(persegi_panjang)
print("Keliling:", persegi_panjang.keliling(), "cm")
print("Luas:", persegi_panjang.luas(), "cm²")
