import pytest

from geoconvert.convert import (
    us_address_to_state_code,
    us_postcode_to_state_code,
)


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
