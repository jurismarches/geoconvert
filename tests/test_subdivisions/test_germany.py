import mock
import pytest

from geoconvert.convert import (
    address_to_country_and_subdivision_codes,
    de_address_to_land_code,
    de_hauptstadt_to_land_code,
    de_land_name_to_land_code,
    de_postcode_to_land_code,
)


class TestGermany:
    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Katharinenberg 14 – 20 18439 Stralsund ", "MV"),
            # Detection via province code should be case-sensitive
            ("Be yourself!", None),
            ("This is BE", "BE"),
            ("31-37 53179 Bonn Telefon: +49 228 4010 Fax: +49 228 4011223", "NW"),
            # nuts code
            ("stasticial region de119", "BW"),
            ("stasticial region DE2", "BY"),
        ],
    )
    def test_de_address_to_land_code(self, input_data, expected):
        assert de_address_to_land_code(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("65760 Eschborn", "HE"),
            ("Straße 3 53119 Bonn Telefon: +49 22899610-2928", "NW"),
            ("80639        München", "BY"),
            ("Eschborn", None),
        ],
    )
    def test_de_postcode_to_land_code(self, input_data, expected):
        assert de_postcode_to_land_code(input_data) == expected
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

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            # land name
            ("Hamburg liegt in Norddeutschland", ("DE", "HH")),
            ("Metropolregion Hamburg", ("DE", "HH")),
            ("Glockengießerwall 5 20095 Hamburg", ("DE", "HH")),
            ("Nordrhein Westfalen", ("DE", "NW")),
            ("nordrhein-westfalen", ("DE", "NW")),
            ("Thüringen", ("DE", "TH")),
            ("thuringen", ("DE", "TH")),
            ("The capital of Germany is Berlin", ("DE", "BE")),
            # hauptstadt
            ("Humboldtstraße 5–6 14467 Potsdam", ("DE", "BB")),
            ("is in Frankfurt-Am-Main", ("DE", "HE")),
            ("GUTEN TAG KÖLN", ("DE", "NW")),
            ("leipzig", ("DE", "SN")),
            ("80639        München", ("DE", "BY")),
            # land code
            ("Be yourself!", (None, None)),
            ("This is BE", (None, None)),
            ("This is BE in Germany", ("DE", "BE")),
            # Postcodes
            ("Katharinenberg 14 – 20 18439 Stralsund", (None, None)),
            ("Katharinenberg 14 – 20 18439 Stralsund GERMANY", ("DE", "MV")),
            ("31-37 53179 Bonn Telefon: +49 228 4010", (None, None)),
            ("31-37 53179 Bonn DEUTSCHLAND Telefon: +49 228 4010", ("DE", "NW")),
            ("65760 Eschborn", (None, None)),
            ("65760 Eschborn germany", ("DE", "HE")),
        ],
    )
    def test_de_country_and_subdivision_codes(self, input_data, expected):
        assert address_to_country_and_subdivision_codes(input_data) == expected
        expected = (
            f"{expected[0]}-{expected[1]}" if not expected == (None, None) else None
        )
        assert (
            address_to_country_and_subdivision_codes(input_data, iso_format=True)
            == expected
        )

    @mock.patch("geoconvert.convert.DE_POSTCODE_RANGE", {})
    def test_de_postcode_to_land_code_with_no_data(self):
        # NOTE : this test has no other use than to keep a 100% coverage
        assert de_postcode_to_land_code("00000") is None
