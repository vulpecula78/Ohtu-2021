class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.aiempi_tulos = 0

    def miinus(self, arvo):
        self.aiempi_tulos = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.aiempi_tulos = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.aiempi_tulos = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.aiempi_tulos = self.tulos
        self.tulos = arvo
