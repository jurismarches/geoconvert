import re

from .united_states import US_STATES_CODES


fr_regions = {
    # New region names first (2018)
    "auvergne rhone alpes": "84",  # chef lieu: Lyon
    "bourgogne franche comte": "27",  # chef lieu: Dijon
    "centre val de loire": "24",  # chef lieu: Orleans
    "grand est": "44",  # chef lieu: strasbourg
    "hauts de france": "32",  # chef lieu: Lille
    "nouvelle aquitaine": "75",  # chef lieu: Bordeaux
    "occitanie": "76",  # chef lieu: Toulouse
    "normandie": "28",  # chef lieu: Rouen
    # Old region names second
    "alsace": "42",  # old region (pre 2016)
    "aquitaine": "72",  # old region (pre 2016)
    "auvergne": "83",  # old region (pre 2016)
    "bourgogne": "26",  # old region (pre 2016)
    "bretagne": "53",
    "centre": "24",
    "champagne ardenne": "21",  # old region (pre 2016)
    "corse": "94",
    "franche comte": "43",  # old region (pre 2016)
    "guadeloupe": "01",
    "guyane": "03",
    "ile de france": "11",
    "languedoc roussillon": "91",  # old region (pre 2016)
    "limousin": "74",  # old region (pre 2016)
    "lorraine": "41",  # old region (pre 2016)
    "martinique": "02",
    "mayotte": "06",
    "midi pyrenees": "73",  # old region (pre 2016)
    "nord pas de calais": "31",  # old region (pre 2016)
    "basse normandie": "25",  # old region (pre 2016)
    "haute normandie": "23",  # old region (pre 2016)
    "pays de la loire": "52",
    "picardie": "22",  # old region (pre 2016)
    "poitou charentes": "54",  # old region (pre 2016)
    "provence alpes cote d'azur": "93",
    "reunion": "04",
    "rhone alpes": "82",  # old region (pre 2016)
}

# Keep backward compatibility
regions = fr_regions

# Region ID => Dept chef lieu id, (List of region"s dept)
fr_principal_places = {
    "42": ("67", ["67", "68"]),
    "72": ("33", ["24", "33", "40", "47", "64"]),
    "83": ("63", ["03", "15", "43", "63"]),
    "26": ("21", ["21", "58", "71", "89"]),
    "53": ("35", ["22", "29", "35", "56"]),
    "24": ("45", ["18", "28", "36", "37", "41", "45"]),
    "21": ("51", ["08", "10", "51", "52"]),
    "94": ("20A", ["20A", "20B"]),
    "43": ("25", ["25", "39", "70", "90"]),
    "01": ("971", ["971"]),
    "03": ("973", ["973"]),
    "11": ("75", ["75", "77", "78", "91", "92", "93", "94", "95"]),
    "91": ("34", ["11", "30", "34", "48", "66"]),
    "74": ("87", ["19", "23", "87"]),
    "41": ("57", ["54", "55", "57", "88"]),
    "02": ("972", ["972"]),
    "06": ("976", ["976"]),
    "73": ("31", ["09", "12", "31", "32", "46", "65", "81", "82"]),
    "31": ("59", ["59", "62"]),
    "25": ("14", ["14", "50", "61"]),
    "23": ("76", ["27", "76"]),
    "52": ("44", ["44", "49", "53", "72", "85"]),
    "22": ("80", ["02", "60", "80"]),
    "54": ("86", ["16", "17", "79", "86"]),
    "93": ("13", ["04", "05", "06", "13", "83", "84"]),
    "04": ("974", ["974"]),
    "82": ("69", ["01", "07", "26", "38", "42", "69", "73", "74"]),
    # New regions (2016)
    "44": (  # merges 41, 42, 21
        "67",
        ["67", "68", "54", "55", "57", "88", "08", "10", "51", "52"],
    ),
    "75": (  # merges 72, 54, 74
        "33",
        ["24", "33", "40", "47", "64", "19", "23", "87", "16", "17", "79", "86"],
    ),
    "84": (  # merges 82, 83
        "69",
        ["03", "15", "43", "63", "01", "07", "26", "38", "42", "69", "73", "74"],
    ),
    "27": ("21", ["21", "58", "71", "89", "25", "39", "70", "90"]),  # merges 26, 43
    "76": (  # merges 73, 91
        "31",
        ["11", "30", "34", "48", "66", "09", "12", "31", "32", "46", "65", "81", "82"],
    ),
    "32": ("59", ["59", "62", "02", "60", "80"]),  # merges 31, 22
    "28": ("76", ["27", "76", "14", "50", "61"]),  # merges 23, 25
}

# Keep backward compatibility
principal_places = fr_principal_places

fr_departments = {
    "ain": "01",
    "aisne": "02",
    "allier": "03",
    "alpes-de-haute-provence": "04",
    # In case there is a misspell
    "alpes-de-hautes-provence": "04",
    "hautes-alpes": "05",
    "alpes-maritimes": "06",
    "ardeche": "07",
    "ardennes": "08",
    "ariege": "09",
    "aube": "10",
    "aude": "11",
    "aveyron": "12",
    "bouches-du-rhone": "13",
    "calvados": "14",
    "cantal": "15",
    "charente-maritime": "17",
    "charente": "16",
    "cher": "18",
    "correze": "19",
    "corse-du-sud": "20A",
    "haute-corse": "20B",
    "cote-d'or": "21",
    "cotes-d'armor": "22",
    "creuse": "23",
    "dordogne": "24",
    "doubs": "25",
    "drome": "26",
    # Keep 27 after 28 in that order for the dept name regex not to find
    # the first when the second is expected.
    "eure-et-loir": "28",
    "eure": "27",
    "finistere": "29",
    "gard": "30",
    "haute-garonne": "31",
    "gers": "32",
    "gironde": "33",
    "herault": "34",
    "ille-et-vilaine": "35",
    # Keep 36 after 37 in that order for the dept name regex not to find
    # the first when the second is expected.
    "indre-et-loire": "37",
    "indre": "36",
    "isere": "38",
    "jura": "39",
    "landes": "40",
    "loir-et-cher": "41",
    "haute-loire": "43",
    # Keep 42 after 44 in that order for the dept name regex not to find
    # the first when the second is expected.
    "loire-atlantique": "44",
    "loire": "42",
    "loiret": "45",
    # Keep 46 after 47 in that order for the dept name regex not to find
    # the first when the second is expected.
    "lot-et-garonne": "47",
    "lot": "46",
    "lozere": "48",
    "maine-et-loire": "49",
    "manche": "50",
    "marne": "51",
    "haute-marne": "52",
    "mayenne": "53",
    "meurthe-et-moselle": "54",
    "meuse": "55",
    "morbihan": "56",
    "moselle": "57",
    "nievre": "58",
    "nord": "59",
    "oise": "60",
    "orne": "61",
    "pas-de-calais": "62",
    "puy-de-dome": "63",
    "pyrenees-atlantiques": "64",
    # In case there is a misspell
    "pyrenees-atlantique": "64",
    "hautes-pyrenees": "65",
    "pyrenees-orientales": "66",
    "bas-rhin": "67",
    "haut-rhin": "68",
    "rhone": "69",
    "haute-saone": "70",
    "saone-et-loire": "71",
    "sarthe": "72",
    "savoie": "73",
    "haute-savoie": "74",
    "paris": "75",
    "seine-maritime": "76",
    "seine-et-marne": "77",
    "yvelines": "78",
    "deux-sevres": "79",
    "somme": "80",
    # Keep 81 after 82 in that order for the dept name regex not to find
    # the first when the second is expected.
    "tarn-et-garonne": "82",
    "tarn": "81",
    "var": "83",
    "vaucluse": "84",
    "vendee": "85",
    "vienne": "86",
    "haute-vienne": "87",
    "vosges": "88",
    "yonne": "89",
    "territoire-de-belfort": "90",
    "essonne": "91",
    "hauts-de-seine": "92",
    "seine-saint-denis": "93",
    "val-de-marne": "94",
    "val-d'oise": "95",
    "guadeloupe": "971",
    "martinique": "972",
    "guyane": "973",
    "ile-de-la-reunion": "974",
    "la-reunion": "974",
    "saint-pierre-et-miquelon": "975",
    "mayotte": "976",
    "terres-australes-et-antarctiques": "984",
    "wallis-et-futuna": "986",
    "polynesie-francaise": "987",
    "nouvelle-caledonie": "988",
}


# Keep backward compatibility
departments = fr_departments


# Regexes

names = r"\b|\b".join(name for name in fr_departments)
fr_department_name_regex = re.compile(rf"(?P<dept>\b{names}\b)", re.I)

names = r"\b|\b".join(name for name in fr_regions)
fr_region_name_regex = re.compile(rf"(?P<region>\b{names}\b)", re.I)

us_states_codes = r"\b|\b".join(code for code in US_STATES_CODES)
fr_postcode_regex = re.compile(
    r"(?<!TSA)(?<!BP)(?<!B.P.)(?<!CS)(?:[^\d]|^)(?<!TSA)(?<!BP)(?<!B.P.)(?<!CS)"
    + rf"(?<!(\b{us_states_codes}\b)\s)"
    + r"(?P<postcode>\d{2}\s?\d{3})\s*([^\d\s]|$)",
    re.I,
)
