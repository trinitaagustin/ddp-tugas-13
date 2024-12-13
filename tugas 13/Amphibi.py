from Animal import Animal

class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal(),
        print("Jenis air \t\t\t :", self.jenis_air,
              "\nBernapas \t\t\t :", self.bernapas)
        
katak = Amphibi("Katak", "Serangga", "Darat dan Air", "Bertelur", "Air Tawar", "Kulit dan Paru-Paru")
katak.info_amphibi()
print("---------------")

salamander = Amphibi("Salamander", "Seranggq", "Darat dan Air", "Bertelur", "Air tawar", "Kulit dan Paru-Paru")
salamander.info_amphibi()
print("---------------")

caecilian = Amphibi("Caecilian", "Cacing", "Darat dan Air", "Bertelur", "Tanah dan air", "Kulit dan Paru-Paru")
caecilian.info_amphibi()
print("---------------")