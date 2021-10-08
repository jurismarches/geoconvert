import pytest

from geoconvert.convert import (
    fr_region_id_to_info,
    fr_region_name_to_id,
    fr_region_name_to_info,
    region_info_from_id,
    region_info_from_name,
    region_name_to_id,
)


class TestFrance:
    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("73", ("31", ["09", "12", "31", "32", "46", "65", "81", "82"])),
            ("06", ("976", ["976"])),
            (6, ("976", ["976"])),
            ("6", ("976", ["976"])),
            ("24", ("45", ["18", "28", "36", "37", "41", "45"])),
            ("22", ("80", ["02", "60", "80"])),
            (
                "93",
                ("13", ["04", "05", "06", "13", "83", "84"]),
            ),
            ("", None),
            (None, None),
        ],
    )
    def test_fr_region_id_to_info(self, input_data, expected):
        assert fr_region_id_to_info(input_data) == expected
        assert region_info_from_id(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Bienvenue en bourgogne franche comté", "27"),
            ("midi pyrénées", "73"),
            ("grand est", "44"),
            (u"mayotte ", "06"),
            (u"Centre val de Loire", "24"),
            (u"Picardie ", "22"),
            (u"provence alpes côte d'azur", "93"),
            (u"", None),
            (u"hauts de france", "32"),
            (u"auvergne rhône alpes", "84"),
            (u"nouvelle aquitaine", "75"),
            (u"La guadeloupe, une superbe région", "01"),
            (u"VICE-RECTORAT DE MAYOTTE ( DCS)", "06"),
        ],
    )
    def test_fr_region_name_to_id(self, input_data, expected):
        assert fr_region_name_to_id(input_data) == expected
        assert region_name_to_id(input_data) == expected

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            (
                "Bienvenue en bourgogne franche comté",
                ("21", ["21", "58", "71", "89", "25", "39", "70", "90"]),
            ),
            ("midi pyrénées", ("31", ["09", "12", "31", "32", "46", "65", "81", "82"])),
            (
                "grand est",
                ("67", ["67", "68", "54", "55", "57", "88", "08", "10", "51", "52"]),
            ),
            (u"mayotte ", ("976", ["976"])),
            (u"Centre val de Loire", ("45", ["18", "28", "36", "37", "41", "45"])),
            (u"Picardie ", ("80", ["02", "60", "80"])),
            (
                u"provence alpes côte d'azur",
                ("13", ["04", "05", "06", "13", "83", "84"]),
            ),
            (u"", None),
            (u"hauts de france", ("59", ["59", "62", "02", "60", "80"])),
            (
                u"auvergne rhône alpes",
                (
                    "69",
                    [
                        "03",
                        "15",
                        "43",
                        "63",
                        "01",
                        "07",
                        "26",
                        "38",
                        "42",
                        "69",
                        "73",
                        "74",
                    ],
                ),
            ),
            (
                u"nouvelle aquitaine",
                (
                    "33",
                    [
                        "24",
                        "33",
                        "40",
                        "47",
                        "64",
                        "19",
                        "23",
                        "87",
                        "16",
                        "17",
                        "79",
                        "86",
                    ],
                ),
            ),
            (u"La guadeloupe, une superbe région", ("971", ["971"])),
            (u"VICE-RECTORAT DE MAYOTTE ( DCS)", ("976", ["976"])),
            (
                "Les Pays de la Loire, une superbe région",
                ("44", ["44", "49", "53", "72", "85"]),
            ),
        ],
    )
    def test_fr_region_name_to_info(self, input_data, expected):
        assert fr_region_name_to_info(input_data) == expected
        assert region_info_from_name(input_data) == expected
