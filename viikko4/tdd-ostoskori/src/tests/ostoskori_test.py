import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        olut = Tuote("Olut", 2)
        makkara = Tuote("Makkara", 3)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(makkara)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuote_hintojen_summa(self):
        olut = Tuote("Olut", 2)
        makkara = Tuote("Makkara", 3)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(makkara)

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        olut = Tuote("Olut", 2)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_kahden_tuotteen_hinta(self):
        olut = Tuote("Olut", 2)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)

        self.assertEqual(self.kori.hinta(), 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        olut = Tuote("Olut", 2)
        makkara = Tuote("Makkara", 3)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(makkara)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        olut = Tuote("Olut", 2)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_tuotteen_niminen_ostos_maaraltaan_kaksi(self):
        olut = Tuote("Olut", 2)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)

        ostokset = self.kori.ostokset()[0]

        self.assertEqual(ostokset.tuotteen_nimi(), "Olut")
        self.assertEqual(ostokset.lukumaara(), 2)

    def test_jos_kahdesta_samasta_tuotteesta_poistetaan_toinen_jaa_ostokseen_yksi_tuote(self):
        olut = Tuote("Olut", 2)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)

        self.kori.poista_tuote(olut)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_koriin_lisatty_tuote_poistetaan_niin_kori_on_tyhja(self):
        olut = Tuote("Olut", 2)
        self.kori.lisaa_tuote(olut)

        self.kori.poista_tuote(olut)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)

    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        olut = Tuote("Olut", 2)
        makkara = Tuote("Makkara", 3)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(makkara)
        self.kori.lisaa_tuote(makkara)

        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)
