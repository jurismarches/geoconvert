import pytest

from geoconvert import find_countries


class TestConvert:
    @pytest.mark.parametrize(
        "input_data, expected",
        [
            # As codes
            (
                "AT,KO,NO",
                ["AT", "KO", "NO"],
            ),
            (  # non valids codes are not taken
                "AT,KO,NO,XX",
                ["AT", "KO", "NO"],
            ),
            # only one word
            (
                "spain",
                ["ES"],
            ),
            # with separators
            (
                # ,
                "china, france, spain",
                ["CN", "ES", "FR"],
            ),
            (
                # &
                "china &amp; france &amp; spain",
                ["CN", "ES", "FR"],
            ),
            (
                # \n
                "china \n france \n spain",
                ["CN", "ES", "FR"],
            ),
            # "et" is both a separator and not a separator
            (
                "espagne, antigua et barbuda et france",
                ["AG", "ES", "FR"],
            ),
            # Without separators
            (
                "china france spain",
                ["CN", "ES", "FR"],
            ),
            # multiple-words countries
            (
                "nouvelle Zélande, el salvador",
                ["NZ", "SV"],
            ),
            # Multi-lang is ok
            (
                "nouvelle Zélande, kyrgyz republic, weirussland",
                ["BY", "KG", "NZ"],
            ),
            (
                (
                    "le programme DPA a été mis en œuvre au Bénin "
                    "au Cameroun "
                    "en Côte d’Ivoire "
                    "à Madagascar "
                    "et au Tchad"
                ),
                ["BJ", "CI", "CM", "MG", "TD"],
            ),
            # If no country code is found, nothing is returned.
            ("", []),
            ("2 pl. Saint-Pierre, 44000 Nantes", []),
            (
                "Av. Pres. Castelo Branco, Portão 3 - Maracanã",
                [],
            ),
        ],
    )
    def test_find_countries(self, input_data, expected):
        """
        Test countries detection
        """
        result = find_countries(input_data)
        assert result == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            #
            # Guinea
            #
            (  # "multiple names" form is recognized as only one country
                "Papua New Guinea",
                ["PG"],
            ),
            (  # both countries are recognized in a list
                "Papua New Guinea, Guinea",
                ["GN", "PG"],
            ),
            (  # both countries are recognized in text
                "Papua New Guinea and Guinea",
                ["GN", "PG"],
            ),
            #
            # Sudan
            #
            (  # "multiple names" form is recognized as only one country
                "South Sudan",
                ["SS"],
            ),
            (  # both countries are recognized in a list
                "Sudan, South Sudan",
                ["SD", "SS"],
            ),
            (  # both countries are recognized in text
                "South Sudan and Sudan",
                ["SD", "SS"],
            ),
            #
            # Congo
            #
            (  # "multiple names" form is recognized as only one country
                "République démocratique du Congo",
                ["CD"],
            ),
            (  # both countries are recognized in a list
                "République démocratique du Congo, République du Congo",
                ["CD", "CG"],
            ),
            (  # both countries are recognized in a list
                "République démocratique du Congo, Congo",
                ["CD", "CG"],
            ),
            (
                "République démocratique du Congo et République du Congo",
                ["CD", "CG"],
            ),
            (
                "République démocratique du Congo et Congo",
                ["CD", "CG"],
            ),
            (
                "congo, République démocratique du, congo, république du ",
                ["CD", "CG"],
            ),
            (
                "congo, République  du, congo, république démocratique du ",
                ["CD", "CG"],
            ),
            (
                """GAUFF CONSULTANTS AFRIQUE (930919)
                    Country: République du Congo

                    SERING INGEGNERIA (930912)
                    Country: République démocratique du Congo""",
                ["CD", "CG"],
            ),
            (
                """GAUFF CONSULTANTS AFRIQUE (930919)<br>Country: République du Congo<br>SERING INGEGNERIA (930912)<br/>Country: République démocratique du Congo""",
                ["CD", "CG"],
            ),
            (
                """<li>Country: République du Congo</li><li/>Country: République démocratique du Congo<li/>""",
                ["CD", "CG"],
            ),
        ],
    )
    def test_find_special_countries_disambiguation(self, input_data, expected):
        """
        Some countries have ambiguous names. Here, test some common cases.

        Mainly though as a non-regression test case.
        """
        result = find_countries(input_data)
        assert result == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            (
                "10 millions de francs suisse",
                ["CH"],  # should be []
            ),
            (
                "Fourniture de yaourt 'Petit suisse'",
                ["CH"],  # should be []
            ),
            (
                "Rue de la Kinshasa, 75000 Paris",
                ["CD", "FR", "US"],  # should be ["FR"]
            ),
        ],
    )
    def test_find_countries_not_detected_yet(self, input_data, expected):
        """
        This test lists known non-handle cases. If any of this test breaks, it may be a good thing !
        """
        result = find_countries(input_data)
        assert result == expected
