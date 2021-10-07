import pytest

from geoconvert.convert import (
    address_to_country_and_subdivision_codes,
    address_to_subdivision_code,
    address_to_zipcode,
    ca_address_to_province_code,
    ca_postcode_to_province_code,
    ca_province_name_to_province_code,
    de_address_to_land_code,
    de_hauptstadt_to_land_code,
    de_land_name_to_land_code,
    dept_name_to_zipcode,
    fr_address_to_dept_code,
    fr_dept_name_to_dept_code,
    fr_postcode_to_dept_code,
    us_address_to_state_code,
    us_postcode_to_state_code,
)


class TestNoCountryProvided:

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


class TestCanada:

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


class TestGermany:

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Katharinenberg 14 – 20 18439 Stralsund ", None),
            # Detection via province code should be case-sensitive
            ("Be yourself!", None),
            ("This is BE", "BE"),
        ],
    )
    def test_de_address_to_land_code(self, input_data, expected):
        assert de_address_to_land_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Hamburg liegt in Norddeutschland", "HH"),
            ("Metropolregion Hamburg", "HH"),
            ("Glockengießerwall 5 20095 Hamburg", "HH"),
            ("Nordrhein Westfalen", "NW"),
            ("nordrhein-westfalen", "NW"),
            ("Thüringen", "TH"),
            ("thuringen", "TH"),
            ("The capital of Germany is Berlin", "BE"),
        ],
    )
    def test_de_land_name_to_land_code(self, input_data, expected):
        assert de_land_name_to_land_code(input_data) == expected
        assert de_address_to_land_code(input_data) == expected
        assert address_to_country_and_subdivision_codes(input_data) == ("DE", expected)
        assert address_to_country_and_subdivision_codes(input_data, iso_format=True) == "DE-" + expected
    

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Humboldtstraße 5–6 14467 Potsdam", "BB"),
            ("is in Frankfurt-Am-Main", "HE"),
            ("GUTEN TAG KÖLN", "NW"),
            ("leipzig", "SN"),
        ],
    )
    def test_de_hauptstadt_to_land_code(self, input_data, expected):
        assert de_hauptstadt_to_land_code(input_data) == expected
        assert de_address_to_land_code(input_data) == expected
        assert address_to_country_and_subdivision_codes(input_data) == ("DE", expected)
        assert address_to_country_and_subdivision_codes(input_data, iso_format=True) == "DE-" + expected


class TestUSA:

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


class TestFrance:

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
            ("97701 Saint-Barthelemy", "977"),
            ("97098 Saint-Barthelemy", "977"),
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
            ("Tout savoir sur Saint Barthélemy", "977"),
            ("Tout savoir sur saint-barthelemy", "977"),
            ("Tout savoir sur saint Barthélémy", "977"),
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
            ("97701 Saint-Barthelemy", "977"),
            ("97098 Saint-Barthelemy", "977"),
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
            ("Tout savoir sur Saint Barthélemy", "977"),
            ("Tout savoir sur saint-barthelemy", "977"),
            ("Tout savoir sur saint Barthélémy", "977"),
            # There may be some mistakes, so be careful what is passed
            ("Rue de la Réunion, 75000 Paris", "974"),
            ("Rue de l'Orne, 44800 Saint-Herblain", "61"),
        ],
    )
    def test_fr_dept_name_dept_code(self, input_data, expected):
        assert fr_dept_name_to_dept_code(input_data) == expected
        assert dept_name_to_zipcode(input_data) == expected

