from tuomari import Tuomari

class KPS:        
    def pelaa(self):        
        tuomari = Tuomari()
        
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
             tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
             print(tuomari)

             ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
             tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)
        
    
    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
