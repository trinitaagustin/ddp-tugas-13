from Animal import Animal

class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_mamalia(self):
        super().info_animal(),
        print("Ukuran tubuh \t\t\t :", self.ukuran_tubuh,
              "\nJenis kulit \t\t\t :", self.jenis_kulit)
        
domba = Mamalia("Domba", "Tumbuhan", "Darat", "Melahirkan", "Sedang", "Berbulu")
domba.info_mamalia()
print("---------------")

kucing = Mamalia("Kucing", "Daging", "Darat", "Melahirkan", "Kecil", "Berbulu")
kucing.info_mamalia()
print("---------------")

gajah = Mamalia("Gajah", "Tumbuhan", "Darat", "Melahirkan", "Besar", "Sedikit Berbulu")
gajah.info_mamalia()

