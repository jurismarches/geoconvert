import re

us_states = {
    "alabama": "AL",
    "alaska": "AK",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "florida": "FL",
    "georgia": "GA",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "new york": "NY",
    "north carolina": "NC",
    "north dakota": "ND",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "pennsylvania": "PA",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    # Always keep WV before VA
    "west virginia": "WV",
    "virginia": "VA",
    # Always keep DC before WA
    "washington dc": "DC",
    "washington": "WA",
    "wisconsin": "WI",
    "wyoming": "WY",
}

US_STATES_CODES = set(us_states.values())


# Regexes

names = r"\b|\b".join(name.replace(" ", "\s") for name in us_states)
us_state_name_regex = re.compile(rf"(?P<state>\b{names}\b)", re.I)

codes = r"\b|\b".join(code for code in US_STATES_CODES)
us_state_code_regex = re.compile(rf"(?P<code>\b{codes}\b)")

us_postcode_regex = re.compile(
    rf"(?P<state_code>\b{codes}\b)"  # Positive lookbehind for a state code
    + r"\s+(?P<postcode>\b\d{5}\b)",
    re.I,
)
