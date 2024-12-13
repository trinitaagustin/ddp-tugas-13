#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

class Animal:
    def __init__(self, name, makananan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makananan
        self.hidup = hidup
        self.berkembang = berkembang_biak

    def info_animal(self):
        print( "Nama Hewan \t\t\t :", self.name,
              "\nMakanan \t\t\t : ", self.makanan,
              "\nHidup \t\t\t\t : ", self.hidup,
              "\nBerkembang Biak \t\t : ", self.berkembang)


#hewan = Animal("Kucing", "Daging", "Darat", "Mengandung")
#hewan.info_animal()

