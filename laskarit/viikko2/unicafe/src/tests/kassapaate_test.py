import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_kassan_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_myytyja_lounaita_oikea_maara(self):
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 0)
    
    ### EDULLISET KÄTEISOSTOT ###
    
    def test_syo_edullisesti_kateisella_nostaa_saldoa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_syo_edullisesti_kateisella_nostaa_saldoa_oikein_kun_tasaraha(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_syo_edullisesti_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(vaihtoraha, 260)
    
    def test_syo_edullisesti_vaihtoraha_oikein_kun_tasaraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(vaihtoraha, 0)
    
    def test_syo_edullisesti_kateisella_nostaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 1)

    def test_syo_edullisesti_kateisella_nostaa_lounaiden_maaraa_kun_tasaraha(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 1)

    def test_syo_edullisesti_kateisella_ei_muuta_saldoa_kun_maksu_liian_pieni(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_syo_edullisesti_kateisella_ei_muuta_lounaiden_maaraa_kun_maksu_liian_pieni(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 0)
    
    def test_syo_edullisesti_vaihtoraha_oikein_kun_maksu_liian_pieni(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(vaihtoraha, 100)

    ### MAUKKAAT KÄTEISOSTOT ###

    def test_syo_maukkaasti_kateisella_nostaa_saldoa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_syo_maukkaasti_kateisella_nostaa_saldoa_oikein_kun_tasaraha(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
    
    def test_syo_maukkaasti_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(vaihtoraha, 100)
    
    def test_syo_maukkaasti_vaihtoraha_oikein_kun_tasaraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(vaihtoraha, 0)
    
    def test_syo_maukkaasti_kateisella_nostaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 1)

    def test_syo_maukkaasti_kateisella_nostaa_lounaiden_maaraa_kun_tasaraha(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 1)

    def test_syo_maukkaasti_kateisella_ei_muuta_saldoa_kun_maksu_liian_pieni(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_syo_maukkaasti_kateisella_ei_muuta_lounaiden_maaraa_kun_maksu_liian_pieni(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 0)
    
    def test_syo_maukkaasti_vaihtoraha_oikein_kun_maksu_liian_pieni(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(vaihtoraha, 100)
    
    ### EDULLISET KORTTIOSTOT ###

    def test_totuusarvo_syo_edullisesti_kortilla_kun_osto_onnistuu(self):
        totuusarvo = self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(totuusarvo, True)

    def test_totuusarvo_syo_edullisesti_kortilla_kun_osto_epaonnistuu(self):
        kortti = Maksukortti(100)
        totuusarvo = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(totuusarvo, False)
    
    def test_syo_edullisesti_kortilla_kortin_saldo_muuttuu_kun_osto_onnistuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo_euroina(), 7.60)
    
    def test_syo_edullisesti_kortilla_kortin_saldo_ei_muutu_kun_osto_epaonnistuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 1.0)
    
    def test_syo_edullisesti_kortilla_muuttaa_lounaiden_maaraa_kun_osto_onnistuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 1)
    
    def test_syo_edullisesti_kortilla_ei_muuta_lounaiden_maaraa_kun_osto_epaonnistuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 0)
    
    def test_kassan_saldo_ei_muutu_kun_syo_edullisesti_maksu_onnistuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassan_saldo_ei_muutu_kun_syo_edullisesti_maksu_epaonnistuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    ### MAUKKAAT KORTTIOSTOT ###

    def test_totuusarvo_syo_maukkaasti_kortilla_kun_osto_onnistuu(self):
        totuusarvo = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(totuusarvo, True)

    def test_totuusarvo_syo_maukkaasti_kortilla_kun_osto_epaonnistuu(self):
        kortti = Maksukortti(100)
        totuusarvo = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(totuusarvo, False)
    
    def test_syo_maukkaasti_kortilla_kortin_saldo_muuttuu_kun_osto_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo_euroina(), 6.0)
    
    def test_syo_maukkaasti_kortilla_kortin_saldo_ei_muutu_kun_osto_epaonnistuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 1.0)
    
    def test_syo_maukkaasti_kortilla_muuttaa_lounaiden_maaraa_kun_osto_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 1)
    
    def test_syo_maukkaasti_kortilla_ei_muuta_lounaiden_maaraa_kun_osto_epaonnistuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 0)
    
    def test_kassan_saldo_ei_muutu_kun_syo_maukkaasti_maksu_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassan_saldo_ei_muutu_kun_syo_maukkaasti_maksu_epaonnistuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    ### KORTIN LATAUS ###

    def test_kortin_lataus_nostaa_kortin_saldoa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1500)

        self.assertEqual(self.kortti.saldo_euroina(), 25.0)
    
    def test_kortin_lataus_nostaa_kassan_saldoa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1015.0)
    
    def test_negatiivinen_summa_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1500)

        self.assertEqual(self.kortti.saldo_euroina(), 10.0)

    def test_negatiivinen_summa_ei_muuta_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)