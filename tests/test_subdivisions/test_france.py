import pytest

from geoconvert.convert import (
    address_to_zipcode,
    dept_name_to_zipcode,
    fr_address_to_dept_code,
    fr_dept_name_to_dept_code,
    fr_postcode_to_dept_code,
)


class TestFrance:
    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Chemin du Solarium\\n Le Haut Vigneau\\n 33175 GRADIGNAN CEDEX", "33"),
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
            # NUTS code
            ("stasticial region FRB04", "37"),
            ("stasticial region fr244", "37"),
            # Dept names
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
            ("Hauts-de-Seine ", "92"),
            ("H\xe9rault", "34"),
            ("Seine-Saint-Denis ", "93"),
            ("Loire", "42"),
            ("Corse-du-Sud", "20A"),
            ("", None),
            ("Vendé?e", "85"),
            ("Loire Atlanti)que", "44"),
            ("Yonne", "89"),
            ("Saint Pierre et Miquelon", "975"),
            ("Tout savoir à propos de Saint Barthélemy", "977"),
            ("Tout savoir à propos de saint-barthelemy", "977"),
            ("Tout savoir à propos de saint Barthélémy", "977"),
            # Region names
            ("Pays de la Loire", "44"),
            # Special cases for the old French région "Centre"
            ("Région Centre", "45"),
            ("Conseil Régional centre", "45"),
            # No confusion with the old "Centre" name for the French region "Centre-Val-de-Loire"
            ("Centre Pompidou", None),
            # No confusion with the "Nord" department
            ("Hopital nord Franche Comté", "25"),
            # Both dept name and region name
            ("Guyane", "973"),
            ("Guadeloupe", "971"),
            # Avoid disambiguations
            # due to street names
            ("Rue de la Réunion 61000 Alencon", "61"),  # "réunion" could mean 974
            ("rue de Paris, Nantes", None),  # "paris" could mean 75
            ("Rue de l'Orne, 44800 Saint-Herblain (44)", "44"),  # "Orne" could be 61
            # due to city names
            ("Sully sur Loire (Loiret)", "45"),  # "Loire" could mean 42
            ("Gournay-sous-Marne (Seine saint Denis)", "93"),  # "Marne" could be 51
            # due to phrase
            ("en val-de-Loire", None),  # "Loire" could be 42
            # The current strategy has drawbacks
            ("Tout savoir sur Saint Barthélemy", None),
            # There can be some mistakes, that we may want to fix one day.
            ("Vallées de l'Orne et de l'Odon", "61"),  # in 14
            ("commune de Saint-Vincent-des-Landes", "40"),  # in 44
            # In this case, we could look for 2 or 3 digit
            ("CHU 44", None),  # in 44
        ],
    )
    def test_fr_address_to_dept_code(self, input_data, expected):
        assert fr_address_to_dept_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Chemin du Solarium\\n Le Haut Vigneau\\n 33175 GRADIGNAN CEDEX", "33"),
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
            # Saint-Martin postcodes
            ("Code postal 97150", "971"),
            ("Code postal 97051", "971"),
            ("Code postal 97080", "971"),
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
            ("Hauts-de-Seine ", "92"),
            ("H\xe9rault", "34"),
            ("Seine-Saint-Denis ", "93"),
            ("Loire", "42"),
            ("Corse-du-Sud", "20A"),
            ("", None),
            ("Vendé?e", "85"),
            ("Loire Atlanti)que", "44"),
            ("Yonne", "89"),
            ("Saint Pierre et Miquelon", "975"),
            ("Tout savoir à propos de Saint Barthélemy", "977"),
            ("Tout savoir à propos de saint-barthelemy", "977"),
            ("Tout savoir à propos de saint Barthélémy", "977"),
            # Avoid disambiguations
            # due to street names
            ("Rue de la Réunion 61000 Alencon", None),  # "réunion" could mean 974
            ("rue de Paris, Nantes", None),  # "paris" could mean 75
            ("Rue de l'Orne, Saint-Herblain (44)", None),  # "Orne" could be 61
            # due to city names
            ("Sully sur Loire (Loiret)", "45"),  # "Loire" could mean 42
            ("Gournay-sous-Marne (Seine saint Denis)", "93"),  # "Marne" could be 51
            # due to phrase
            ("en val-de-Loire", None),  # "Loire" could be 42
            # The current strategy has drawbacks
            ("Tout savoir sur Saint Barthélemy", None),
            # There can be some mistakes, that we may want to fix one day.
            ("Vallées de l'Orne et de l'Odon", "61"),  # in 14
            ("commune de Saint-Vincent-des-Landes", "40"),  # in 44
        ],
    )
    def test_fr_dept_name_dept_code(self, input_data, expected):
        assert fr_dept_name_to_dept_code(input_data) == expected
        assert dept_name_to_zipcode(input_data) == expected
