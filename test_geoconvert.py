#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Geoconvert."""

import unittest

from geoconvert.convert import zipcode_to_dept_name
from geoconvert.convert import address_to_zipcode
from geoconvert.convert import dept_name_to_zipcode
from geoconvert.convert import region_id_to_name
from geoconvert.convert import region_name_to_id
from geoconvert.convert import country_name_to_id


class GeoconvertTestCase(unittest.TestCase):
    def test_zipcode_to_dept_name(self):
        self.assertEqual(zipcode_to_dept_name('121'), None)
        self.assertEqual(zipcode_to_dept_name('44000'), 'loire-atlantique')
        self.assertEqual(zipcode_to_dept_name('2a'), 'corse-du-sud')
        self.assertEqual(zipcode_to_dept_name('2A'), 'corse-du-sud')
        self.assertEqual(zipcode_to_dept_name('20A'), 'corse-du-sud')

    def test_address_to_zipcode(self):
        data = [
            (u"Chemin du Solarium\\n Le Haut Vigneau\\n 33175 GRADIGNAN CEDEX", '33'),
            ("Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ", '33'),
            ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589", '33'),
            ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX", '33'),
            ('7 cours Grandval\\nBP 414 - 20183 AJACCIO - CEDEX', '20A'),
            ('20212   Erbajolo', '20B'),
            ('20223   Solenzara Air', '20A'),
            ('BP 55342 20223   Solenzara Air', '20A'),
            ('Chemin du Solarium Le Haut Vigneau 33 175 GRADIGNAN CEDEX', '33'),
            ('20 223   Solenzara Air', '20A'),
            ('97821 Le Port Cedex', '971'),
            ('27006 Évreux Cedex', '27'),
            ('  27006 Évreux Cedex', '27'),
            ('27006', '27'),
            ('Roissy-en-France95700', '95'),
            (' 44200 BP 10720 Nantes cedex', '44'),
            ('a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse', '31'),
            ('a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse', '31'),
            ('a l attention de M. Bon Jean, Avenue des clients bp72152, F - 31020 Toulouse', '31'),
            ('Avenue des clients CS 72152, F - 31020 Toulouse', '31'),
            ('BP 1330, 6503 TARBES Cedex 9, tel. 05.62.54.58.63', '06'),
            ('06503 TARBES Cedex 9, tel. 05.62.54.58.63', '06'),
            ('Ville de Blanquefort, 12 rue Dupaty B.P. 20117, à l attention de fernanda Edant-33294 Blanquefort.', '33'),
            ('Ville de Blanquefort, 12 rue Dupaty B.P.20117, à l attention de fernanda Edant-33294 Blanquefort.', '33'),
            ('conseil général du Haut-Rhin, 100 avenue d alsace B.P. 20351, conseil général du Haut-Rhin-68006 Colmar Cedex', '68'),
            ('conseil général du Haut-Rhin, 100 avenue d alsace B.P.20351, conseil général du Haut-Rhin-68006 Colmar Cedex', '68'),
            ('Avenue des clients CS 72152, F - 31020 Toulouse', '31'),
            ('Avenue des clients CS72152, F - 31020 Toulouse', '31'),
            ('6503 TARBES Cedex 9, tel. 05.62.54.58.63', '06'),
            ('97700 Saint-Barthelemy', '974'),
            ('a l attention de M. Bon Jean, Avenue des client', None)
        ]

        for test in data:
            self.assertEqual(address_to_zipcode(test[0]), test[1])

    def test_dept_name_to_zipcode(self):
        data = [
            ('Martinique', '972'),
            ("cotes d'armr", None),
            ("cotes d'armor", '22'),
            (u'Hauts-de-Seine ', '92'),
            (u'H\xe9rault', '34'),
            (u'Seine-Saint-Denis ', '93'),
            (u'Loire', '42'),
            (u'Corse-du-Sud', '20A'),
            (u'', None),
            (u'Yonne', '89'),
            (u'Saint Pierre et Miquelon', '975')]
        for test in data:
            self.assertEqual(dept_name_to_zipcode(test[0]), test[1])

    def test_region_id_to_name(self):
        pass

    def test_region_name_to_id(self):
        pass

    def test_region_info_from_id(self):
        pass

    def test_region_info_from_name(self):
        pass

    def test_country_name_to_id_fr(self):
        data = [
            ('france', 'FR'),
            ('Comores', 'KM'),
            ('Madagascar', 'MG'),
            (u'S\xe9n\xe9gal', 'SN'),
            ('République démocratique du Congo', 'CD'),
            ('Mali', 'ML'),
            ('Sri Lanka ', 'LK'),
            (u'\xa0V\xe9n\xe9zuela\xa0', 'VE'),
            (u'Vi\xeatnam', 'VN'),
            ('Nigeria', 'NG'),
            (u'Niger', 'NE'),
            (u'aaa ( bbb', None),
            (u" Le  nigéria c'est trop   sympa", 'NG'),
            (u"Pays d'exécution : Niger", 'NE'),
            ("  Côte d'Ivoire ", 'CI'),
            ("U.S. Mission Iraq\n\nIraq", 'IQ'),
            ("Pays:France ?".encode('ascii', 'ignore'), 'FR'),
            (",royaume-uni,", 'GB'),
            ("PAYS-BRÉSIL", 'BR')]
        for test in data:
            self.assertEqual(country_name_to_id(test[0]), test[1])

    def test_country_name_to_id_en(self):
        data = [
            ('Mongolia', 'MN'),
            ('Marocco', 'MA'),
            ('Georgia', 'GE'),
            ('Namibia', 'NA'),
            ('Venezuela', 'VE'),
            ('Armenia', 'AM'),
            ('sweden', 'SE'),
            (u"Knotts Island, NC 27950\n\n27950-0039\nUnited States", 'US'),
            ("721 APS BLDG 3334\nUNIT 3295 \nRamstein Air Base, Non-U.S. 66877 \nGermany ", 'DE'),
            ("Saudi Arabia", 'SA'),
            ("Country execution:nigeria.", 'NG')]
        for test in data:
            self.assertEqual(country_name_to_id(test[0], lang='EN'), test[1])

if __name__ == '__main__':
    unittest.main()