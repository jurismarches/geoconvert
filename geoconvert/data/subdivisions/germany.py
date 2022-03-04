import re


de_landers = {
    "baden wurttemberg": "BW",
    "bayern": "BY",
    "berlin": "BE",
    "brandenburg": "BB",
    "freie hansestadt bremen": "HB",
    "hamburg": "HH",
    "hessen": "HE",
    "mecklenburg vorpommern": "MV",
    "niedersachsen": "NI",
    "nordrhein westfalen": "NW",
    "rheinland pfalz": "RP",
    "saarland": "SL",
    "sachsen anhalt": "ST",
    "sachsen": "SN",
    "schleswig holstein": "SH",
    "thuringen": "TH",
}

DE_LANDERS_CODES = set(de_landers.values())


DE_HAUPTSTADT = {
    "stuttgart": "BW",
    "munchen": "BY",
    "potsdam": "BB",
    "bremen": "HB",
    "wiesbaden": "HE",
    "frankfurt am main": "HE",
    "schwerin": "MV",
    "rostock": "MV",
    "hannover": "NI",
    "dusseldorf": "NW",
    "koln": "NW",
    "mainz": "RP",
    "saarbrucken": "SL",
    "magdeburg": "ST",
    "halle ": "ST",
    "dresden": "SN",
    "leipzig": "SN",
    "kiel": "SH",
    "erfurt": "TH",
}

# source https://simple.wikipedia.org/wiki/Postal_codes_in_Germany
DE_POSTCODE_RANGE = {
    1944: "SN",
    1990: "BB",
    2999: "SN",
    3999: "BB",
    4616: "SN",
    4617: "TH",
    4625: "SN",
    4626: "TH",
    4930: "SN",
    4931: "BB",
    4999: "SN",
    5999: "NI",
    6576: "ST",
    6577: "TH",
    6999: "ST",
    7999: "TH",
    9999: "SN",
    14999: "BE",
    16999: "BB",
    19347: "MV",
    19348: "BB",
    19999: "MV",
    21243: "HH",
    21244: "NI",
    21679: "SH",
    21730: "NI",
    21999: "SH",
    22999: "HH",
    25999: "SH",
    26999: "NI",
    28999: "HB",
    31999: "NI",
    33999: "NW",
    36999: "HE",
    37300: "NI",
    37359: "TH",
    39999: "NI",
    48999: "NW",
    49999: "NI",
    52999: "NW",
    53110: "RP",
    53229: "NW",
    53720: "RP",
    53721: "NW",
    53808: "RP",
    53809: "NW",
    54999: "RP",
    55547: "RP",
    55558: "NW",
    56999: "RP",
    57611: "NW",
    57612: "RP",
    59999: "NW",
    63915: "HE",
    63916: "BY",
    65623: "HE",
    65624: "RP",
    65999: "HE",
    66999: "SL",
    66849: "RP",
    66999: "SL",
    66879: "RP",
    66999: "SL",
    66894: "RP",
    66999: "SL",
    79999: "BW",
    87999: "BY",
    88999: "BW",
    95999: "BY",
    99999: "TH",
}


# Regexes
names = r"\b|\b".join(code for code in de_landers.keys())
de_land_name_regex = re.compile(rf"(?P<land>\b{names}\b)", re.I)

codes = r"\b|\b".join(code for code in DE_LANDERS_CODES)
de_land_code_regex = re.compile(rf"(?P<code>\b{codes}\b)")

hauptstadt = r"\b|\b".join(code for code in DE_HAUPTSTADT.keys())
de_land_hauptstadt_regex = re.compile(rf"(?P<hauptstadt>\b{hauptstadt}\b)")

de_postcode_regex = re.compile(r"\b(?P<postcode>\d{5})")
