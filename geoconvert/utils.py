# -*- coding: utf8 -*-
import re
import unicodedata


def remove_accents(text):
    """
    Remove accents from a string
    """
    return unicodedata.normalize('NFKD', unicode(text)).encode('ascii', 'ignore')

def safe_string(text):
    u"""
    Safe a string
    >>> safe_string('Alsace')
    'alsace'
    >>> safe_string(' AlSace')
    'alsace'
    >>> safe_string(u'île-de France ')
    'ile de france'
    >>> safe_string(u"Provence alpes côte D'azur")
    "provence alpes cote d'azur"
    >>> safe_string('ile- de  france')
    'ile de france'
    """
    text = remove_accents(text)
    text = text.replace('-', ' ')
    text = re.sub(r'\s+', ' ', text.strip())
    text = text.lower().encode('ASCII', 'replace').replace('?', '.')
    return text

def reverse_dict(dict_to_reverse):
    """
    Reverse a dict
    >>> reverse_dict({'key': 'value'})
    {'value': 'key'}
    >>> reverse_dict({'key1': 'value1', 'key2': 'value2'})
    {'value2': 'key2', 'value1': 'key1'}
    """
    reversed_dict = {}
    for key, value in dict_to_reverse.items():
        reversed_dict[value] = key
    return reversed_dict


if __name__ == "__main__":
    import doctest
    doctest.testmod()
