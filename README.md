Geoconvert converts (obvious) data like zipcode, postcode, address, country name,
French department name, Americain state name, Canadian province or territory name
to generic data.

* Languages available for country names: deutsch, english, french, portuguese, spanish.
* Languages available for capital names: deutsch, english, french.

Support Python 3.6, 3.7, 3.8 and 3.9.

[![Build Status](https://travis-ci.org/jurismarches/geoconvert.svg?branch=master)](https://travis-ci.org/jurismarches/geoconvert)
[![codecov](https://codecov.io/gh/jurismarches/geoconvert/branch/master/graph/badge.svg?token=UB3Vij6ygJ)](https://codecov.io/gh/jurismarches/geoconvert)

# Installation

Install the latest version from Github:
```bash
pip install https://github.com/jurismarches/geoconvert/archive/master.zip
```

# TL;DR

```python
>>> from geoconvert.convert import (
... 	address_to_country_code,
... 	address_to_subdivision_code,
... 	address_to_country_and_subdivision_codes,
... )
>>> address_to_country_code("Bienvenue à Londres")  # FR
'GB'
>>> address_to_country_code("Bienvenue à Londres", lang="fr")
'GB'
>>> address_to_country_code("Bienvenue à Londres", lang="en")
>>> address_to_country_code("Welcome to Cyprus")  # EN
'CY'
>>> address_to_country_code("Welcome to Los Angeles, California")
'US'
>>> address_to_country_code("Welcome to Los Angeles, CA")
>>> address_to_country_code("Willkommen bei Kairo")  # DE
'EG'
>>> address_to_country_code("Bem vindo ao Afeganistão")  # PT
'AF'
>>> address_to_country_code("Bienvenidos a Nueva Zelanda")  # ES
'NZ'
>>> address_to_country_code("659 Ocean Ave, Lakewood, New Jersey 08701")
'US'
>>> address_to_country_code("Le Chemin des Garennes, Jersey JE3 2FE, Jersey")
'JE'
>>> address_to_subdivision_code("2 pl. Saint-Pierre, 44000 Nantes, France")  # FR
'44'
>>> address_to_subdivision_code("2 pl. Saint-Pierre, 44000 Nantes", country="FR")
'44'
>>> address_to_subdivision_code("2 pl. Saint-Pierre, 44000 Nantes", country="US")
>>> address_to_subdivision_code("1800 W Erie Ave, Lorain, OH 44052")  # US
'OH'
>>> address_to_subdivision_code("1800 W Erie Ave, Lorain, OH 44052", country="FR")
>>> address_to_subdivision_code("196 Voie Camillien-Houde, Montréal, QC H3H 1A1")  # CA
'QC'
>>> address_to_country_and_subdivision_codes("1170 Cattus Island Blvd, Toms River, New Jersey")  # US
('US', 'NJ')
>>> address_to_country_and_subdivision_codes("Montréal, Québec")  # CA
('CA', 'QC')
>>> address_to_country_and_subdivision_codes("1800 W Erie Ave, Lorain, OH 44052")  # US
('US', 'OH')
>>> address_to_country_and_subdivision_codes("Kairo", lang="de")
('EG', None)
>>> address_to_country_and_subdivision_codes("Kairo", lang="de", country="EG")
('EG', None)
>>> address_to_country_and_subdivision_codes("Kairo", lang="de", country="US")
(None, None)

```


# Usage examples

Geoconvert mainly provides mainly two types of functions:
- one converts an input containing a country or capital name to a two-letter country code
  (ISO 3166-1 alpha 2) using a set of available languages.
- the other converts an address of a given country to a subdivision code
  (department code for France, province or territory code for Canada,
  state code for the United States of America).

Some usage examples are shown below. For more examples, take a look at the unit tests.

## Finding country codes

The main function you are looking for is the following, converting a country or
a capital name to a country code. By default, it uses all the available languages to
guess the country code:
```python
>>> from geoconvert.convert import address_to_country_code
>>> address_to_country_code("Bienvenue à Kinshasa")  # FR
'CD'
>>> address_to_country_code("Welcome to Cyprus")  # EN
'CY'
>>> address_to_country_code("Willkommen bei Kairo")  # DE
'EG'
>>> address_to_country_code("Bem vindo ao Afeganistão")  # PT
'AF'
>>> address_to_country_code("Bienvenidos a Nueva Zelanda")  # ES
'NZ'

```

If you known the language of your input data, you may select that language
for more efficiency (available choices: "de" for german, "en" for english,
"fr" for french, "pt" for portuguese):
```python
>>> address_to_country_code("Bienvenue à Kinshasa", lang="fr")
'CD'
>>> address_to_country_code("Welcome to Cyprus", lang="en")
'CY'
>>> address_to_country_code("Willkommen bei Kairo", lang="de")
'EG'
>>> address_to_country_code("Bem vindo ao Afeganistão", lang="pt")
'AF'
>>> address_to_country_code("Bienvenidos a Nueva Zelanda", lang="es")
'NZ'

```

There are more specific functions, for which you can also select a language
(all of them are used by default):
```python
>>> from geoconvert.convert import (
... 	country_name_to_country_code, capital_name_to_country_code
... )
>>> country_name_to_country_code(" Le  nigéria c'est trop   sympa", lang="fr")
'NG'
>>> capital_name_to_country_code('Kairo', lang="de")
'EG'

```

## Finding subdivision codes

Geoconvert also gives you the abilty to find the code associated to a smaller
part of a given country, namely:
- the province or territory code for Canada,
- the department code for France,
- the department codes of a French region,
- the state code for the United States of America.

The main function you are looking for is `address_to_subdivision_code`.
It converts an address to a subdivision code.
By default, it uses all the available subdivisions to guess the subdivision code:
```python
>>> address_to_subdivision_code("2 pl. Saint-Pierre, 44000 Nantes, France")  # FR
'44'
>>> address_to_subdivision_code("1800 W Erie Ave, Lorain, OH 44052")  # US
'OH'
>>> address_to_subdivision_code("196 Voie Camillien-Houde, Montréal, QC H3H 1A1")  # CA
'QC'

```

There should be no confusion between French and US postcodes:
```python
>>> address_to_subdivision_code("2 pl. Saint-Pierre, 44000 Nantes", country="US")
>>> address_to_subdivision_code("1800 W Erie Ave, Lorain, OH 44052", country="FR")

```

### Brazil

You can find the state code associated with an address, via the postcode,
state name (in Portuguese) or code:
```python
>>> from geoconvert.convert import br_address_to_state_code
>>> br_address_to_state_code("Luz, 01120-010")
'SP'
>>> br_address_to_state_code("Piauí")
'PI'
>>> br_address_to_state_code("Dourados, MS")
'MS'

```

You may use more specific functions, depending on your needs:
```python
>>> from geoconvert.convert import (
... 	br_postcode_to_state_code, br_state_name_to_state_code
... )
>>> br_postcode_to_state_code("Mariana, 04094-050")
'SP'
>>> br_state_name_to_state_code("a capital do estado do maranhao.")
'MA'

```


### Canada

You can find the province or territory code associated with an address, via the postcode,
province or territory name (in French or English) or code:
```python
>>> from geoconvert.convert import ca_address_to_province_code
>>> ca_address_to_province_code("H3T 1X6")
'QC'
>>> ca_address_to_province_code("Toronto, Ontario")
'ON'
>>> ca_address_to_province_code("Toronto, ON")
'ON'
>>> ca_address_to_province_code("Québec")
'QC'
>>> ca_address_to_province_code("Terre-Neuve-et-Labrador")
'NL'
>>> ca_address_to_province_code("Newfoundland and Labrador")
'NL'
>>> ca_address_to_province_code("Bldg 158, Iqaluit, NU X0A 0H0, Canada")
'NU'
>>> ca_address_to_province_code("52-58 Franklin Rd, Inuvik, NT X0E 0T0, Canada")
'NT'

```

You may use more specific functions, depending on your needs:
```python
>>> from geoconvert.convert import (
... 	ca_postcode_to_province_code, ca_province_name_to_province_code
... )
>>> ca_postcode_to_province_code("Iqaluit X0A 0H0")
'NU'
>>> ca_postcode_to_province_code("Inuvik X0E 0T0")
'NT'
>>> ca_province_name_to_province_code("Welcome to Ontario")
'ON'

```

### France

You can find the department code associated with an address or department name:
```python
>>> from geoconvert.convert import fr_address_to_dept_code
>>> fr_address_to_dept_code("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX")
'33'
>>> fr_address_to_dept_code("Loire-Atlantique")
'44'
>>> fr_address_to_dept_code("LOIRE    -    ATLANTIQUE")
'44'
>>> fr_address_to_dept_code("Loire    -    ")
'42'

```

You can also derive the main department and the list of all departments
which are part of a given region from its name:
```python
>>> from geoconvert.convert import fr_region_name_to_info
>>> # Returns the deparment code where the head of the region is
>>> # and the list of all the departments in the region.
>>> fr_region_name_to_info('Les Pays de la Loire, une superbe région')
('44', ['44', '49', '53', '72', '85'])

```

You may use more specific functions, depending on your needs:
```python
>>> from geoconvert.convert import (
... 	fr_address_to_dept_code,
... 	fr_dept_name_to_dept_code,
... 	fr_postcode_to_dept_code,
... )
>>> fr_postcode_to_dept_code("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX")
'33'
>>> fr_dept_name_to_dept_code("Loire    -    Atlantique")
'44'
>>> fr_dept_name_to_dept_code("Loire    -    ")
'42'

```

### United States of America

You can find the state code associated with an address, via the postcode,
state name (in English) or code:
```python
>>> from geoconvert.convert import us_address_to_state_code
>>> us_address_to_state_code("Sunnyvale, CA 94085")
'CA'
>>> us_address_to_state_code("New Hampshire")
'NH'
>>> us_address_to_state_code("Los Angeles, CA")
'CA'

```

You may use more specific functions, depending on your needs:
```python
>>> from geoconvert.convert import (
... 	us_postcode_to_state_code, us_state_name_to_state_code
... )
>>> us_postcode_to_state_code("6931 Rings Rd, Amlin, OH 43002")
'OH'
>>> us_state_name_to_state_code("Welcome to West Virginia")
'WV'

```


## Mixing both country codes and subdivision codes

You can derive both country and subdivision codes at the same time:
```python
>>> from geoconvert.convert import address_to_country_and_subdivision_codes
>>> address_to_country_and_subdivision_codes("Montréal, QC, Canada")
('CA', 'QC')
>>> address_to_country_and_subdivision_codes("Montréal, Québec")
('CA', 'QC')
>>> address_to_country_and_subdivision_codes("Montréal, QC")
(None, None)
>>> address_to_country_and_subdivision_codes("Montréal, QC", country="CA")
('CA', 'QC')
>>> address_to_country_and_subdivision_codes("Montréal", country="CA")
(None, None)
>>> address_to_country_and_subdivision_codes("Montréal, QC", country="US")
(None, None)
>>> address_to_country_and_subdivision_codes("Kairo", lang="de")
('EG', None)
>>> address_to_country_and_subdivision_codes("Kairo", lang="de", country="EG")
('EG', None)
>>> address_to_country_and_subdivision_codes("Kairo", lang="de", country="US")
(None, None)

```

Result format can be choosen between a tuple and an iso code
```python
>>> address_to_country_and_subdivision_codes("14467 Potsdam")
('DE', 'BB')
>>> address_to_country_and_subdivision_codes("14467 Potsdam", iso_format=True)
'DE-BB'
>>> address_to_country_and_subdivision_codes("14467 Germany")
('DE', None)
>>> address_to_country_and_subdivision_codes("14467 Germany", iso_format=True)
'DE'

```

There should be no confusion between French and US postcodes:
```python
>>> address_to_country_and_subdivision_codes("2 pl. Saint-Pierre, 44000 Nantes", country="US")
(None, None)
>>> address_to_country_and_subdivision_codes("6931 Rings Rd, Amlin, OH 43002", country="FR")
(None, None)

```

# For developers

## Tests

Just run pytest:
```bash
make test
```

Do not forget to install the dependencies first, preferably in a vitrual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements_test.txt
```

## Releases

To release a new version you must update `__version__` on `geoconvert/__init__.py`
and tag the master branch with the same version.

## Adding a new language for countries and/or capitals

* Add the data in dictionaries, where the key is the name, and the value is the
  corresponding country code.
* These dictionaries must be named `countries_<language_code>` in `geoconvert/data/countries.py`
  and/or `capitals_<language_code>` in `geoconvert/data/capitals.py`.
  The language code is a two-letter, lowercase code.
  For instance, for italian, the language code is "it".
* Use already existing data as a template, especially to handle `special_countries`.
* Add the corresponding dictionnary to `language_to_country_names` and/or `language_to_capital_names`.
  This allows the `address_to_country_code`, `country_name_to_country_code`,
  and `capital_name_to_country_code` functions to use this language.
* Add the language to the list of available languages at the top of this README.
* Add examples which are specific for this language in the README, doctests and tests,
  especially for `address_to_country_code` and `address_to_country_and_subdivision_codes`.

## Adding subdivisions to a new country

* Add the data in dictionaries in `geoconvert/data/subdivisions/<country_name>.py`,
  where `<country_name>` is the lowercase country name in English
  (for instance, `geoconvert/data/subdivisions/germany.py` for Germany).
* Add functions that allow you convert an address to a subdivision code :
  * a base function `<country_code>_address_to_<subdivision_name>_code` that uses the
    other implemented functions converting an address to a subdivision code
    (e.g., `ca_address_to_province_code`)
  * a function converting the full subdivision name to the subdivision code
    (e.g., `ca_province_name_to_province_code`)
  * a function converting a postcode from that country to a subdivision
    (e.g., `ca_postcode_to_province_code`).
    This is optionnal, but highly recommended.
  * optionnally, a regex finding the subdivision code directly from the text can be used
    as the last option in `<country_code>_address_to_<subdivision_name>_code`.
* Add the base function to the `country_to_subdivision_lookup_function`
  dictionary under the corresponding uppercase country code key.
  This allows this function to be used by the `address_to_subdivision_code` and
  `address_to_country_and_subdivision_codes` functions.
* Add the newly available subdivisions to the list at the top of this README.
* Add examples which are specific for this country in the README, doctests and tests,
  especially the `address_to_subdivision_code` and
  `address_to_country_and_subdivision_codes` functions.
  Each added function must be tested as well.
