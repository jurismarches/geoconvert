# -*- coding: utf8 -*-
import re
from .utils import remove_accents
from .utils import safe_string
from .utils import reverse_dict

from .data import regions
from .data import departments
from .data import principal_places
from .data import countries_en
from .data import countries_fr
from .data import capitals_en
from .data import capitals_fr

try:
    from itertools import ifilter
except ImportError:
    ifilter = filter


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
        zipcode_match = re.search(r"(?<!TSA)(?<!BP)(?<!B.P.)(?<!CS)(?:[^\d]|^)(?<!TSA)(?<!BP)(?<!B.P.)(?<!CS)(?P<zipcode>\d{2}\s?\d{3})\s*([^\d\s]|$)", line, re.IGNORECASE)
        if zipcode_match:
            zipcode = zipcode_match.group('zipcode').replace(' ', '').zfill(5)

            if zipcode[:3] == '978':
                # Reunion uses 978 sometimes instead of 974
                return '974'

            elif zipcode[:3] == '977':
                # Merge St Berthelemy 97701 in Guadeloupe
                if zipcode == '97701':
                    return '971'

                # Otherwise, Reunion uses 977 sometimes instead of 974
                return '974'

            elif zipcode == '97098':
                # Merge St Berthelemy 97098 in Guadeloupe
                return '971'

            # Corse
            elif zipcode[:2] == '20':
                try:
                    if int(zipcode) < 20200 or int(zipcode) in [20223, 20900]:
                        return '20A'
                    else:
                        return '20B'
                except ValueError:
                    return None

            # Other
            else:
                return next(ifilter(lambda zc: zipcode.startswith(zc), departments.keys()), None)

    return None


# unwanted chars in dept names
_DEPT_REJECT = re.compile(r"[^\w'-]")


def dept_name_to_zipcode(text):
    """
    Return the departement number from the departement name
    """
    if text:
        try:
            if not isinstance(text, unicode):
                text = unicode(text, 'utf-8')
        except NameError:
            # unicode module doesn't exist on Python 3.X
            pass
        # replace spaces for '-'
        nom_dep = text.strip(' ').replace(" ", "-").lower()
        # remove accents
        nom_dep = remove_accents(nom_dep)
        # remove unwanted chars
        nom_dep = _DEPT_REJECT.sub('', nom_dep)
        # match
        for key, value in departments.items():
            if nom_dep == value:
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
            region_name = ' %s ' % re.sub(r'\s+', ' ', remove_accents(region_name).lower()).strip()
            search = re.search(r'(\s|[^\w\s])(%s)(\s|[^\w\s])' % '|'.join([key for key, value in regions_reversed.items()]), region_name)
            if search:
                region_name = search.group(2)
                return regions_reversed[region_name]

            return None
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

        items_found = []
        # Normalize string
        country = ' %s ' % re.sub(r'\s+', ' ', remove_accents(country).lower()).strip()
        for key, value in countries:
            if re.search(r'(\s|[^\w\s])%s(\s|[^\w\s])' % key, country):
                items_found.append((key, value))

        if items_found:
            return max(items_found, key=lambda item: len(item[0]))[1]

    return None


def capital_name_to_country_id(capital, lang='FR'):
    """
    Get capital name and return corresponding country code.
    """
    if capital:
        if lang == 'EN':
            capitals = capitals_en
        else:
            capitals = capitals_fr

        items_found = []
        # Normalize string
        capital = ' %s ' % re.sub(r'\s+', ' ', remove_accents(capital).lower()).strip()
        for key, value in capitals:
            if re.search(r'(\s|[^\w\s])%s(\s|[^\w\s])' % key, capital):
                items_found.append((key, value))

        if items_found:
            return max(items_found, key=lambda item: len(item[0]))[1]

    return None
