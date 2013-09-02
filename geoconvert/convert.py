# -*- coding: utf8 -*-
import re
import string

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

    >>> zipcode_to_dept_name('121')

    >>> zipcode_to_dept_name('44000')
    'loire-atlantique'

    >>> zipcode_to_dept_name('2a')
    'corse-du-sud'

    >>> zipcode_to_dept_name('2A')
    'corse-du-sud'

    >>> zipcode_to_dept_name('20A')
    'corse-du-sud'

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

    >>> address_to_zipcode(u"Chemin du Solarium\\n Le Haut Vigneau\\n 33175 GRADIGNAN CEDEX")
    '33'

    >>> address_to_zipcode("Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ")
    '33'

    >>> address_to_zipcode("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589")
    '33'

    >>> address_to_zipcode("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX")
    '33'

    >>> address_to_zipcode('7 cours Grandval\\nBP 414 - 20183 AJACCIO - CEDEX')
    '20A'

    >>> address_to_zipcode('20212   Erbajolo')
    '20B'

    >>> address_to_zipcode('20223   Solenzara Air')
    '20A'

    >>> address_to_zipcode('BP 55342 20223   Solenzara Air')
    '20A'

    >>> address_to_zipcode('Chemin du Solarium Le Haut Vigneau 33 175 GRADIGNAN CEDEX')
    '33'

    >>> address_to_zipcode('20 223   Solenzara Air')
    '20A'

    >>> address_to_zipcode('97821 Le Port Cedex')
    '971'

    >>> address_to_zipcode('27006 Évreux Cedex')
    '27'

    >>> address_to_zipcode('  27006 Évreux Cedex')
    '27'

    >>> address_to_zipcode('27006')
    '27'

    >>> address_to_zipcode('Roissy-en-France95700')
    '95'

    >>> address_to_zipcode(' 44200 BP 10720 Nantes cedex')
    '44'

    >>> address_to_zipcode('a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse')
    '31'

    >>> address_to_zipcode('a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse')
    '31'
    """

    # Test de text de caracteres passée en parametre
    for line in text.splitlines():
        word = re.search(r"(?<!BP)(?:[^\d]|^)(?<!BP)(\d{2}\s?\d{3})\s*([^\d\s]|$)", line)
        if word:
            # If postal code with whitespace (44 300)
            if word.group(1).find(' '):
                word = word.group(1).replace(' ', '')
            # Else (44300)
            else:
                word = word.group(1)
            if word[:2] != '20' and word[:3] != '978':
                try:
                    if int(word) and len(word) == 5:
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

    >>> dept_name_to_zipcode('Martinique')
    '972'

    >>> dept_name_to_zipcode("cotes d'armr")

    >>> dept_name_to_zipcode("cotes d'armor")
    '22'

    >>> dept_name_to_zipcode(u'Hauts-de-Seine ')
    '92'

    >>> dept_name_to_zipcode(u'H\xe9rault')
    '34'

    >>> dept_name_to_zipcode(u'Seine-Saint-Denis ')
    '93'

    >>> dept_name_to_zipcode(u'Loire')
    '42'

    >>> dept_name_to_zipcode(u'Corse-du-Sud')
    '20A'

    >>> dept_name_to_zipcode(u'')

    >>> dept_name_to_zipcode(u'Yonne')
    '89'

    >>> dept_name_to_zipcode(u'Saint Pierre et Miquelon')
    '975'
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
    ur"""
    Get country name and return his code.
    >>> country_name_to_id('france')
    'FR'

    >>> country_name_to_id('Comores')
    'KM'

    >>> country_name_to_id('Madagascar')
    'MG'

    >>> country_name_to_id(u'S\xe9n\xe9gal')
    'SN'

    >>> country_name_to_id('République démocratique du Congo')
    'CD'

    >>> country_name_to_id('Mali')
    'ML'

    >>> country_name_to_id('Sri Lanka ')
    'LK'

    >>> country_name_to_id(u'\xa0V\xe9n\xe9zuela\xa0')
    'VE'

    >>> country_name_to_id('Mongolia', lang='EN')
    'MN'

    >>> country_name_to_id('Marocco', lang='EN')
    'MA'

    >>> country_name_to_id('Georgia', lang='EN')
    'GE'

    >>> country_name_to_id('Namibia', lang='EN')
    'NA'

    >>> country_name_to_id('Armenia', lang='EN')
    'AM'

    >>> country_name_to_id('sweden', lang='EN')
    'SE'

    >>> country_name_to_id(u'Vi\xeatnam')
    'VN'

    >>> country_name_to_id('Nigeria')
    'NG'

    >>> country_name_to_id(u'Niger')
    'NE'

    >>> country_name_to_id(u'aaa ( bbb')


    >>> country_name_to_id(u" Le  nigéria c'est trop   sympa")
    'NG'

    >>> country_name_to_id(u"Pays d'exécution : Niger")
    'NE'

    >>> country_name_to_id(u"Knotts Island, NC 27950\n\n27950-0039\nUnited States", lang='EN')
    'US'

    >>> country_name_to_id("  Côte d'Ivoire ")
    'CI'

    >>> country_name_to_id("721 APS BLDG 3334\nUNIT 3295 \nRamstein Air Base, Non-U.S. 66877 \nGermany ", lang='EN')
    'DE'

    >>> country_name_to_id("Saudi Arabia", lang='EN')
    'SA'

    >>> country_name_to_id("U.S. Mission Iraq\n\nIraq")
    'IQ'

    >>> country_name_to_id("Pays:France ?".encode('ascii', 'ignore'))
    'FR'

    >>> country_name_to_id("Country execution:nigeria.", lang='EN')
    'NG'

    >>> country_name_to_id(",royaume-uni,")
    'GB'

    >>> country_name_to_id("PAYS-BRÉSIL")
    'BR'

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
