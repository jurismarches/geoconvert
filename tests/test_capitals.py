import pytest

from geoconvert.convert import (
    capital_name_to_country_code,
    capital_name_to_country_id,
    language_to_capital_names,
)
from geoconvert.utils import safe_string


class TestCapitals:
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
            ("La ville est Lomé.", "TG"),
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
            ("são tomé", "ST"),
            ("Das stadt ist Ulaanbaatar.", "MN"),
        ],
    )
    def test_capital_name_to_country_code_de(self, input_data, expected):
        assert capital_name_to_country_code(input_data, lang="DE") == expected
        assert capital_name_to_country_id(input_data, lang="DE") == expected

    def test_capital_name_to_country_code_with_unknown_language(self):
        unknown_lang = "it"
        # If this breaks, this is because the language was added.
        # Just choose another unkown language and use another example.
        assert unknown_lang not in language_to_capital_names
        assert capital_name_to_country_code("Roma", lang=unknown_lang) is None

    def test_each_capital_name_in_data_is_a_safe_string(self):
        """
        If there is one capital name which is not a safe string,
        replace that name by the safe one in data.
        """
        for lang, capital_names in language_to_capital_names.items():
            for name in capital_names:
                assert safe_string(name) == name
