# -*- coding: utf8 -*-
import re

from utils import remove_accents
from utils import safe_string
from utils import reverse_dict

from data import regions
from data import departments
from data import principal_places
from data import countries_en
from data import countries_fr


def zipcode_to_dept_name(zipcode):
    """
    Return the departement name from a CP or the departement number
    """

    # Normalize caps and format for 20A and 20B
    zipcode = zipcode.upper()
    if zipcode in ['2A', '2B']:
        zipcode = '%s0%s' % tuple(zipcode)
    if (len(zipcode) == 5 and zipcode[:2] in departments.keys()):
        return departments[zipcode[:2]]
    elif (len(zipcode) == 5 and zipcode[:3] in departments.keys()):
        return departments[zipcode[:3]]
    elif (len(zipcode) == 6 and zipcode[2] == " ") and zipcode[:2] in departments.keys():
        return departments[zipcode[:2]]
    elif zipcode in departments.keys():
        return departments[zipcode]
    else:
        return None


def address_to_zipcode(text):
    """
    Return the departement number from any text which contains any zip code
    """

    for line in text.splitlines():
        word = re.search(r"(?<!BP)(?:[^\d]|^)(?<!BP)(\d{2}\s?\d{3}|0?[1-9]\s?\d{3})\s*([^\d\s]|$)", line, re.IGNORECASE)
        if word:
            # If postal code with whitespace (44 300)
            if word.group(1).find(' '):
                word = word.group(1).replace(' ', '')
            # Else (44300)
            else:
                word = word.group(1)
            if word[:2] != '20' and word[:3] != '978':
                try:
                    if int(word):
                        word = word.zfill(5)
                        for key in departments.keys():
                            if word[:2] == key or word[:3] == key:
                                return key
                except ValueError:
                    pass
            else:
                if word[:3] == '978':
                    return '971'  # as asked by FO for another script
                elif int(word) < 20200 or int(word) in [20223, 20900]:
                    return '20A'
                else:
                    return '20B'
    return None


def dept_name_to_zipcode(text):
    """
    Return the departement number from the departement name
    """
    if text:
        try:
            nom_dep = text.strip(' ').replace(" ", "-").lower().encode('ASCII', 'replace').replace('?', '.')
        except:
            nom_dep = text.replace(" ", "-").lower()
        for key, value in departments.items():
            if nom_dep == value:
                return key
        for key, value in departments.items():
            if re.search(nom_dep, value):
                return key
    return None


def region_id_to_name(region_id):
    if region_id:
        return regions[region_id]
    return None


def region_name_to_id(region_name):
    if region_name:
        regions_reversed = reverse_dict(regions)
        region_name = safe_string(region_name)
        try:
            return regions_reversed[region_name]
        except KeyError:
            pass
    return None


def region_info_from_id(region_id):
    if region_id:
        try:
            return principal_places[str(region_id)]
        except KeyError:
            pass
    return None


def region_info_from_name(region_name):
    region_id = region_name_to_id(region_name)
    return region_info_from_id(region_id)


def country_name_to_id(country, lang='FR'):
    """
    Get country name and return his code.
    """
    if country:
        if lang == 'EN':
            countries = countries_en
        else:
            countries = countries_fr
        # Normalize string
        country = ' %s ' % re.sub(r'\s+', ' ', remove_accents(country).lower()).strip()
        for key, value in countries.iteritems():
            if re.search(r'(\s|[^\w\s])%s(\s|[^\w\s])' % key, country):
                return value
    return None
