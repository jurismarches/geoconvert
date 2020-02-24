Geoconvert convert (obvious) data like zipcode, address, department name to generic data.

Support Python 2.7, 3.6, 3.7 and 3.8.

[![Build Status](https://travis-ci.org/jurismarches/geoconvert.svg?branch=master)](https://travis-ci.org/jurismarches/geoconvert)

Installation
============

Install the latest version from Github:
```
$ pip install https://github.com/jurismarches/geoconvert/archive/master.zip
```

Examples
========

```python
    from geoconvert.convert import zipcode_to_dept_name
    zipcode_to_dept_name('44300')
    'loire-altantique'

    from geoconvert.convert import address_to_zipcode
    address_to_zipcode('Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX')
    '33'

    from geoconvert.convert import region_name_to_id
    region_name_to_id('La guadeloupe, une superbe région')
    '01

    from geoconvert.convert import test_dept_name_to_zipcode
    test_dept_name_to_zipcode('Martinique')
    '972'

    from geoconvert.convert import country_name_to_id
    country_name_to_id(" Le  nigéria c'est trop   sympa")
    'NG

    from geoconvert.convert import capital_name_to_country_id
    capital_name_to_country_id('Paris')
    'FR'
```


For more examples, take a look at unit tests.

Usage
=====

```python
    from geoconvert.convert import zipcode_to_dept_name
    from geoconvert.convert import address_to_zipcode
    from geoconvert.convert import dept_name_to_zipcode
    from geoconvert.convert import region_id_to_name
    from geoconvert.convert import region_name_to_id
    from geoconvert.convert import country_name_to_id
```

Tests
=====

```python
    python -m unittest test_geoconvert.py
```

Releases
========

To release a new version you must update `__version__` on `geoconvert/__init__.py`
and tag the master branch with the same version.
