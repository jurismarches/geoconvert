import re


br_states = {
    "acre": "AC",
    "alagoas": "AL",
    "amapa": "AP",
    "amazonas": "AM",
    "bahia": "BA",
    "ceara": "CE",
    "distrito federal": "DF",
    "espirito santo": "ES",
    "goias": "GO",
    "maranhao": "MA",
    "mato grosso do sul": "MS",
    "mato grosso": "MT",
    "minas gerais": "MG",
    "para": "PA",
    "paraiba": "PB",
    "parana": "PR",
    "pernambuco": "PE",
    "piaui": "PI",
    "rio de janeiro": "RJ",
    "rio grande do norte": "RN",
    "rio grande do sul": "RS",
    "rondonia": "RO",
    "roraima": "RR",
    "sao paulo": "SP",
    "santa catarina": "SC",
    "sergipe": "SE",
    "tocantins": "TO",
}

BR_STATES_CODES = set(br_states.values())

BR_POSTCODES_RANGE = {
    199: "SP",
    289: "RJ",
    299: "ES",
    399: "MG",
    489: "BA",
    499: "SE",
    569: "PE",
    579: "AL",
    589: "PB",
    599: "RN",
    639: "CE",
    649: "PI",
    659: "MA",
    688: "PA",
    689: "AP",
    692: "AM",
    693: "RR",
    698: "AM",
    699: "AC",
    727: "DF",
    729: "GO",
    736: "DF",
    767: "GO",
    769: "RO",
    779: "TO",
    788: "MT",
    789: "RO",
    799: "MS",
    879: "PR",
    899: "SC",
    999: "RS",
}

# Regexes

names = r"\b|\b".join(name.replace(" ", r"\s") for name in br_states)
br_state_name_regex = re.compile(rf"(?P<state>\b{names}\b)", re.I)

codes = r"\b|\b".join(code for code in BR_STATES_CODES)
br_state_code_regex = re.compile(rf"(?P<code>\b{codes}\b)")

br_postcode_regex = re.compile(r"\b(?P<postcode>\d{3})\d{2}-\d{3}\b")
