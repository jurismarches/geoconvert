#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Geoconvert."""

import pytest

from geoconvert.convert import zipcode_to_dept_name
from geoconvert.convert import address_to_zipcode
from geoconvert.convert import dept_name_to_zipcode
from geoconvert.convert import country_name_to_id
from geoconvert.convert import region_name_to_id
from geoconvert.convert import capital_name_to_country_id
from geoconvert.address import AddressParser
from geoconvert.utils import reverse_dict


class TestGeoconvert:
    @pytest.mark.parametrize(
        "input_data, expected",
        [
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
            ('97821 Le Port Cedex', '974'),
            ('27006 Évreux Cedex', '27'),
            ('  27006 Évreux Cedex', '27'),
            ('27006', '27'),
            ('Roissy-en-France95700', '95'),
            (' 44200 BP 10720 Nantes cedex', '44'),
            ('a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse', '31'),
            ('a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse', '31'),
            ('a l attention de M. Bon Jean, Avenue des clients bp72152, F - 31020 Toulouse', '31'),
            ('Avenue des clients CS 72152, F - 31020 Toulouse', '31'),
            ('BP 1330, 6503 TARBES Cedex 9, tel. 05.62.54.58.63', None),
            ('Ville de Blanquefort, 12 rue Dupaty B.P. 20117, à l attention de fernanda Edant-33294 Blanquefort.', '33'),
            ('conseil général du Haut-Rhin, 100 avenue d alsace B.P.20351, conseil général du Haut-Rhin-68006 Colmar Cedex', '68'),
            ('Avenue des clients CS 72152, F - 31020 Toulouse', '31'),
            ('Avenue des clients CS72152, F - 31020 Toulouse', '31'),
            ('6503 TARBES Cedex 9, tel. 05.62.54.58.63', None),
            ('97701 Saint-Barthelemy', '971'),
            ('97098 Saint-Barthelemy', '971'),
            ('a l attention de M. Bon Jean, Avenue des client', None),
            ("13 avenue de la porte d'Italie TSA 61371, F - 75621 Paris", '75'),
            ("avenue René Cassin — BP 67190 97801 Saint-Denis Cedex 9", '974'),
            ("M. le maire, hôtel de Ville 97717 Saint-Denis", '974'),
        ],
    )
    def test_address_to_zipcode(self, input_data, expected):
        assert address_to_zipcode(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("121", None),
            ("44000", "loire-atlantique"),
            ("2a", "corse-du-sud"),
            ("2A", "corse-du-sud"),
            ("20A", "corse-du-sud"),
        ],
    )
    def test_zipcode_to_dept_name(self, input_data, expected):
        assert zipcode_to_dept_name(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ('Martinique', '972'),
            ("cotes d'armr", None),
            ("cotes d'armor", '22'),
            (u'Hauts-de-Seine ', '92'),
            (u'H\xe9rault', '34'),
            (u'Seine-Saint-Denis ', '93'),
            (u'Loire', '42'),
            (u'Corse-du-Sud', '20A'),
            (u'', None),
            (u'Vendé?e', '85'),
            (u'Loire Atlanti)que', '44'),
            (u'Yonne', '89'),
            (u'Saint Pierre et Miquelon', '975'),
        ],
    )
    def test_dept_name_to_zipcode(self, input_data, expected):
        assert dept_name_to_zipcode(input_data) == expected

    def test_region_id_to_name(self):
        pass

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ('bourgogne franche comté', '27'),
            ("midi pyrénées", '73'),
            ("grand est", '44'),
            (u'mayotte ', '06'),
            (u'Centre val de Loire', '24'),
            (u'Picardie ', '22'),
            (u'provence alpes côte d\'azur', '93'),
            (u'', None),
            (u'hauts de france', '32'),
            (u'auvergne rhône alpes', '84'),
            (u'nouvelle aquitaine', '75'),
            (u'La guadeloupe, une superbe région', '01'),
            (u'VICE-RECTORAT DE MAYOTTE ( DCS)', '06'),
        ],
    )
    def test_region_name_to_id(self, input_data, expected):
        assert region_name_to_id(input_data) == expected

    def test_region_info_from_id(self):
        pass

    def test_region_info_from_name(self):
        pass

    @pytest.mark.parametrize(
        "input_data, expected",
        [
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
            ("  Côte d’Ivoire ", 'CI'),  # with accent for apostrophe
            ("U.S. Mission Iraq\n\nIraq", 'IQ'),
            ("Pays:France ?".encode('ascii', 'ignore'), 'FR'),
            (",royaume-uni,", 'GB'),
            (u"trinité-et-Tobago", 'TT'),
            ("surinam", 'SR'),
            (u"saint-barthélemy", 'BL'),
            (u"saint-barthélemy", 'BL'),
            ('sint maarten', 'SX'),
            (u'curaçao', 'CW'),
            ("andorre", 'AD'),
            ('bonaire, saint-eustache et saba', 'BQ'),
            ('soudan', 'SD'),
            ('soudan du sud', 'SS'),
            ("PAYS-BRÉSIL", 'BR'),
            (u"Lorem ipsum Libye - LIBYE", 'LY'),
            ("palestine", 'PS'),
            ("Congo (Brazzaville)", 'CG'),
            ("Congo (Kinshasa)", 'CD'),
        ],
    )
    def test_country_name_to_id_fr(self, input_data, expected):
        assert country_name_to_id(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ('Mongolia', 'MN'),
            ('Marocco', 'MA'),
            ('Georgia', 'GE'),
            ('kosovo', 'KO'),
            ('Namibia', 'NA'),
            ('Venezuela', 'VE'),
            ('Armenia', 'AM'),
            ('sweden', 'SE'),
            (u"Knotts Island, NC 27950\n\n27950-0039\nUnited States", 'US'),
            ("721 APS BLDG 3334\nUNIT 3295 \nRamstein Air Base, Non-U.S. 66877 \nGermany ", 'DE'),
            ("Saudi Arabia", 'SA'),
            ("Country execution:nigeria.", 'NG'),
            ("RUSSIA", 'RU'),
            ("PAPUA NEW GUINEA", 'PG'),
            ("guinea-bissau", 'GW'),
            ("netherlands antilles", 'AN'),
            ("netherlands or something", 'NL'),
            (u'curaçao', 'CW'),
            (u'saint barthélemy', 'BL'),
            ('Sudan', 'SD'),
            ('South Sudan', 'SS'),
            ('tanzania', 'TZ'),
            ("united states minor outlying islands", 'UM'),
            ("Lorem ipsum Libya - LIBYA", 'LY'),
            (' Democratic Republic of the Congo', 'CD'),
            ('CONGO, DEM. REPUBLIC', 'CD'),
            ('TIMOR LESTE', 'TL'),
            ('state of palestine', 'PS'),
            ('palestine, state of', 'PS'),
        ],
    )
    def test_country_name_to_id_en(self, input_data, expected):
        assert country_name_to_id(input_data, lang='EN') == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Dänemark", "DK"),
            ("weißrussland", "BY"),
            ("Demokratische Republik Kongo", "CD"),
            ("korea, süd", "KR"),
            ("libanon", "LB"),
            ("são tomé und príncipe", "ST"),
            ("schweden", "SE"),
            ("schweiz", "CH"),
            ("st. vincent und die grenadinen", "VC"),
            ("Korea, Nord", "KP"),
            ("Lorem Ipsum, Bundesstaat Kanada ", "CA"),
            ("   Palästina      ", "PS"),
            ("Bundesstaat, der Palastina", "PS"),
            ("frankreich einstaten", "FR"),
            ("DOMINICA!!", "DM"),
            (u"   Land der Hinrichtung : Deutschland", "DE"),
            ("Dschibuti-Stadt", "DJ"),
            ("elfenbeinküste und ecuador    ", "CI"),
        ],
    )
    def test_country_name_to_id_de(self, input_data, expected):
        assert country_name_to_id(input_data, lang='DE') == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ('bruxelles', 'BE'),
            (u'La ville est Lomé.', 'TG'),
        ],
    )
    def test_capital_name_to_country_id_fr(self, input_data, expected):
        assert capital_name_to_country_id(input_data, lang='FR') == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ('Copenhagen', 'DK'),
            ("bern", "CH"),
            ("The city is ulaanbaatar.", "MN"),
        ],
    )
    def test_capital_name_to_country_id_en(self, input_data, expected):
        assert capital_name_to_country_id(input_data, lang='EN') == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ('Kopenhagen', 'DK'),
            (u'são tomé', 'ST'),
            ("Das stadt ist Ulaanbaatar.", "MN"),
        ],
    )
    def test_capital_name_to_country_id_de(self, input_data, expected):
        assert capital_name_to_country_id(input_data, lang='DE') == expected


class TestAddressParser:

    address_parser = AddressParser()
    data = [
        (u"Chemin du Solarium\n Le Haut Vigneau\n 33175 GRADIGNAN CEDEX 1", '33175', '33'),
        ("Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ", '33175', '33'),
        ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589", '33175', '33'),
        ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX", '33175', '33'),
        ('7 cours Grandval\nBP 414 - 20183 AJACCIO - CEDEX', '20183', '2A'),
        ('20212   Erbajolo', '20212', '2B'),
        ('20223   Solenzara Air', '20223', '2B'),
        ('BP 55342 20223   Solenzara Air', '20223', '2B'),
        ('Chemin du Solarium Le Haut Vigneau 33 175 GRADIGNAN CEDEX', '33175', '33'),
        ('20 223   Solenzara Air', '20223', '2B'),
        ('97821 Le Port Cedex', '97821', '978'),
        ('27006 Évreux Cedex', '27006', '27'),
        ('  27006 Évreux Cedex', '27006', '27'),
        ('27006', '27006', '27'),
        ('Roissy-en-France95700', '95700', '95'),
        (' 44200 BP 10720 Nantes cedex', '44200', '44'),
        ('a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse', '31020', '31'),
        ('a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse', '31020', '31'),
        ('a l attention de M. Bon Jean, Avenue des clients bp72152, F - 31020 Toulouse', '31020', '31'),
        ('Avenue des clients CS 72152, F - 31020 Toulouse', '31020', '31'),
        ('BP 1330, 6503 TARBES Cedex 9, tel. 05.62.54.58.63', '06503', '06'),
        ('Ville de Blanquefort, 12 rue Dupaty B.P. 20117, à l attention de fernanda Edant-33294 Blanquefort.', '33294', '33'),
        ('conseil général du Haut-Rhin, 100 avenue d alsace B.P.20351, conseil général du Haut-Rhin-68006 Colmar Cedex', '68006', '68'),
        ('Avenue des clients CS 72152, F - 31020 Toulouse', '31020', '31'),
        ('Avenue des clients CS72152, F - 31020 Toulouse', '31020', '31'),
        ('6503 TARBES Cedex 9, tel. 05.62.54.58.63', '06503', '06'),
        ('97700 Saint-Barthelemy', '97700', '977'),
        ('Mme Cindy DUMAS, 1500 Bd Lepic - B.P. 348 73103 Aix-les-Bains', '73103', '73'),
        ('Mme Cindy DUMAS, 15000 Bd Lepic - B.P. 348 73103 Aix-les-Bains', '73103', '73'),
        ('Mme Cindy DUMAS, 15000 Bd Lepic - 73103 B.P. 89348 Aix-les-Bains', '73103', '73'),
        ('Mme Cindy DUMAS, 15000 Bd Lepic - 73103 b.p. 89348 Aix-les-Bains', '73103', '73'),
        ('Mme Cindy DUMAS, 15000 Bd Lepic - 73103 bp 89348 Aix-les-Bains', '73103', '73'),
        (u"M. le président Du Conseil Général Du Lot, avenue de l'europe - regourd Cedex 9 46005 Cahors", '46005', '46'),
        (u"M. le maire, place Dr Pierre Esquirol Cedex 9 47916 Agen.", '47916', '47'),
        ("M. Claude Lopez, 44 avenue Saint Lazare Cedex 2 34965 Montpellier", '34965', '34'),
        (u"M. le président, le Forum 3, rue Malakoff Cedex 01 38031 Grenoble", '38031', '38'),
        (u"Samop - mandataire du cg38, les jardins d'entreprises \r\nbâtiment b4 \r\n213 rue de gerland 69007 Lyon", '69007', '69'),
        (u"M. le président, 9, rue Saint Pierre Lentin cs 94117 Cedex 1 45041 Orléans Cedex", '45041', '45'),
        (u"M. le président Du Conseil Général Du Lot, avenue de l'europe - regourd Cedex 9 46005 Cahors", '46005', '46'),
        (u"M. le président, hôtel du Département , rue Gaston Manent B.P. 1324 Cedex 9 65013 Tarbes", '65013', '65'),
        ('a l attention de M. Bon Jean, Avenue des client', None, None),
        (u"SICTOM du Guiers\n27 avenue Pravaz BP66\n38480 - Pont de Beauvoisin ", '38480', '38'),
        (u"SICTOM du Guiers\n27\n avenue Pravaz BP\n\n 66\n38480\n - Pont de Beauvoisin ", '38480', '38'),
        (u"Mlle DAMAGNEZ Julie, place Victor Pauchet pil daa Marchés Publics 80054 Amiens Cedex 1", '80054', '80'),
        (u"CS 17569 80054 Amiens CEDEX 158", '80054', '80'),
        (u"Adresse de test C.S. 17569 80054 Amiens CEDEX 15800", '80054', '80'),
        (u"Adresse de test CS. 17569 80054 Amiens CEDEX 15800", '80054', '80'),
        (u"Adresse de test C.S 17569 80054 Amiens CEDEX 15800", '80054', '80'),
        (u"Adresse de test BP. 17569 80054 Amiens CEDEX 15800", '80054', '80'),
        (u"Adresse de test B.P 17569 80054 Amiens CEDEX 15800", '80054', '80'),
        (u"M. Bonnet Roland, Directeur interdépartemental des routes Centre-Ouest, le Pastel 22 rue des Pénitents Blancs Le Pastel 22 rue des Pénitents Blancs 87032 Limoges Cedex", '87032', '87'),
        (u"Mme del bianco Véronique, Chargée de marché public, service es marchés publics 93130 Noisy-le-Sec", '93130', '93'),
        (u"direction de la Commande Publique, à l'attention de M. le président, 379 rue Hubert Delisle B.P 437 97838 Le Tampon Cedex", '97838', '978'),
        (u"M. le Directeur, Paris Bâtiment 153 93352 Paris", '93352', '93'),
        (u"M. le Directeur, Paris Bâtiment 53 93352 Paris", '93352', '93'),
        (u"M. le Directeur, Paris Bâtiment 3 93352 Paris", '93352', '93'),
        (u"Adresse : CS 72055 56002 Vannes", '56002', '56'),
        (u"Orléans (45)", "45000", "45"),
        (u"Orléans (45000)", "45000", "45"),
        (u"Bourg-en-Bresse (01)", "01000", "01"),
        (u"Bourg-en-Bresse (1)", None, None),
    ]

    @pytest.mark.parametrize("address_string, zipcode, _", data)
    def test_zipcode(self, address_string, zipcode, _):
        """
        Test zipcode detection
        """
        address = self.address_parser.parse(address_string)
        assert address.zipcode == zipcode

    @pytest.mark.parametrize("address_string, _, dept_number", data)
    def test_department(self, address_string, _, dept_number):
        """
        Test department detection
        """
        address = self.address_parser.parse(address_string)
        assert address.get_department() == dept_number


class TestUtils:

    @pytest.mark.parametrize(
        "input_dict, key, expected",
        [
            ({'key': 'value'}, 'value', 'key'),
            ({'key1': 'value1', 'key2': 'value2'}, 'value1', 'key1'),
            ({'key1': 'value1', 'key2': 'value2'}, 'value2', 'key2'),
        ],
    )
    def test_reverse_dict(self, input_dict, key, expected):
        assert reverse_dict(input_dict).get(key) == expected
