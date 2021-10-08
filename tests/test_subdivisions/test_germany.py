import pytest

from geoconvert.convert import (
    address_to_country_and_subdivision_codes,
    de_address_to_land_code,
    de_hauptstadt_to_land_code,
    de_land_name_to_land_code,
)


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
