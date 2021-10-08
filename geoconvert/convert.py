# -*- coding: utf-8 -*-
import re

from .data import (
    br_postcode_regex,
    BR_POSTCODES_RANGE,
    br_state_code_regex,
    br_state_name_regex,
    br_states,
    CA_POSTCODE_FIRST_LETTER_TO_PROVINCE_CODE,
    ca_postcode_regex,
    ca_province_code_regex,
    ca_province_name_regex,
    ca_provinces,
    DE_HAUPTSTADT,
    de_land_code_regex,
    de_land_hauptstadt_regex,
    de_land_name_regex,
    de_landers,
    fr_department_name_regex,
    fr_departments,
    fr_postcode_regex,
    fr_principal_places,
    fr_region_name_regex,
    fr_regions,
    language_to_capital_names,
    language_to_country_names,
    us_postcode_regex,
    us_state_code_regex,
    us_state_name_regex,
    us_states,
)
from .utils import safe_string


# BRAZIL


def br_address_to_state_code(text):
    # First, look for the postcode and derive the state code from it
    code = br_postcode_to_state_code(text)
    if code is not None:
        return code
    # Look for the state name in plain text
    state_code = br_state_name_to_state_code(text)
    if state_code:
        return state_code
    # Look for the state code in the plain text
    code_match = re.search(br_state_code_regex, text)
    if code_match:
        return code_match.group("code").upper()


def br_state_name_to_state_code(text):
    text = safe_string(text)

    # Quickly reach conclusion if possible
    if text in br_states:
        return br_states[text]

    # Otherwise use a regex
    state_name_match = re.search(br_state_name_regex, text)
    if state_name_match:
        state_name = state_name_match.group("state")
        return br_states[state_name]


def br_postcode_to_state_code(text):
    # An american postcode is made of 5 digit preceded by the state code
    br_postcode_match = re.search(br_postcode_regex, text)
    if not br_postcode_match:
        return
    
    postcode = int(br_postcode_match.group("postcode"))
    state_code = None
    for max_range, state_code in BR_POSTCODES_RANGE.items():
        if max_range >= postcode:
            break
    return state_code


# CANADA


def ca_address_to_province_code(text):
    # First, look for the postcode and derive the province code from it
    code = ca_postcode_to_province_code(text)
    if code is not None:
        return code
    # Look for the province name in the plain text
    code = ca_province_name_to_province_code(text)
    if code is not None:
        return code
    # Look for the province code in the plain text
    code_match = re.search(ca_province_code_regex, text)
    if code_match:
        return code_match.group("code").upper()


def ca_postcode_to_province_code(text):
    text = safe_string(text)
    # A Canadian postcode looks like "H0H 0H0".
    ca_postcode_match = re.search(ca_postcode_regex, text)
    if ca_postcode_match:
        ca_postcode = ca_postcode_match.group("postcode")
        if ca_postcode.startswith("x"):
            # Postcodes starting with an "x" may mean Nunavut or
            # Northest Territories.
            if ca_postcode[1:3] in ["0a", "0b", "0c"]:
                return ca_provinces["nunavut"]
            else:
                return ca_provinces["northwest territories"]
        else:
            # In every other case, the first letter of the postcode
            # allows to find the related province or territory.
            return CA_POSTCODE_FIRST_LETTER_TO_PROVINCE_CODE.get(ca_postcode[0])


def ca_province_name_to_province_code(text):
    text = safe_string(text)

    # Quickly reach conclusion if possible
    if text in ca_provinces:
        return ca_provinces[text]

    # Otherwise use a regex
    province_name_match = re.search(ca_province_name_regex, text)
    if province_name_match:
        province_name = province_name_match.group("province")
        return ca_provinces[province_name]


# GERMANY


def de_address_to_land_code(text):
    # Look for the land name in the plain text
    code = de_land_name_to_land_code(text)
    if code:
        return code
    # Look for the land hauptstadt in the plain text
    code = de_hauptstadt_to_land_code(text)
    if code:
        return code
    # Look for the land code in the plain text
    code_match = re.search(de_land_code_regex, text)
    if code_match:
        return code_match.group("code").upper()


def de_hauptstadt_to_land_code(text):
    text = safe_string(text)

    # Quickly reach conclusion if possible
    if text in DE_HAUPTSTADT.keys():
        return DE_HAUPTSTADT[text]

    # Otherwise use a regex
    hauptstadt_match = re.search(de_land_hauptstadt_regex, text)
    if hauptstadt_match:
        land_name = hauptstadt_match.group("hauptstadt")
        return DE_HAUPTSTADT[land_name]


def de_land_name_to_land_code(text):
    text = safe_string(text)

    # Quickly reach conclusion if possible
    if text in de_landers:
        return de_landers[text]

    # Otherwise use a regex
    land_name_match = re.search(de_land_name_regex, text)
    if land_name_match:
        land_name = land_name_match.group("land")
        return de_landers[land_name]

# USA


def us_address_to_state_code(text):
    # First, look for the postcode and derive the state code from it
    code = us_postcode_to_state_code(text)
    if code is not None:
        return code
    # Look for the state name in plain text
    state_code = us_state_name_to_state_code(text)
    if state_code:
        return state_code
    # Look for the state code in the plain text
    code_match = re.search(us_state_code_regex, text)
    if code_match:
        return code_match.group("code").upper()


def us_state_name_to_state_code(text):
    text = safe_string(text)

    # Quickly reach conclusion if possible
    if text in us_states:
        return us_states[text]

    # Otherwise use a regex
    state_name_match = re.search(us_state_name_regex, text)
    if state_name_match:
        state_name = state_name_match.group("state")
        return us_states[state_name]


def us_postcode_to_state_code(text):
    text = safe_string(text)
    # An american postcode is made of 5 digit preceded by the state code
    us_postcode_match = re.search(us_postcode_regex, text)
    if us_postcode_match:
        return us_postcode_match.group("state_code").upper()


# FRANCE


def fr_address_to_dept_code(text):
    # First, look for the postcode and derive the dept code from it
    code = fr_postcode_to_dept_code(text)
    if code is not None:
        return code
    # Look for the dept name in plain text
    return fr_dept_name_to_dept_code(text)


def fr_postcode_to_dept_code(text):
    postcode_match = re.search(fr_postcode_regex, text)
    if postcode_match:
        postcode = postcode_match.group("postcode").replace(" ", "").zfill(5)

        # Let us treat special cases first

        # St Barthelemy (97701 or 97098)
        if postcode in ("97701", "97098"):
            return "977"

        # 978 or 977 may be used for Réunion: let's turn that into 974
        if postcode[:3] in ("977", "978"):
            return "974"

        # Corse
        if postcode[:2] == "20":
            if int(postcode) < 20200 or int(postcode) in [20223, 20900]:
                return "20A"
            else:
                return "20B"

        # Other cases
        for code in (postcode[:2], postcode[:3]):
            if code in fr_departments.values():
                return code


# Keep backward compatibility
address_to_zipcode = fr_postcode_to_dept_code


def fr_dept_name_to_dept_code(text):
    """
    Return the departement number from the departement name
    """
    # There is no space in french dept names, but hyphens instead.
    text = safe_string(text).replace(" ", "-")

    # Quickly reach conclusion if possible
    if text in fr_departments:
        return fr_departments[text]

    # Otherwise use a regex
    dept_name_match = re.search(fr_department_name_regex, text)
    if dept_name_match:
        dept_name = dept_name_match.group("dept")
        return fr_departments[dept_name]


# Keep backward compatibility
dept_name_to_zipcode = fr_dept_name_to_dept_code


def fr_region_name_to_id(text):
    text = safe_string(text)

    # Quickly reach conclusion if possible
    if text in fr_regions:
        return fr_regions[text]

    # Otherwise use a regex
    region_name_match = re.search(fr_region_name_regex, text)
    if region_name_match:
        region_name = region_name_match.group("region")
        return fr_regions[region_name]


# Keep backward compatibility
region_name_to_id = fr_region_name_to_id


def fr_region_id_to_info(region_id):
    region_id = str(region_id).zfill(2)
    if region_id in fr_principal_places:
        return fr_principal_places[region_id]


# Keep backward compatibility
region_info_from_id = fr_region_id_to_info


def fr_region_name_to_info(region_name):
    region_id = fr_region_name_to_id(region_name)
    if region_id:
        return fr_region_id_to_info(region_id)


# Keep backward compatibility
region_info_from_name = fr_region_name_to_info


# GLOBAL


def country_name_to_country_code(text, lang=None):
    """
    Get country name and return his code.

    We go through all languages by default:
    >>> country_name_to_country_code("Deutschland")  # de
    'DE'
    >>> country_name_to_country_code("Germany")  # en
    'DE'
    >>> country_name_to_country_code("Allemagne")  # fr
    'DE'
    >>> country_name_to_country_code("Alemanha")  # pt
    'DE'

    You may specify the language to make it more efficient to get the
    country code, but you must use the correct language to get a match:
    >>> country_name_to_country_code("Allemagne", lang="fr")
    'DE'
    >>> country_name_to_country_code("Allemagne", lang="de")

    There are no errors nor warnings when the language is unknown:
    >>> country_name_to_country_code("Germania", lang="it")
    """
    return _full_name_to_country_code(text, lang, language_to_country_names)


# Keep backward compatibility
country_name_to_id = country_name_to_country_code


def capital_name_to_country_code(text, lang=None):
    """
    Find the corresponding country code from the capital name.
    """
    return _full_name_to_country_code(text, lang, language_to_capital_names)


def _full_name_to_country_code(text, lang, language_to_full_names):
    """
    Find the corresponding country code from the capital name.
    """
    # Make sure the text has the expected format
    text = safe_string(text)
    if not text:
        return

    # Find the languages to be used use to find the country code
    if lang and lang.lower() in language_to_full_names:
        # Use just the given language when it is available.
        language_to_full_names = {lang: language_to_full_names[lang.lower()]}
    elif lang is not None:
        # If the language is unknown, just do not use any language.
        language_to_full_names = {}

    for lang, full_names in language_to_full_names.items():
        country_code = _full_name_to_country_code_for_lang(text, lang, full_names)
        if country_code:
            return country_code


def _full_name_to_country_code_for_lang(text, lang, full_names):
    # Quickly reach conclusion if possible
    if text in full_names:
        return full_names[text]

    # Otherwise use a regex
    items_found = []
    for name, code in full_names.items():
        if re.search(rf"(\s|[^\w\s]|\b){name}(\s|[^\w\s]|\b)", text):
            items_found.append((name, code))
    if items_found:
        return max(items_found, key=lambda item: len(item[0]))[1]


# Keep backward compatibility
capital_name_to_country_id = capital_name_to_country_code


def address_to_country_code(text, lang=None):
    """
    Return the country code from the address. If nothing is found, None
    is returned.

    The country code can be found via the country or capital name in any
    available language if lang is None, otherwise all available
    languages are used.

    All languages available in geoconvert are used by default:
    >>> address_to_country_code("Bienvenue à Kinshasa")  # FR
    'CD'
    >>> address_to_country_code("Welcome to Cyprus")  # EN
    'CY'
    >>> address_to_country_code("Willkommen bei Kairo")  # DE
    'EG'
    >>> address_to_country_code("Bem vindo ao Afeganistão")  # PT
    'AF'

    You may use a specific language to go faster, but you'll lose the
    genericity of the result for any available language.
    >>> address_to_country_code("Ungarn", lang="us")
    >>> address_to_country_code("Ungarn", lang="de")
    'HU'
    """
    # Look for the country code from the country name first.
    country_code = country_name_to_country_code(text, lang)
    if country_code:
        return country_code

    # Look for the country code from the capital name second.
    country_code = capital_name_to_country_code(text, lang)
    if country_code:
        return country_code

    # Go through all countries, one after the other, to guess the country
    # from a subdivision (but only via safe-enough means of identifying
    # the subdivision)
    country_code, _ = _guess_subdivision_then_country_codes(text)
    return country_code


# Here are the lookup functions to use when the country is known.
# This means that we can use all possible ways to find subdivisions
# for that given country, because the user explicitly said which country
# the input text comes from.
country_to_subdivision_lookup_function = {
    "BR": br_address_to_state_code,
    "CA": ca_address_to_province_code,
    "FR": fr_address_to_dept_code,
    "DE": de_address_to_land_code,
    "US": us_address_to_state_code,
}

# Here are the lookup functions to use when the country is unknown.
# This makes sure that only safe functions, with almost zero risk of
# confusion between countries, are used.
# For instance, here, compared to country_to_subdivision_lookup_function,
# it lacks:
# - Canadian province matching with province code.
#   For instance, "Toronto, ON" does not give "ON",
#   because otherwise "ON A SOIF!" would also give "ON".
# - US state matching via province code.
#   For instance, "Bridgeville, DE" must not give "DE" when the country
#   is unknown, otherwise "RIO DE JANEIRO" would alose give "DE".
# - Brazilian state matching via province code
#   For instance MS can be Mato Grosso do Sul or Mississippi
# - French postcode matching, because 5-digit postcodes are used in
#   many countries.
# - German postcode matching, because 5-digit postcodes are used in
#   many countries and the postcodes do not follow landers boudaries
country_to_safe_subdivision_lookup_function = (
    ("BR", br_state_name_to_state_code),
    ("BR", br_postcode_to_state_code),
    ("CA", ca_postcode_to_province_code),
    ("CA", ca_province_name_to_province_code),
    ("FR", fr_dept_name_to_dept_code),
    ("DE", de_address_to_land_code),
    ("US", us_postcode_to_state_code),
    ("US", us_state_name_to_state_code),
)


def address_to_subdivision_code(text, country=None):
    """
    Return the subdivision code given an address. If nothing is found,
    None is returned.

    You can use any type of capitalization for country.
    Specifying a country should only

    The subdivision code returned depends on the country:
    - for Canada: province or territories code
    - for France: department code
    - for USA: state code

    >>> address_to_subdivision_code("2 pl. Saint-Pierre, 44000 Nantes, France")
    '44'
    >>> address_to_subdivision_code("1196 Voie Camillien-Houde, Montréal, QC H3H 1A1")
    'QC'
    >>> address_to_subdivision_code("Los Angeles, CA 90068, États-Unis")
    'CA'

    If no subdivision is found for the given country, nothing is returned:
    >>> address_to_subdivision_code("")
    >>> address_to_subdivision_code("2 pl. Saint-Pierre, 44000 Nantes", country="ca")

    There should not be false positives between French and American postcodes:
    >>> address_to_subdivision_code("2 pl. Saint-Pierre, 44000 Nantes", country="us")
    >>> address_to_subdivision_code("Los Angeles, CA 90068, États-Unis", country="fr")
    """
    # Find the subdivision code according to the country.
    if country:
        country = country.upper()
        if country in country_to_subdivision_lookup_function:
            return country_to_subdivision_lookup_function[country](text)
    else:
        # Go through all countries, one after the other, while no result
        # is found.
        _, subdivision_code = _guess_country_and_subdivision_codes(text)
        return subdivision_code


def _address_to_country_and_subdivision_codes(text, lang, country):
    """
    Hidden function to be used by address_to_country_and_subdivision_codes
    """
    if country:
        country = country.upper()
        # If a country is given, look for the subdivision of that specific country
        if country in country_to_subdivision_lookup_function:
            subdivision_code = address_to_subdivision_code(text, country=country)
            if subdivision_code:
                # If a subdivision is found,
                # return it with the corresponding country code
                return (country, subdivision_code)
        # If no subdivision can be found for the given country,
        # try and look for a country code from the input text,
        # and return it if it matches the one given by the user.
        country_code = address_to_country_code(text, lang)
        if country_code == country:
            return (country_code, None)
    else:
        return _guess_country_and_subdivision_codes(text, lang)

    return (None, None)


def address_to_country_and_subdivision_codes(text, lang=None, country=None, iso_format=False):
    """
    Return the country and subdivision code from the address.

    The country code is found using the country or the capital name in
    any available language if lang is None.
    Otherwise, only the given language is used.

    The subdivision code returned depends on the country:
    - for Canada: province or territories code
    - for France: department code
    - for USA: state code

    All available languages and countries are used by default:
    >>> address_to_country_and_subdivision_codes("Paris")
    ('FR', '75')
    >>> address_to_country_and_subdivision_codes(
    ...     "1196 Voie Camillien-Houde, Montréal, QC H3H 1A1"
    ... )
    ('CA', 'QC')
    >>> address_to_country_and_subdivision_codes("Los Angeles, CA\\nUnited States")
    ('US', 'CA')

    You may specify the country or the language:
    >>> address_to_country_and_subdivision_codes("Los Angeles, CA", country="US")
    ('US', 'CA')
    >>> address_to_country_and_subdivision_codes("Los Angeles, CA\\nEstados Unidos", lang="pt")
    ('US', 'CA')

    If no subdivision is found for the given country, the country is still searched
    in plain text:
    >>> address_to_country_and_subdivision_codes("Los Angeles, \\nEstados Unidos", country="US")
    ('US', None)
    >>> address_to_country_and_subdivision_codes("Paris, France", country="US")
    (None, None)

    A subdivision code might not always be found:
    >>> address_to_country_and_subdivision_codes("Ottawa")
    ('CA', None)
    >>> address_to_country_and_subdivision_codes("Kairo")
    ('EG', None)

    If no country is found, then no subdivision country can be found:
    >>> address_to_country_and_subdivision_codes("")
    (None, None)
    >>> address_to_country_and_subdivision_codes("2 pl. Saint-Pierre, Nantes")
    (None, None)

    There should be no confusion between French and US postcodes:
    >>> address_to_country_and_subdivision_codes("2 pl. Saint-Pierre, 44000 Nantes", country="US")
    (None, None)
    >>> address_to_country_and_subdivision_codes("6931 Rings Rd, Amlin, OH 43002", country="FR")
    (None, None)

    You can choose to get results in a tuple or in iso format
    >>> address_to_country_and_subdivision_codes("14467 Potsdam")
    ('DE', 'BB')
    >>> address_to_country_and_subdivision_codes("14467 Potsdam", iso_format=True)
    'DE-BB'
    >>> address_to_country_and_subdivision_codes("14467 Germany")
    ('DE', None)
    >>> address_to_country_and_subdivision_codes("14467 Germany", iso_format=True)
    'DE'
    """
    result = _address_to_country_and_subdivision_codes(text, lang, country)
    if iso_format:
        if result[1]:
            return '-'.join(result)
        return result[0]
    return result


def _guess_country_and_subdivision_codes(text, lang=None):
    """
    Just guess the subdivision when no country is explicitly given.
    """
    country_code, subdivision_code = _guess_country_then_subdivision_codes(text, lang)
    if country_code is not None:
        return country_code, subdivision_code
    return _guess_subdivision_then_country_codes(text)


def _guess_country_then_subdivision_codes(text, lang=None):
    """
    Guess the country code from the input text first,
    then look for the subdivision code for that country.
    """
    country_code = address_to_country_code(text, lang)
    if country_code:
        return country_code, address_to_subdivision_code(text, country=country_code)

    return (None, None)


def _guess_subdivision_then_country_codes(text):
    """
    If no countries are found in plain text, just guess the
    subdivision by looping through all available countries.
    Stop at the first subdivision code found.
    """
    for (
        country_code,
        safe_subdivision_lookup_function,
    ) in country_to_safe_subdivision_lookup_function:
        subdivision_code = safe_subdivision_lookup_function(text)
        if subdivision_code:
            return (country_code, subdivision_code)

    return (None, None)
