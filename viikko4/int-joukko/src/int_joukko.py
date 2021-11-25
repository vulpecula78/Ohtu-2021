
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.ljono:
            return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

    def poista(self, luku):
        for i in range(0, self.alkioiden_lkm):
            if luku == self.ljono[i]:
                self.ljono.pop(i) 
                self.alkioiden_lkm -= 1
                break

    def kopioi_taulukko(self, taulu_a, taulu_b):
        for i in range(0, len(taulu_a)):
            taulu_b[i] = taulu_a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = []
        for i in range(0, self.alkioiden_lkm):
            taulu.append(self.ljono[i])
        return taulu

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste = IntJoukko()
        yhdistettavat = joukko_a.to_int_list() + joukko_b.to_int_list()

        for luku in yhdistettavat:
            yhdiste.lisaa(luku)
        return yhdiste

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()
        
        for luku in a_taulu:
            if luku in b_taulu:
                leikkaus.lisaa(luku)
        return leikkaus

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()
        
        for luku in a_taulu:
            if luku not in b_taulu:
                erotus.lisaa(luku)
        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i]) + ", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1]) + "}"
            return tuotos
