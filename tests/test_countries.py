import pytest

from geoconvert.convert import (
    address_to_country_code,
    country_name_to_country_code,
    country_name_to_id,
    language_to_country_names,
)
from geoconvert.utils import safe_string


class TestCountries:
    @pytest.mark.parametrize(
        "input_data, kwargs, expected",
        [
            # Look for the country name in any language available by default
            ("Deutschland", {}, "DE"),  # de
            ("Germany", {}, "DE"),  # en
            ("Allemagne", {}, "DE"),  # fr
            ("Alemanha", {}, "DE"),  # pt
            # If no country found, return None
            ("Wonderland", {}, None),
            ("Germany", {"lang": "fr"}, None),
            # No confusion with Congo ("CD")
            ("Congo (Brazzaville)", {}, "CG"),
            ("Congo (Kinshasa)", {}, "CD"),
            ("Congo", {}, "CG"),
            # No confusion with Guinea ("GN")
            # "GQ"
            ("equatorial guinea", {}, "GQ"),  # de / en
            ("aquatorialguinea", {}, "GQ"),  # es
            ("guinee equatoriale", {}, "GQ"),  # fr
            ("guine equatorial", {}, "GQ"),  # pt
            # "PG"
            ("papua neuguinea", {}, "PG"),  # de
            ("pap new guinea", {}, "PG"),  # en
            ("papua nueva guinea", {}, "PG"),  # es
            ("papouasie nouvelle guinee", {}, "PG"),  # fr
            ("papua nova guine", {}, "PG"),  # pt
            # "GW"
            ("guinea bissau", {}, "GW"),  # de / en / es
            ("guinee bissau", {}, "GW"),  # fr
            ("guine bissau", {}, "GW"),  # pt
            # No confusion with Jersey ("JE")
            ("new jersey", {}, "US"),
            # No confusion with Sudan ("SD")
            ("sudsudan", {}, "SS"),  # de
            ("south sudan", {}, "SS"),  # en
            ("sudan del sur", {}, "SS"),  # es
            ("Soudan du Sud", {}, "SS"),  # fr
            ("sudao do sul", {}, "SS"),  # pt
            # No confusion with Iceland, which spells "Island" in German ("IS")
            ("Cayman islands", {}, "KY"),  # en
            ("Christmas island", {}, "CX"),  #en
            ("Bouvet Island", {}, "BV"),  # en
            ("Heard Island", {}, "HM"),  # en
            ("Norfolk Island", {}, "NF"),  # en
            ("Solomon Islands", {}, "SB"),  # en
            # However, in cases where island is singular instead of plural,
            # there can be confusion.
            ("Solomon Island Nationals", {}, "IS"),  # en
            # Any capitalization for lang works
            ("Germany", {"lang": "en"}, "DE"),
            ("Germany", {"lang": "En"}, "DE"),
            ("Germany", {"lang": "EN"}, "DE"),
            ("Germany", {"lang": "eN"}, "DE"),
        ],
    )
    def test_country_name_to_country_code(self, input_data, kwargs, expected):
        assert country_name_to_country_code(input_data, **kwargs) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("france", "FR"),
            ("Comores", "KM"),
            ("Madagascar", "MG"),
            (u"S\xe9n\xe9gal", "SN"),
            ("République démocratique du Congo", "CD"),
            ("Mali", "ML"),
            ("Sri Lanka ", "LK"),
            (u"\xa0V\xe9n\xe9zuela\xa0", "VE"),
            (u"Vi\xeatnam", "VN"),
            ("Nigeria", "NG"),
            (u"Niger", "NE"),
            (u"aaa ( bbb", None),
            (u" Le  nigéria c'est trop   sympa", "NG"),
            (u"Pays d'exécution : Niger", "NE"),
            ("  Côte d'Ivoire ", "CI"),
            ("  Côte d’Ivoire ", "CI"),  # with accent for apostrophe
            ("U.S. Mission Iraq\n\nIraq", "IQ"),
            ("Pays:France ?".encode("ascii", "ignore"), "FR"),
            (",royaume-uni,", "GB"),
            (u"trinité-et-Tobago", "TT"),
            ("surinam", "SR"),
            (u"saint-barthélemy", "BL"),
            (u"saint-barthélemy", "BL"),
            ("sint maarten", "SX"),
            (u"curaçao", "CW"),
            ("andorre", "AD"),
            ("bonaire, saint-eustache et saba", "BQ"),
            ("soudan", "SD"),
            ("soudan du sud", "SS"),
            ("PAYS-BRÉSIL", "BR"),
            (u"Lorem ipsum Libye - LIBYE", "LY"),
            ("palestine", "PS"),
            ("Congo (Brazzaville)", "CG"),
            ("Congo (Kinshasa)", "CD"),
            ("São tome & principe ", "ST"),
            ("Papouasie Nouvelle Guinée", "PG"),
        ],
    )
    def test_country_name_to_country_code_fr(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="fr") == expected
        assert country_name_to_id(input_data, lang="fr") == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Mongolia", "MN"),
            ("Marocco", "MA"),
            ("Georgia", "GE"),
            ("kosovo", "KO"),
            ("Namibia", "NA"),
            ("Venezuela", "VE"),
            ("Armenia", "AM"),
            ("sweden", "SE"),
            (u"Knotts Island, NC 27950\n\n27950-0039\nUnited States", "US"),
            (
                "721 APS BLDG 3334\nUNIT 3295 \nRamstein Air Base, Non-U.S. 66877 \nGermany ",
                "DE",
            ),
            ("Saudi Arabia", "SA"),
            ("Country execution:nigeria.", "NG"),
            ("RUSSIA", "RU"),
            ("PAPUA NEW GUINEA", "PG"),
            ("guinea-bissau", "GW"),
            ("netherlands antilles", "AN"),
            ("netherlands or something", "NL"),
            (u"curaçao", "CW"),
            (u"saint barthélemy", "BL"),
            ("Sudan", "SD"),
            ("South Sudan", "SS"),
            ("tanzania", "TZ"),
            ("united states minor outlying islands", "UM"),
            ("Lorem ipsum Libya - LIBYA", "LY"),
            (" Democratic Republic of the Congo", "CD"),
            ("CONGO, DEM. REPUBLIC", "CD"),
            ("TIMOR LESTE", "TL"),
            ("state of palestine", "PS"),
            ("palestine, state of", "PS"),
        ],
    )
    def test_country_name_to_country_code_en(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="EN") == expected
        assert country_name_to_id(input_data, lang="EN") == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Dänemark", "DK"),
            ("weißrussland", "BY"),
            ("Demokratische Republik Kongo", "CD"),
            ("korea, süd", "KR"),
            ("libanon", "LB"),
            ("são tomé und príncipe", "ST"),
            ("schweden", "SE"),
            ("schweiz", "CH"),
            ("st. vincent und die grenadinen", "VC"),
            ("Korea, Nord", "KP"),
            ("Lorem Ipsum, Bundesstaat Kanada ", "CA"),
            ("   Palästina      ", "PS"),
            ("Bundesstaat, der Palastina", "PS"),
            ("frankreich einstaten", "FR"),
            ("DOMINICA!!", "DM"),
            (u"   Land der Hinrichtung : Deutschland", "DE"),
            ("Dschibuti-Stadt", "DJ"),
            ("elfenbeinküste und ecuador    ", "CI"),
        ],
    )
    def test_country_name_to_country_code_de(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="DE") == expected
        assert country_name_to_id(input_data, lang="DE") == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Afeganistão", "AF"),
            ("África do Sul", "ZA"),
            ("Albânia", "AL"),
            ("Butão", "BT"),
            ("Camarões", "CM"),
            ("República Centro-Africana", "CF"),
            ("Grécia", "GR"),
            ("Lituânia", "LT"),
            ("Estados Federados da Micronésia", "FM"),
            ("Nigéria!!", "NG"),
            ("Lorem Ipsum, país Níger ", "NE"),
            ("   Panamá      ", "PA"),
            ("o país do peru", "PE"),
            (u"País de execução: Polónia", "PL"),
            ("São Vicente e Granadinas    ", "VC"),
            ("Guine bissau", "GW"),
        ],
    )
    def test_country_name_to_country_code_pt(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="PT") == expected
        assert country_name_to_id(input_data, lang="PT") == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Los Emiratos Árabes Unidos", "AE"),
            ("  Islas   Vírgenes   Británicas   ", "VG"),
            ("Turkménistan\n", "TM"),
            ("España!", "ES"),
            ("Egipto", "EG"),
            ("groenlandia", "GL"),
            ("Camboya", "KH"),
            ("Isla de Mauricio", "MU"),
            ("San Cristóbal y Nieves", "KN"),
            ("Nueva Zelanda", "NZ"),
            ("Países Bajos ", "NL"),
            ("Kirguistán", "KG"),
            ("suiza", "CH"),
            ("Tayikistán", "TJ"),
            ("Tailandia", "TH"),
        ],
    )
    def test_country_name_to_country_code_es(self, input_data, expected):
        assert country_name_to_country_code(input_data, lang="ES") == expected
        assert country_name_to_id(input_data, lang="ES") == expected

    def test_country_name_to_country_code_with_unknown_language(self):
        unknown_lang = "it"
        # If this breaks, this is because the language was added.
        # Just choose another unkown language and use another example.
        assert unknown_lang not in language_to_country_names
        assert country_name_to_country_code("Italia", lang=unknown_lang) is None

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("2 pl. Saint-Pierre, 44000 Nantes, France", "FR"),
            ("1196 Voie Camillien-Houde, Montréal, QC H3H 1A1, Canada", "CA"),
            ("Los Angeles, CA\nUnited States", "US"),
            ("Cabul, Afeganistão", "AF"),
            ("Try to find South Sudan in an address", "SS"),
            ("650 Great Rd, Princeton, New Jersey", "US"),
            ("St Peter, Jersey JE1 1BY, Jersey", "JE"),
            ("East Asia and Pacific Region: Papua New Guinea", "PG"),
            ("N1, Conakry, Guinea", "GN"),
            # The country code can be found using the capital name in any available language
            ("Kairo", "EG"),
            ("Paris", "FR"),
            ("Washington D.C.", "US"),
            ("Ottawa", "CA"),
            # If no country code is found, nothing is returned.
            ("", None),
            ("2 pl. Saint-Pierre, 44000 Nantes", None),
            (
                "Av. Pres. Castelo Branco, Portão 3 - Maracanã",
                None,
            ),
        ],
    )
    def test_address_to_country_code(self, input_data, expected):
        assert address_to_country_code(input_data) == expected

    def test_each_country_name_in_data_is_a_safe_string(self):
        """
        If there is one country name which is not a safe string,
        replace that name by the safe one in data.
        """
        for lang, country_names in language_to_country_names.items():
            for name in country_names:
                assert safe_string(name) == name
