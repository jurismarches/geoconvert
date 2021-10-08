import mock
import pytest

from geoconvert.convert import (
    address_to_country_and_subdivision_codes,
    br_address_to_state_code,
    br_postcode_to_state_code,
    br_state_name_to_state_code,
)


class TestBrazil:
    @pytest.mark.parametrize(
        "input_data",
        [
            "Le Pernambouc",
            "Av. Pres. Castelo Branco, Portão 3 - Maracanã",
        ],
    )
    def test_not_found(self, input_data):
        assert br_address_to_state_code(input_data) is None

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Praça da Luz, 2 – Luz SP, BR", "SP"),
            ("Museu Oscar Niemeyer, Curitiba – PR, Brazil", "PR"),
            ("Dourados, MS, Brésil", "MS"),
        ],
    )
    def test_br_address_to_state_code(self, input_data, expected):
        assert br_address_to_state_code(input_data) == expected
        # unsafe : country must be precised
        assert address_to_country_and_subdivision_codes(input_data, country="BR") == (
            "BR",
            expected,
        )
        assert (
            address_to_country_and_subdivision_codes(
                input_data, country="BR", iso_format=True
            )
            == "BR-" + expected
        )

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Localização   :   Goiânia, Goiás, Brasil", "GO"),
            ("São Luís (frequentemente chamado de São Luís do Maranhão)", "MA"),
            ("a capital do estado do maranhao.", "MA"),
            ("Avenida Pedro Alvares Cabral Vila Mariana, São Paulo", "SP"),
            ("cidade do Rio-de-Janeiro", "RJ"),
            ("Praça da Luz, 2 – Luz, São Paulo", "SP"),
            ("Dourados, État du Mato Grosso do Sul", "MS"),
            ("Dourados, État du Mato Grosso", "MT"),
            ("PARA", "PA"),
            ("Paraiba", "PB"),  # not mistaken for PA
            ("parana", "PR"),  # not mistaken for PA
        ],
    )
    def test_br_state_name_to_state_code(self, input_data, expected):
        assert br_state_name_to_state_code(input_data) == expected
        assert br_address_to_state_code(input_data) == expected
        assert address_to_country_and_subdivision_codes(input_data) == ("BR", expected)
        assert (
            address_to_country_and_subdivision_codes(input_data, iso_format=True)
            == "BR-" + expected
        )

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Avenida Pedro Alvares Cabral Vila Mariana, 04094-050, Brésil", "SP"),
            ("Praça da Luz, 2 – Luz, 01120-010", "SP"),
            ("Dourados, 79868-000", "MS"),
            ("99999-999", "RS"),
            ("00000-000", "SP"),
            ("59999-999", "RN"),
            ("60000-000", "CE"),
        ],
    )
    def test_br_postcode_to_state_code(self, input_data, expected):
        assert br_postcode_to_state_code(input_data) == expected
        assert br_address_to_state_code(input_data) == expected
        assert address_to_country_and_subdivision_codes(input_data) == ("BR", expected)
        assert (
            address_to_country_and_subdivision_codes(input_data, iso_format=True)
            == "BR-" + expected
        )

    @mock.patch("geoconvert.convert.BR_POSTCODES_RANGE", {})
    def test_br_postcode_to_state_code_with_no_data(self):
        # NOTE : this test has no other use than to keep a 100% coverage
        assert br_postcode_to_state_code("00000-000") is None
