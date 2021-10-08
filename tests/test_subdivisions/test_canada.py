import pytest

from geoconvert.convert import (
    ca_address_to_province_code,
    ca_postcode_to_province_code,
    ca_province_name_to_province_code,
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
