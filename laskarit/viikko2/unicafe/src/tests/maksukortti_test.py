import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 25.0)
    
    def test_oton_jalkeen_oikea_saldo(self):
        self.maksukortti.ota_rahaa(750)

        self.assertEqual(self.maksukortti.saldo_euroina(), 2.5)
    
    def test_liian_suuri_otto_ei_muuta_saldoa(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_totuusarvo_otolla_oikein_kun_rahaa_riittavasti(self):
        totuusarvo = self.maksukortti.ota_rahaa(750)

        self.assertEqual(totuusarvo, True)
    
    def test_totuusarvo_otolla_oikein_kun_rahaa_ei_riittavasti(self):
        totuusarvo = self.maksukortti.ota_rahaa(1500)

        self.assertEqual(totuusarvo, False)
