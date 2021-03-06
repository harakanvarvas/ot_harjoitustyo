import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_edullisia_myyty(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_maukkaita_myyty(self):
        self.assertEqual(str(self.kassapaate.maukkaat), "0")


    def test_kateisosto_toimii_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_kateisosto_edullinen_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_kateisosto_toimii_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_kateisosto_maukkaat_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_korttiosto_toimii_edulliset(self):
        self.kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.edulliset), "1")
        return True

    def test_korttiosto_edullinen_kortilla_ei_tarpeeksi_rahaa(self):
        self.kortti = Maksukortti(0)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        return False

    def test_korttiosto_toimii_maukkaat(self):
        self.kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
        return True

    def test_korttiosto_maukas_kortilla_ei_tarpeeksi_rahaa(self):
        self.kortti = Maksukortti(0)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        return False

    def test_ladataan_kortille_rahaa(self):
        self.kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "101000")
        self.assertEqual(str(self.kortti.saldo), "1000")

    def test_kortille_ei_voi_ladata_negatiivista_rahaa(self):
        self.kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kortti.saldo), "0")
