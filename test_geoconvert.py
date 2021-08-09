#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Geoconvert."""

import pytest

from geoconvert.address import AddressParser
from geoconvert.convert import (
    address_to_country_and_subdivision_codes,
    address_to_country_code,
    address_to_subdivision_code,
    address_to_zipcode,
    ca_address_to_province_code,
    ca_postcode_to_province_code,
    ca_province_name_to_province_code,
    capital_name_to_country_code,
    capital_name_to_country_id,
    country_name_to_country_code,
    country_name_to_id,
    dept_name_to_zipcode,
    fr_address_to_dept_code,
    fr_dept_name_to_dept_code,
    fr_postcode_to_dept_code,
    fr_region_id_to_info,
    fr_region_name_to_id,
    fr_region_name_to_info,
    language_to_capital_names,
    language_to_country_names,
    region_info_from_id,
    region_info_from_name,
    region_name_to_id,
    us_address_to_state_code,
    us_postcode_to_state_code,
)
from geoconvert.utils import safe_string


class TestGeoconvert:
    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Toronto, Ontario", "ON"),
            ("Québec", "QC"),
            ("Terre-Neuve-et-Labrador", "NL"),
            ("1575 Av. Gatineau, H3T 1X6, Montréal", "QC"),
            ("Bldg 158, Iqaluit, NU X0A 0H0, Canada", "NU"),
            ("52-58 Franklin Rd, Inuvik, NT X0E 0T0, Canada", "NT"),
            ("Toronto, ON", "ON"),
            ("Newcastle upon Tyne", None),
            ("Onalaska, WI", None),
            (
                """15910 Hermosa avenue updated,Bldg 1,Central Research Park
Sunnyvale , CA 94085
United States""",
                None,
            ),
            # Detection via province code should be case-sensitive
            ("On a faim!", None),
            ("This is Toronto, ON", "ON"),
        ],
    )
    def test_ca_address_to_province_code(self, input_data, expected):
        assert ca_address_to_province_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("1575 Av. Gatineau, H3T 1X6, Montréal", "QC"),
            ("Bldg 158, Iqaluit, NU X0A 0H0, Canada", "NU"),
            ("52-58 Franklin Rd, Inuvik, NT X0E 0T0, Canada", "NT"),
            ("Toronto, ON", None),
            ("Newcastle upon Tyne", None),
            ("Onalaska, WI", None),
        ],
    )
    def test_ca_postcode_to_province_code(self, input_data, expected):
        assert ca_postcode_to_province_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Toronto, Ontario", "ON"),
            ("Newcastle upon Tyne", None),
            ("Onalaska, WI", None),
            ("Montréal, Québec", "QC"),
        ],
    )
    def test_ca_province_name_to_province_code(self, input_data, expected):
        assert ca_province_name_to_province_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Toronto, Ontario", None),
            ("15752 Gatineau Ave, H3T 1X6, Montréal", None),
            ("Toronto, ON", None),
            ("Newcastle upon Tyne", None),
            ("Onalaska, WI", "WI"),
            (
                """15910 Hermosa avenue updated,Bldg 1,Central Research Park
                Sunnyvale , CA 94085
                United States""",
                "CA",
            ),
            ("Los Angeles, California", "CA"),
            ("Los Angeles, Cali?fornia", "CA"),
            ("Seattle, Washington", "WA"),
            ("Washington DC", "DC"),
            ("Richmond, Virginia", "VA"),
            ("Charleston, West Virginia", "WV"),
            ("650 Great Rd, Princeton, New Jersey", "NJ"),
            # Should be case-sensitive when detecting state code directly.
            # "de" is not mistaken for "DE", but "DE" gives "DE"
            (
                "Av. Pres. Castelo Branco, Portão 3 - Maracanã, Rio de Janeiro - RJ, 20271-130",
                None,
            ),
            ("here is Bridgeville, DE", "DE"),
        ],
    )
    def test_us_address_to_state_code(self, input_data, expected):
        assert us_address_to_state_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("1575 Gatineau Ave, H3T 1X6, Montréal", None),
            ("15751 Gatineau Ave, H3T 1X6, Montréal", None),
            ("Toronto, ON", None),
            ("Newcastle upon Tyne", None),
            ("Onalaska, WI", None),
            (
                """15910 Hermosa avenue updated,Bldg 1,Central Research Park
Sunnyvale , CA 94085
United States""",
                "CA",
            ),
            ("00000 Paris France", None),
            # No false positives
            ("2 pl. St Pierre 44100 Nantes France", None),
            (
                "Av. Pres. Castelo Branco, Portão 3 - Maracanã, Rio de Janeiro - RJ, 20271-130",
                None,
            ),
        ],
    )
    def test_us_postcode_to_state_code(self, input_data, expected):
        assert us_postcode_to_state_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            (u"Chemin du Solarium\\n Le Haut Vigneau\\n 33175 GRADIGNAN CEDEX", "33"),
            (
                "Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ",
                "33",
            ),
            (
                "Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589",
                "33",
            ),
            ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX", "33"),
            ("7 cours Grandval\\nBP 414 - 20183 AJACCIO - CEDEX", "20A"),
            ("20212   Erbajolo", "20B"),
            ("20223   Solenzara Air", "20A"),
            ("BP 55342 20223   Solenzara Air", "20A"),
            ("Chemin du Solarium Le Haut Vigneau 33 175 GRADIGNAN CEDEX", "33"),
            ("20 223   Solenzara Air", "20A"),
            ("97821 Le Port Cedex", "974"),
            ("27006 Évreux Cedex", "27"),
            ("  27006 Évreux Cedex", "27"),
            ("27006", "27"),
            ("Roissy-en-France95700", "95"),
            (" 44200 BP 10720 Nantes cedex", "44"),
            (
                "a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse",
                "31",
            ),
            (
                "a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse",
                "31",
            ),
            (
                "a l attention de M. Bon Jean, Avenue des clients bp72152, F - 31020 Toulouse",
                "31",
            ),
            ("Avenue des clients CS 72152, F - 31020 Toulouse", "31"),
            ("BP 1330, 6503 TARBES Cedex 9, tel. 05.62.54.58.63", None),
            (
                "Ville de Blanquefort, 12 rue Dupaty B.P. 20117, à l attention de fernanda Edant-33294 Blanquefort.",
                "33",
            ),
            (
                "conseil général du Haut-Rhin, 100 avenue d alsace B.P.20351, conseil général du Haut-Rhin-68006 Colmar Cedex",
                "68",
            ),
            ("Avenue des clients CS 72152, F - 31020 Toulouse", "31"),
            ("Avenue des clients CS72152, F - 31020 Toulouse", "31"),
            ("6503 TARBES Cedex 9, tel. 05.62.54.58.63", None),
            ("97701 Saint-Barthelemy", "971"),
            ("97098 Saint-Barthelemy", "971"),
            ("a l attention de M. Bon Jean, Avenue des client", None),
            ("13 avenue de la porte d'Italie TSA 61371, F - 75621 Paris", "75"),
            ("avenue René Cassin — BP 67190 97801 Saint-Denis Cedex 9", "974"),
            ("M. le maire, hôtel de Ville 97717 Saint-Denis", "974"),
            ("Rue de la Réunion, 75000 Paris", "75"),
            ("Rue de l'Orne, 44800 Saint-Herblain", "44"),
            ("Martinique", "972"),
            ("cotes d'armr", None),
            ("cotes d'armor", "22"),
            ("lot", "46"),
            ("lot-et-garonne", "47"),
            ("Ici, c'est Angers dans le-Maine et-Loire", "49"),
            ("Loire", "42"),
            ("Loiret", "45"),
            ("Haute Vienne", "87"),
            ("La Vienne-Dynamique", "86"),
            ("Haute\tLoire", "43"),
            ("Haute-Loire", "43"),
            ("-Marne-", "51"),
            ("Haute-Marne", "52"),
            ("Eure", "27"),
            ("Eure-et Loir", "28"),
            ("Indre", "36"),
            ("Indre-et Loire", "37"),
            ("Tarn", "81"),
            ("Bonjour du Tarn et Garonne", "82"),
            (u"Hauts-de-Seine ", "92"),
            (u"H\xe9rault", "34"),
            (u"Seine-Saint-Denis ", "93"),
            (u"Loire", "42"),
            (u"Corse-du-Sud", "20A"),
            (u"", None),
            (u"Vendé?e", "85"),
            (u"Loire Atlanti)que", "44"),
            (u"Yonne", "89"),
            (u"Saint Pierre et Miquelon", "975"),
            # There can be some mistakes, that we may want to fix one day.
            # In this case, we could look for 2 or 3 digit
            ("Rue de l'Orne, Saint-Herblain (44)", "61"),
        ],
    )
    def test_fr_address_to_dept_code(self, input_data, expected):
        assert fr_address_to_dept_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            (u"Chemin du Solarium\\n Le Haut Vigneau\\n 33175 GRADIGNAN CEDEX", "33"),
            (
                "Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ",
                "33",
            ),
            (
                "Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589",
                "33",
            ),
            ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX", "33"),
            ("7 cours Grandval\\nBP 414 - 20183 AJACCIO - CEDEX", "20A"),
            ("20212   Erbajolo", "20B"),
            ("20223   Solenzara Air", "20A"),
            ("BP 55342 20223   Solenzara Air", "20A"),
            ("Chemin du Solarium Le Haut Vigneau 33 175 GRADIGNAN CEDEX", "33"),
            ("20 223   Solenzara Air", "20A"),
            ("97821 Le Port Cedex", "974"),
            ("27006 Évreux Cedex", "27"),
            ("  27006 Évreux Cedex", "27"),
            ("27006", "27"),
            ("Roissy-en-France95700", "95"),
            (" 44200 BP 10720 Nantes cedex", "44"),
            (
                "a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse",
                "31",
            ),
            (
                "a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse",
                "31",
            ),
            (
                "a l attention de M. Bon Jean, Avenue des clients bp72152, F - 31020 Toulouse",
                "31",
            ),
            ("Avenue des clients CS 72152, F - 31020 Toulouse", "31"),
            ("BP 1330, 6503 TARBES Cedex 9, tel. 05.62.54.58.63", None),
            (
                "Ville de Blanquefort, 12 rue Dupaty B.P. 20117, à l attention de fernanda Edant-33294 Blanquefort.",
                "33",
            ),
            (
                "conseil général du Haut-Rhin, 100 avenue d alsace B.P.20351, conseil général du Haut-Rhin-68006 Colmar Cedex",
                "68",
            ),
            ("Avenue des clients CS 72152, F - 31020 Toulouse", "31"),
            ("Avenue des clients CS72152, F - 31020 Toulouse", "31"),
            ("6503 TARBES Cedex 9, tel. 05.62.54.58.63", None),
            ("97701 Saint-Barthelemy", "971"),
            ("97098 Saint-Barthelemy", "971"),
            ("a l attention de M. Bon Jean, Avenue des client", None),
            ("13 avenue de la porte d'Italie TSA 61371, F - 75621 Paris", "75"),
            ("avenue René Cassin — BP 67190 97801 Saint-Denis Cedex 9", "974"),
            ("M. le maire, hôtel de Ville 97717 Saint-Denis", "974"),
            ("Rue de la Réunion, 75000 Paris", "75"),
            ("Rue de l'Orne, 44800 Saint-Herblain", "44"),
            ("D7, Sainte-Luce 97228, Martinique", "972"),
            ("99999", None),
        ],
    )
    def test_fr_postcode_to_dept_code(self, input_data, expected):
        assert fr_postcode_to_dept_code(input_data) == expected
        assert address_to_zipcode(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Martinique", "972"),
            ("cotes d'armr", None),
            ("cotes d'armor", "22"),
            ("lot", "46"),
            ("lot-et-garonne", "47"),
            ("Ici, c'est Angers dans le-Maine et-Loire", "49"),
            ("Loire", "42"),
            ("Loiret", "45"),
            ("Haute Vienne", "87"),
            ("La Vienne-Dynamique", "86"),
            ("Haute\tLoire", "43"),
            ("Haute-Loire", "43"),
            ("-Marne-", "51"),
            ("Haute-Marne", "52"),
            ("Eure", "27"),
            ("Eure-et Loir", "28"),
            ("Indre", "36"),
            ("Indre-et Loire", "37"),
            ("Tarn", "81"),
            ("Bonjour du Tarn et Garonne", "82"),
            (u"Hauts-de-Seine ", "92"),
            (u"H\xe9rault", "34"),
            (u"Seine-Saint-Denis ", "93"),
            (u"Loire", "42"),
            (u"Corse-du-Sud", "20A"),
            (u"", None),
            (u"Vendé?e", "85"),
            (u"Loire Atlanti)que", "44"),
            (u"Yonne", "89"),
            (u"Saint Pierre et Miquelon", "975"),
            # There may be some mistakes, so be careful what is passed
            ("Rue de la Réunion, 75000 Paris", "974"),
            ("Rue de l'Orne, 44800 Saint-Herblain", "61"),
        ],
    )
    def test_fr_dept_name_dept_code(self, input_data, expected):
        assert fr_dept_name_to_dept_code(input_data) == expected
        assert dept_name_to_zipcode(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("73", ("31", ["09", "12", "31", "32", "46", "65", "81", "82"])),
            ("06", ("976", ["976"])),
            (6, ("976", ["976"])),
            ("6", ("976", ["976"])),
            ("24", ("45", ["18", "28", "36", "37", "41", "45"])),
            ("22", ("80", ["02", "60", "80"])),
            (
                "93",
                ("13", ["04", "05", "06", "13", "83", "84"]),
            ),
            ("", None),
            (None, None),
        ],
    )
    def test_fr_region_id_to_info(self, input_data, expected):
        assert fr_region_id_to_info(input_data) == expected
        assert region_info_from_id(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Bienvenue en bourgogne franche comté", "27"),
            ("midi pyrénées", "73"),
            ("grand est", "44"),
            (u"mayotte ", "06"),
            (u"Centre val de Loire", "24"),
            (u"Picardie ", "22"),
            (u"provence alpes côte d'azur", "93"),
            (u"", None),
            (u"hauts de france", "32"),
            (u"auvergne rhône alpes", "84"),
            (u"nouvelle aquitaine", "75"),
            (u"La guadeloupe, une superbe région", "01"),
            (u"VICE-RECTORAT DE MAYOTTE ( DCS)", "06"),
        ],
    )
    def test_fr_region_name_to_id(self, input_data, expected):
        assert fr_region_name_to_id(input_data) == expected
        assert region_name_to_id(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            (
                "Bienvenue en bourgogne franche comté",
                ("21", ["21", "58", "71", "89", "25", "39", "70", "90"]),
            ),
            ("midi pyrénées", ("31", ["09", "12", "31", "32", "46", "65", "81", "82"])),
            (
                "grand est",
                ("67", ["67", "68", "54", "55", "57", "88", "08", "10", "51", "52"]),
            ),
            (u"mayotte ", ("976", ["976"])),
            (u"Centre val de Loire", ("45", ["18", "28", "36", "37", "41", "45"])),
            (u"Picardie ", ("80", ["02", "60", "80"])),
            (
                u"provence alpes côte d'azur",
                ("13", ["04", "05", "06", "13", "83", "84"]),
            ),
            (u"", None),
            (u"hauts de france", ("59", ["59", "62", "02", "60", "80"])),
            (
                u"auvergne rhône alpes",
                (
                    "69",
                    [
                        "03",
                        "15",
                        "43",
                        "63",
                        "01",
                        "07",
                        "26",
                        "38",
                        "42",
                        "69",
                        "73",
                        "74",
                    ],
                ),
            ),
            (
                u"nouvelle aquitaine",
                (
                    "33",
                    [
                        "24",
                        "33",
                        "40",
                        "47",
                        "64",
                        "19",
                        "23",
                        "87",
                        "16",
                        "17",
                        "79",
                        "86",
                    ],
                ),
            ),
            (u"La guadeloupe, une superbe région", ("971", ["971"])),
            (u"VICE-RECTORAT DE MAYOTTE ( DCS)", ("976", ["976"])),
            (
                "Les Pays de la Loire, une superbe région",
                ("44", ["44", "49", "53", "72", "85"]),
            ),
        ],
    )
    def test_fr_region_name_to_info(self, input_data, expected):
        assert fr_region_name_to_info(input_data) == expected
        assert region_info_from_name(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, kwargs, expected",
        [
            # Look for the country name in any language available by default
            ("Deutschland", {}, "DE"),  # de
            ("Germany", {}, "DE"),  # en
            ("Allemagne", {}, "DE"),  # fr
            ("Alemanha", {}, "DE"),  # pt
            # If no country found, return None
            ("Wonderland", {}, None),
            ("Germany", {"lang": "fr"}, None),
            # No confusion with Congo
            ("Congo (Brazzaville)", {}, "CG"),
            ("Congo (Kinshasa)", {}, "CD"),
            ("Congo", {}, "CG"),
            # Any capitalization for lang works
            ("Germany", {"lang": "en"}, "DE"),
            ("Germany", {"lang": "En"}, "DE"),
            ("Germany", {"lang": "EN"}, "DE"),
            ("Germany", {"lang": "eN"}, "DE"),
        ],
    )
    def test_country_name_to_country_code(self, input_data, kwargs, expected):
        assert country_name_to_country_code(input_data, **kwargs) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("france", "FR"),
            ("Comores", "KM"),
            ("Madagascar", "MG"),
            (u"S\xe9n\xe9gal", "SN"),
            ("République démocratique du Congo", "CD"),
            ("Mali", "ML"),
            ("Sri Lanka ", "LK"),
            (u"\xa0V\xe9n\xe9zuela\xa0", "VE"),
            (u"Vi\xeatnam", "VN"),
            ("Nigeria", "NG"),
            (u"Niger", "NE"),
            (u"aaa ( bbb", None),
            (u" Le  nigéria c'est trop   sympa", "NG"),
            (u"Pays d'exécution : Niger", "NE"),
            ("  Côte d'Ivoire ", "CI"),
            ("  Côte d’Ivoire ", "CI"),  # with accent for apostrophe
            ("U.S. Mission Iraq\n\nIraq", "IQ"),
            ("Pays:France ?".encode("ascii", "ignore"), "FR"),
            (",royaume-uni,", "GB"),
            (u"trinité-et-Tobago", "TT"),
            ("surinam", "SR"),
            (u"saint-barthélemy", "BL"),
            (u"saint-barthélemy", "BL"),
            ("sint maarten", "SX"),
            (u"curaçao", "CW"),
            ("andorre", "AD"),
            ("bonaire, saint-eustache et saba", "BQ"),
            ("soudan", "SD"),
            ("soudan du sud", "SS"),
            ("PAYS-BRÉSIL", "BR"),
            (u"Lorem ipsum Libye - LIBYE", "LY"),
            ("palestine", "PS"),
            ("Congo (Brazzaville)", "CG"),
            ("Congo (Kinshasa)", "CD"),
            ("São tome & principe ", "ST"),
        ],
    )
    def test_country_name_to_country_code_fr(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="fr") == expected
        assert country_name_to_id(input_data, lang="fr") == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Mongolia", "MN"),
            ("Marocco", "MA"),
            ("Georgia", "GE"),
            ("kosovo", "KO"),
            ("Namibia", "NA"),
            ("Venezuela", "VE"),
            ("Armenia", "AM"),
            ("sweden", "SE"),
            (u"Knotts Island, NC 27950\n\n27950-0039\nUnited States", "US"),
            (
                "721 APS BLDG 3334\nUNIT 3295 \nRamstein Air Base, Non-U.S. 66877 \nGermany ",
                "DE",
            ),
            ("Saudi Arabia", "SA"),
            ("Country execution:nigeria.", "NG"),
            ("RUSSIA", "RU"),
            ("PAPUA NEW GUINEA", "PG"),
            ("guinea-bissau", "GW"),
            ("netherlands antilles", "AN"),
            ("netherlands or something", "NL"),
            (u"curaçao", "CW"),
            (u"saint barthélemy", "BL"),
            ("Sudan", "SD"),
            ("South Sudan", "SS"),
            ("tanzania", "TZ"),
            ("united states minor outlying islands", "UM"),
            ("Lorem ipsum Libya - LIBYA", "LY"),
            (" Democratic Republic of the Congo", "CD"),
            ("CONGO, DEM. REPUBLIC", "CD"),
            ("TIMOR LESTE", "TL"),
            ("state of palestine", "PS"),
            ("palestine, state of", "PS"),
        ],
    )
    def test_country_name_to_country_code_en(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="EN") == expected
        assert country_name_to_id(input_data, lang="EN") == expected

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
    def test_country_name_to_country_code_de(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="DE") == expected
        assert country_name_to_id(input_data, lang="DE") == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Afeganistão", "AF"),
            ("África do Sul", "ZA"),
            ("Albânia", "AL"),
            ("Butão", "BT"),
            ("Camarões", "CM"),
            ("República Centro-Africana", "CF"),
            ("Grécia", "GR"),
            ("Lituânia", "LT"),
            ("Estados Federados da Micronésia", "FM"),
            ("Nigéria!!", "NG"),
            ("Lorem Ipsum, país Níger ", "NE"),
            ("   Panamá      ", "PA"),
            ("o país do peru", "PE"),
            (u"País de execução: Polónia", "PL"),
            ("São Vicente e Granadinas    ", "VC"),
        ],
    )
    def test_country_name_to_country_code_pt(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="PT") == expected
        assert country_name_to_id(input_data, lang="PT") == expected

    @pytest.mark.parametrize(
            "input_data, expected",
            [
                ("Los Emiratos Árabes Unidos", "AE"),
                ("  Islas   Vírgenes   Británicas   ", "VG"),
                ("Turkménistan\n", "TM"),
                ("España!", "ES"),
                ("Egipto", "EG"),
                ("groenlandia", "GL"),
                ("Camboya", "KH"),
                ("Isla de Mauricio", "MU"),
                ("San Cristóbal y Nieves", "KN"),
                ("Nueva Zelanda", "NZ"),
                ("Países Bajos ", "NL"),
                ("Kirguistán", "KG"),
                ("suiza", "CH"),
                ("Tayikistán", "TJ"),
                ("Tailandia", "TH"),
            ],
        )
    def test_country_name_to_country_code_es(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="ES") == expected
        assert country_name_to_id(input_data, lang="ES") == expected

    @pytest.mark.parametrize(
        "input_data, kwargs, expected",
        [
            # Look for the capital name in any language available by default
            ("Kairo?", {}, "EG"),  # de
            ("    Cairo   ", {}, "EG"),  # en
            ("Le Caire\n", {}, "EG"),  # fr
            # If no country found, return None
            ("Wonderland", {}, None),
            ("Kairo", {"lang": "fr"}, None),
            # Any capitalization for lang works
            ("Cairo", {"lang": "en"}, "EG"),
            ("Cairo", {"lang": "En"}, "EG"),
            ("Cairo", {"lang": "EN"}, "EG"),
            ("Cairo", {"lang": "eN"}, "EG"),
        ],
    )
    def test_capital_name_to_country_code(self, input_data, kwargs, expected):
        assert capital_name_to_country_code(input_data, **kwargs) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("bruxelles", "BE"),
            (u"La ville est Lomé.", "TG"),
        ],
    )
    def test_capital_name_to_country_code_fr(self, input_data, expected):
        assert capital_name_to_country_code(input_data, lang="FR") == expected
        assert capital_name_to_country_id(input_data, lang="FR") == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Copenhagen", "DK"),
            ("bern", "CH"),
            ("The city is ulaanbaatar.", "MN"),
        ],
    )
    def test_capital_name_to_country_code_en(self, input_data, expected):
        assert capital_name_to_country_code(input_data, lang="EN") == expected
        assert capital_name_to_country_id(input_data, lang="EN") == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Kopenhagen", "DK"),
            (u"são tomé", "ST"),
            ("Das stadt ist Ulaanbaatar.", "MN"),
        ],
    )
    def test_capital_name_to_country_code_de(self, input_data, expected):
        assert capital_name_to_country_code(input_data, lang="DE") == expected
        assert capital_name_to_country_id(input_data, lang="DE") == expected

    def test_country_name_to_country_code_with_unknown_language(self):
        unknown_lang = "it"
        # If this breaks, this is because the language was added.
        # Just choose another unkown language and use another example.
        assert unknown_lang not in language_to_country_names
        assert country_name_to_country_code("Italia", lang=unknown_lang) is None

    def test_capital_name_to_country_code_with_unknown_language(self):
        unknown_lang = "it"
        # If this breaks, this is because the language was added.
        # Just choose another unkown language and use another example.
        assert unknown_lang not in language_to_capital_names
        assert capital_name_to_country_code("Roma", lang=unknown_lang) is None

    @pytest.mark.parametrize(
        "input_data, kwargs, expected",
        [
            # All countries are used by default
            ("2 pl. Saint-Pierre, 44000 Nantes, France", {}, "44"),
            ("US Highway 24, Granite, CO 81228-2209", {}, "CO"),
            # You can use any type of capitalization for country
            ("2 pl. Saint-Pierre, 44000 Nantes", {"country": "fr"}, "44"),
            ("2 pl. Saint-Pierre, 44000 Nantes", {"country": "FR"}, "44"),
            # If no subdivision is found for the given country, nothing is returned.
            ("", {}, None),
            ("2 pl. Saint-Pierre, 44000 Nantes", {"country": "ca"}, None),
            # You do not have to specify the correct country for the subdivision
            # code to be found. When the country is specified, we look for that
            # specific country.
            (
                "1196 Voie Camillien-Houde, Montréal, QC H3H 1A1",
                {"country": "ca"},
                "QC",
            ),
            (
                "1196 Voie Camillien-Houde, Montréal, QC H3H 1A1",
                {},
                "QC",
            ),
            ("Los Angeles, CA 90068, États-Unis", {"country": "us"}, "CA"),
            ("Los Angeles, CA 90068, États-Unis", {}, "CA"),
            # Also, there should be no positives due to a confusion between
            # French and US postcodes
            ("US Highway 24, Granite, CO 81228-2209", {"country": "fr"}, None),
            ("US Highway 24, Granite, CO 81228-2209, USA", {"country": "fr"}, None),
            ("2 pl. Saint-Pierre, 44000 Nantes, France", {"country": "us"}, None),
            # We should always find the correct subdivision code
            # when detection via postcode is involved.
            ("US Highway 24, Granite, CO 81228-2209", {}, "CO"),
            ("US Highway 24, Granite, CO 81228-2209, USA", {}, "CO"),
            ("US Highway 24, Granite, CO 81228-2209", {"country": "US"}, "CO"),
            ("US Highway 24, Granite, CO 81228-2209, USA", {"country": "US"}, "CO"),
            ("2 pl. Saint-Pierre, 44000 Nantes", {"country": "FR"}, "44"),
            ("2 pl. Saint-Pierre, 44000 Nantes, France", {}, "44"),
            ("2 pl. Saint-Pierre, 44000 Nantes, France", {"country": "FR"}, "44"),
        ],
    )
    def test_address_to_subdivision_code(self, input_data, kwargs, expected):
        assert address_to_subdivision_code(input_data, **kwargs) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("2 pl. Saint-Pierre, 44000 Nantes, France", "FR"),
            ("1196 Voie Camillien-Houde, Montréal, QC H3H 1A1, Canada", "CA"),
            ("Los Angeles, CA\nUnited States", "US"),
            ("Cabul, Afeganistão", "AF"),
            ("Try to find South Sudan in an address", "SS"),
            ("650 Great Rd, Princeton, New Jersey", "US"),
            ("St Peter, Jersey JE1 1BY, Jersey", "JE"),
            # The country code can be found using the capital name in any available language
            ("Kairo", "EG"),
            ("Paris", "FR"),
            ("Washington D.C.", "US"),
            ("Ottawa", "CA"),
            # If no country code is found, nothing is returned.
            ("", None),
            ("2 pl. Saint-Pierre, 44000 Nantes", None),
            (
                "Av. Pres. Castelo Branco, Portão 3 - Maracanã, Rio de Janeiro - RJ, 20271-130",
                None,
            ),
        ],
    )
    def test_address_to_country_code(self, input_data, expected):
        assert address_to_country_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, kwargs, expected",
        [
            ("2 pl. Saint-Pierre, 44000 Nantes, France", {}, ("FR", "44")),
            # We need to specify a country to find that 44000 is for France
            ("2 pl. Saint-Pierre, 44000 Nantes", {"country": "FR"}, ("FR", "44")),
            (
                "1196 Voie Camillien-Houde, Montréal, QC H3H 1A1, Canada",
                {},
                ("CA", "QC"),
            ),
            ("Los Angeles, CA\nUnited States", {}, ("US", "CA")),
            # A subdivision code might not always be found.
            ("Nantes, France", {}, ("FR", None)),
            ("Los Angeles, United States", {}, ("US", None)),
            ("Montréal, Canada", {}, ("CA", None)),
            # The capital names can be use to find the country code.
            ("Kairo", {}, ("EG", None)),
            ("Paris", {}, ("FR", "75")),
            ("Washington D.C", {}, ("US", "DC")),
            ("Ottawa", {}, ("CA", None)),
            # It should not give awkward results because French postcodes
            # and US postcode look the same.
            ("2 pl. Saint-Pierre, 44000 Nantes, France", {}, ("FR", "44")),
            ("6931 Rings Rd, Amlin, OH 43002", {}, ("US", "OH")),
            ("2 pl. Saint-Pierre, 44000 Nantes", {"country": "US"}, (None, None)),
            ("6931 Rings Rd, Amlin, OH 43002", {"country": "FR"}, (None, None)),
            # It assumes that if you provide a country, then it must
            # be the same as the one found from the text return it,
            # even when the country subdivisions are unknown.
            ("Kairo", {"lang": "de", "country": "US"}, (None, None)),
            ("Kairo", {"lang": "de", "country": "EG"}, ("EG", None)),
            # The default results is a tuple made of two Nones.
            ("", {}, (None, None)),
            ("2 pl. Saint-Pierre, Nantes", {}, (None, None)),
        ],
    )
    def test_address_to_country_and_subdivision_code(
        self, input_data, kwargs, expected
    ):
        assert (
            address_to_country_and_subdivision_codes(input_data, **kwargs) == expected
        )

    def test_each_country_name_in_data_is_a_safe_string(self):
        """
        If there is one country name which is not a safe string,
        replace that name by the safe one in data.
        """
        for lang, country_names in language_to_country_names.items():
            for name in country_names:
                assert safe_string(name) == name

    def test_each_capital_name_in_data_is_a_safe_string(self):
        """
        If there is one capital name which is not a safe string,
        replace that name by the safe one in data.
        """
        for lang, capital_names in language_to_capital_names.items():
            for name in capital_names:
                assert safe_string(name) == name


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
