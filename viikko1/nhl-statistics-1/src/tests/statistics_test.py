import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),    #5
            Player("Lemieux", "PIT", 45, 54),   #2
            Player("Kurri", "EDM", 37, 53),     #4
            Player("Yzerman", "DET", 42, 56),   #3
            Player("Gretzky", "EDM", 35, 89)    #top scorer
        ]
    
class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
       
    def test_loytaa_pelaajan_listalta(self):
        pl = self.statistics.search("Kurri")
        self.assertIn("Kurri", str(pl))
        
    def test_pelaajaa_ei_loydy(self):
        pl = self.statistics.search("Kekkonen")
        self.assertEqual(None, pl)
        
    def test_palauttaa_vain_halutun_joukkueen_pelaajat(self):
        team = self.statistics.team("EDM")
        for i in team:
            self.assertIn("EDM", str(i))
            
    def test_listaa_pelaajat_pisteiden_mukaan(self):
        top_list = self.statistics.top_scorers(4)
        pl = [str(i) for i in top_list]
        self.assertIn("Gretzky", pl[0])
        self.assertIn("Yzerman", pl[2])
        self.assertIn("Semenko", pl[4])
