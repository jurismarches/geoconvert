import pytest

from geoconvert.convert import (
    address_to_country_and_subdivision_codes,
    address_to_subdivision_code,
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
