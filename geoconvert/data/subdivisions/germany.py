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


# Regexes
names = r"\b|\b".join(code for code in de_landers.keys())
de_land_name_regex = re.compile(rf"(?P<land>\b{names}\b)", re.I)

codes = r"\b|\b".join(code for code in DE_LANDERS_CODES)
de_land_code_regex = re.compile(rf"(?P<code>\b{codes}\b)")

hauptstadt = r"\b|\b".join(code for code in DE_HAUPTSTADT.keys())
de_land_hauptstadt_regex = re.compile(rf"(?P<hauptstadt>\b{hauptstadt}\b)")
