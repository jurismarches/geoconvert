# -*- coding: utf8 -*-
import re
import unicodedata


def remove_accents(text):
    """
    Remove accents from a string
    """
    try:
        text = text.decode("utf-8")
    except (UnicodeEncodeError, AttributeError):
        pass
    text = text.replace("’", "'")  # accent used as apostrophe
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
    text = text.decode()
    return text


def safe_string(text):
    """
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
    >>> safe_string('How aRE yOU?')
    'how are you'
    >>> safe_string("l’ocean")
    "l'ocean"
    """
    text = remove_accents(text)
    # Replace "-" and ":" with a whitespace
    text = re.sub(r"[-:]", " ", text)
    # Replace weird '
    text = re.sub(r"[ʼ]", "'", text)
    # Only keep word or space characters as well as "_", and "'".
    text = re.sub(r"[^\w\s']", "", text)
    # Always remove multiple whitespaces at the very last minute
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()
