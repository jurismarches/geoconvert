# -*- coding: utf8 -*-
import re
import unicodedata

python3 = False
if re.search(r"^(\d)", sys.version).group(1) == "3":
    python3 = True


def remove_accents(text):
    """
    Remove accents from a string
    """
    try:
        text = text.decode("utf-8")
    except UnicodeEncodeError:
        pass
    except AttributeError:
        pass
    try:
        text = unicode(text)
    except NameError:
        # unicode module doesn't exist on Python 3.X
        pass
    text = text.replace(u"’", u"'")  # accent used as apostrophe
    text_normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
    if sys.version_info >= (3,):
        text_normalized = text_normalized.decode()
    return text_normalized


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
    >>> safe_string('sao tome & principe')
    'sao tome principe'
    >>> safe_string('new_hampshire')
    'new_hampshire'
    >>> safe_string('washington, d.c.')
    'washington dc'
    """
    try:
        text = text.decode("utf-8")
    except (UnicodeEncodeError, AttributeError):
        pass
    text = remove_accents(text)
    for char in ("-", ":"):
        text = text.replace(char, " ")
    if python3:
        text = text.lower().replace("?", ".")
    else:
        text = text.lower().encode("ASCII", "replace").replace("?", ".")
    # Only keep word or space characters as well as "_", and "'".
    text = re.sub(r"[^\w\s']", "", text)
    # Always remove multiple whitespace at the very last minute
    text = re.sub(r"\s+", " ", text.strip())
    return text


def reverse_dict(dict_to_reverse):
    reversed_dict = {}
    for key, value in dict_to_reverse.items():
        reversed_dict[value] = key
    return reversed_dict
