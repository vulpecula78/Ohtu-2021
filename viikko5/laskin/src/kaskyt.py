class Erotus:
    def __init__(self, sovellus, syote):
        self._syote = syote
        self._sovellus = sovellus
        
    def suorita(self):
        syote = int(self._syote())
        self._sovellus.miinus(syote)

class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus
        
    def suorita(self):
        self._sovellus.nollaa()
        
class Summa:
    def __init__(self, sovellus, syote):
        self._syote = syote
        self._sovellus = sovellus
        
    def suorita(self):
        syote = int(self._syote())
        self._sovellus.plus(syote)
        
class Kumoa:
    def __init__(self, sovellus):
        self._sovellus = sovellus
        
    def suorita(self):
        arvo = self._sovellus.aiempi_tulos
        self._sovellus.aseta_arvo(arvo)
        
