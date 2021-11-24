import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
            self.pankki_mock = Mock()
            self.viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            self.viitegeneraattori_mock.uusi.return_value = 42

            self.varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1 or tuote_id == 2:
                    return 10
                if tuote_id == 3:
                    return 0

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)
                if tuote_id == 2:
                    return Tuote(2, "olut", 3)
                if tuote_id == 3:
                    return Tuote(3, "makkara", 6)

            # otetaan toteutukset käyttöön
            self.varasto_mock.saldo.side_effect = varasto_saldo
            self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
            self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
        
    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)
        
    def test_tilisiirtoa_kutsutaan_oikein_kahdella_eri_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 8)
        
    def test_tilisiirtoa_kutsutaan_oikein_kahdella_samalla_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 6)
        
    def test_tilisiirtoa_kutsutaan_oikein_kun_toinen_tuote_on_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 3)
        
    def test_maksutapahtuma_pyytaa_uuden_viitenumeron(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.viitegeneraattori_mock.uusi.assert_called()        
        
    def test_asioinnin_aloitus_nollaa_edellisen_asioinnin_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 3)
        
    def test_tuote_poistuu_ostoskorista_ja_laskuttaa_oikean_summan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 3)
        
    
