import re


ca_provinces = {
    "yukon": "YT",
    "territoires du nord ouest": "NT",
    "northwest territories": "NT",
    "nunavut": "NU",
    "quebec": "QC",
    "terre neuve et labrador": "NL",
    "newfoundland and labrador": "NL",
    "colombie britannique": "BC",
    "british columbia": "BC",
    "alberta": "AB",
    "saskatchewan": "SK",
    "manitoba": "MB",
    "ontario": "ON",
    "nouveau brunswick": "NB",
    "new brunswick": "NB",
    "ile du prince edouard": "PE",
    "prince edward island": "PE",
    "nouvelle ecosse": "NS",
    "nova scotia": "NS",
}

CA_PROVINCES_CODES = set(ca_provinces.values())

# From https://en.wikipedia.org/wiki/Postal_codes_in_Canada#Table_of_all_postal_codes
# Note that the same first letter is used for Nunavut and Northwest Territories,
# so we have to treat those cases separately.
CA_POSTCODE_FIRST_LETTER_TO_PROVINCE_CODE = {
    "a": "NL",
    "b": "NS",
    "c": "PE",
    "e": "NB",
    "g": "QC",
    "h": "QC",
    "j": "QC",
    "k": "ON",
    "l": "ON",
    "m": "ON",
    "n": "ON",
    "p": "ON",
    "r": "MB",
    "s": "SK",
    "t": "AB",
    "v": "BC",
    "y": "YT",
}


# Regexes

names = r"\b|\b".join(name.replace(" ", r"\s") for name in ca_provinces)
ca_province_name_regex = re.compile(rf"(?P<province>\b{names}\b)", re.I)

codes = r"\b|\b".join(code for code in CA_PROVINCES_CODES)
ca_province_code_regex = re.compile(rf"(?P<code>\b{codes}\b)")

ca_postcode_regex = re.compile(r"(?P<postcode>\b\w\d\w\s?\d\w\d\b)", re.I)
