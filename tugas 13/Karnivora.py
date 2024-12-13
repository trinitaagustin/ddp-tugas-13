from Animal import Animal

class Karnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, taring, keahlian):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.taring = taring
        self.keahlian = keahlian

    def info_karnivora(self):
        super().info_animal(),
        print("Taring \t\t\t\t :", self.taring,
              "\nKeahlian \t\t\t :",  self.keahlian)
        
harimau = Karnivora("Harimau", "Daging", "Darat", "Melahirkan", 10, "Berburu mangsa di malam hari")
harimau.info_karnivora()
print("---------------")

serigala = Karnivora("Serigala", "Daging", "Darat", "Melahirkan", 8, "Berburu dalam kelompok")
serigala.info_karnivora()
print("---------------")

hiu = Karnivora("Hiu", "Ikan", "Air", "Bertelur", 15, "Berburu ikan dengan cepat")
hiu.info_karnivora()
print("---------------")
        