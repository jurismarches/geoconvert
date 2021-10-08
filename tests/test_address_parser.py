import pytest

from geoconvert.address import AddressParser


class TestAddressParser:

    address_parser = AddressParser()
    data = [
        (
            u"Chemin du Solarium\n Le Haut Vigneau\n 33175 GRADIGNAN CEDEX 1",
            "33175",
            "33",
        ),
        (
            "Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ",
            "33175",
            "33",
        ),
        (
            "Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589",
            "33175",
            "33",
        ),
        ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX", "33175", "33"),
        ("7 cours Grandval\nBP 414 - 20183 AJACCIO - CEDEX", "20183", "2A"),
        ("20212   Erbajolo", "20212", "2B"),
        ("20223   Solenzara Air", "20223", "2B"),
        ("BP 55342 20223   Solenzara Air", "20223", "2B"),
        ("Chemin du Solarium Le Haut Vigneau 33 175 GRADIGNAN CEDEX", "33175", "33"),
        ("20 223   Solenzara Air", "20223", "2B"),
        ("97821 Le Port Cedex", "97821", "978"),
        ("27006 Évreux Cedex", "27006", "27"),
        ("  27006 Évreux Cedex", "27006", "27"),
        ("27006", "27006", "27"),
        ("Roissy-en-France95700", "95700", "95"),
        (" 44200 BP 10720 Nantes cedex", "44200", "44"),
        (
            "a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse",
            "31020",
            "31",
        ),
        (
            "a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse",
            "31020",
            "31",
        ),
        (
            "a l attention de M. Bon Jean, Avenue des clients bp72152, F - 31020 Toulouse",
            "31020",
            "31",
        ),
        ("Avenue des clients CS 72152, F - 31020 Toulouse", "31020", "31"),
        ("BP 1330, 6503 TARBES Cedex 9, tel. 05.62.54.58.63", "06503", "06"),
        (
            "Ville de Blanquefort, 12 rue Dupaty B.P. 20117, à l attention de fernanda Edant-33294 Blanquefort.",
            "33294",
            "33",
        ),
        (
            "conseil général du Haut-Rhin, 100 avenue d alsace B.P.20351, conseil général du Haut-Rhin-68006 Colmar Cedex",
            "68006",
            "68",
        ),
        ("Avenue des clients CS 72152, F - 31020 Toulouse", "31020", "31"),
        ("Avenue des clients CS72152, F - 31020 Toulouse", "31020", "31"),
        ("6503 TARBES Cedex 9, tel. 05.62.54.58.63", "06503", "06"),
        ("97700 Saint-Barthelemy", "97700", "977"),
        (
            "Mme Cindy DUMAS, 1500 Bd Lepic - B.P. 348 73103 Aix-les-Bains",
            "73103",
            "73",
        ),
        (
            "Mme Cindy DUMAS, 15000 Bd Lepic - B.P. 348 73103 Aix-les-Bains",
            "73103",
            "73",
        ),
        (
            "Mme Cindy DUMAS, 15000 Bd Lepic - 73103 B.P. 89348 Aix-les-Bains",
            "73103",
            "73",
        ),
        (
            "Mme Cindy DUMAS, 15000 Bd Lepic - 73103 b.p. 89348 Aix-les-Bains",
            "73103",
            "73",
        ),
        (
            "Mme Cindy DUMAS, 15000 Bd Lepic - 73103 bp 89348 Aix-les-Bains",
            "73103",
            "73",
        ),
        (
            u"M. le président Du Conseil Général Du Lot, avenue de l'europe - regourd Cedex 9 46005 Cahors",
            "46005",
            "46",
        ),
        (u"M. le maire, place Dr Pierre Esquirol Cedex 9 47916 Agen.", "47916", "47"),
        (
            "M. Claude Lopez, 44 avenue Saint Lazare Cedex 2 34965 Montpellier",
            "34965",
            "34",
        ),
        (
            u"M. le président, le Forum 3, rue Malakoff Cedex 01 38031 Grenoble",
            "38031",
            "38",
        ),
        (
            u"Samop - mandataire du cg38, les jardins d'entreprises \r\nbâtiment b4 \r\n213 rue de gerland 69007 Lyon",
            "69007",
            "69",
        ),
        (
            u"M. le président, 9, rue Saint Pierre Lentin cs 94117 Cedex 1 45041 Orléans Cedex",
            "45041",
            "45",
        ),
        (
            u"M. le président Du Conseil Général Du Lot, avenue de l'europe - regourd Cedex 9 46005 Cahors",
            "46005",
            "46",
        ),
        (
            u"M. le président, hôtel du Département , rue Gaston Manent B.P. 1324 Cedex 9 65013 Tarbes",
            "65013",
            "65",
        ),
        ("a l attention de M. Bon Jean, Avenue des client", None, None),
        (
            u"SICTOM du Guiers\n27 avenue Pravaz BP66\n38480 - Pont de Beauvoisin ",
            "38480",
            "38",
        ),
        (
            u"SICTOM du Guiers\n27\n avenue Pravaz BP\n\n 66\n38480\n - Pont de Beauvoisin ",
            "38480",
            "38",
        ),
        (
            u"Mlle DAMAGNEZ Julie, place Victor Pauchet pil daa Marchés Publics 80054 Amiens Cedex 1",
            "80054",
            "80",
        ),
        (u"CS 17569 80054 Amiens CEDEX 158", "80054", "80"),
        (u"Adresse de test C.S. 17569 80054 Amiens CEDEX 15800", "80054", "80"),
        (u"Adresse de test CS. 17569 80054 Amiens CEDEX 15800", "80054", "80"),
        (u"Adresse de test C.S 17569 80054 Amiens CEDEX 15800", "80054", "80"),
        (u"Adresse de test BP. 17569 80054 Amiens CEDEX 15800", "80054", "80"),
        (u"Adresse de test B.P 17569 80054 Amiens CEDEX 15800", "80054", "80"),
        (
            u"M. Bonnet Roland, Directeur interdépartemental des routes Centre-Ouest, le Pastel 22 rue des Pénitents Blancs Le Pastel 22 rue des Pénitents Blancs 87032 Limoges Cedex",
            "87032",
            "87",
        ),
        (
            u"Mme del bianco Véronique, Chargée de marché public, service es marchés publics 93130 Noisy-le-Sec",
            "93130",
            "93",
        ),
        (
            u"direction de la Commande Publique, à l'attention de M. le président, 379 rue Hubert Delisle B.P 437 97838 Le Tampon Cedex",
            "97838",
            "978",
        ),
        (u"M. le Directeur, Paris Bâtiment 153 93352 Paris", "93352", "93"),
        (u"M. le Directeur, Paris Bâtiment 53 93352 Paris", "93352", "93"),
        (u"M. le Directeur, Paris Bâtiment 3 93352 Paris", "93352", "93"),
        (u"Adresse : CS 72055 56002 Vannes", "56002", "56"),
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
