from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.sisalto = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self.sisalto:
            tavaroita += ostos.lukumaara()
        return tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.sisalto:
            summa += ostos.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.sisalto:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        ostos = Ostos(lisattava)
        self.sisalto.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.sisalto:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.sisalto.remove(ostos)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.sisalto
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
