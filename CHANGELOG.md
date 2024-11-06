# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [5.3.1] - 2024-11-06

### Added

- 'KNOWN_LANGUAGES_FOR_COUNTRY' variable containing languages geoconvert can process to find countries.

## [5.3.0] - 2024-11-04

### Changed

- "Island" no longer matches Iceland when language is not set.

### Fixed

- "Pacific Island" no longer matches Iceland.

## [5.2.2] - 2024-08-23

- Detection for "moldavie" as "MD" in French.

## [5.2.1] - 2024-05-02

- "Southern Africa" no longer matches South Africa.

## [5.2.0] - 2024-04-08

- Use French region names when finding French subdivisions
  (the dept of the regional prefecture is used if a region name matched)

## [5.1.0] - 2024-02-27

### Added

- Support for Python 3.12
- Detection for DE and FR subdivisions using NUTS codes
- escape ’ character as '

### Fixed

- Do not mistake "océan indien" as IN
- Support for Saint-Martin (France) postcodes

### Dependencies

- remove flake8
- use ruff

## [5.0.0] - 2023-03-13

### Added

- Support for Python 3.10 and 3.11
- Detection for "Irak" as IQ in French (not just "Iraq" for this language)

### Removed

- Support for Python 3.6 and 3.7

### Fixed

- All tests pass, no warning
- Detection for "Congo Democratic Republic" as CG (without "of" in the end)
- Do not mistake "Haute-Vienne" French department with the Austrian capital name "Vienne" (in French)
- Do not mistake "Prince Edward Island" (Canadian province) and "Rhode Island" (US state)
  with Iceland (which spells Island in German).

### Upgrade

- All libraries used for the dev/test environment

## [4.5.5] - 2022-12-20

### Fixed

- Do not mistake para with the Brazilian state Pará

## [4.5.4] - 2022-12-20

### Added

- Kyiv is a known capital name for French and English languages

## [4.5.3] - 2022-06-09

### Added

- Detection for "palestinian territory" as "PS" in English
- Detection for "turkiye" as "TR" in English + French
- Detection for "birmanie" as "MM" in French

## [4.5.2] - 2022-03-15

### Added

- Detection for "Bosnia & Herzegovina" as "BA" in English

### Fixed

- No longer find "IS" for countries with "island" in their names.

## [4.5.1] - 2022-03-11

### Added
- Detection of german departments with postcodes


## [4.5.0] - 2021-10-11

### Changed
- test organisation : single file split into multiple files in folders
- US Minor Outlying Islands (UM) is considered as a country and not a US state
- Saint Barthélémy (FR-977) is considered a French departement on its own and not Guadeloupe

### Added
- Changelog !
- Detection for AG written "Antigue et Barbude" in French
- Detection of any Brazilian state code from the post code, state name or if the state code is present.
- Detection of any German land code from the state name, state capital or if the state code is present.
- `address_to_country_and_subdivision_codes` can return iso format


## [4.4.1] - 2021-09-23

### Changed
- minor refacto in special_countries and tests

## [4.4.0] - 2021-09-22

### Fixed
- Make sure we never mistake Guinea (GN) and Papua New Guinea (PG)

## [4.3.0] - 2021-08-09

### Fixed
- Make sure we never mistake Jersey (JE) and New Jersey (US-NJ)


## [4.2.0] - 2021-07-20

### Fixed
- Make sure we never mistake Sudan (SD) and South Sudan (SS)


## [4.1.0] - 2021-01-17

### Added
- Detection of country names in Spanish

## [4.0.0] - 2021-01-11

### Added
- Detection of any American state code from the post code, state name or if the state code is present.
- Detection of any Canadian province or territory code from the post code, state name or if the state code is present.
- Wrapper functions to allow finding the subdivision code (department for France, state for US, ...) and/or the country code from a text input.
- Update README (show the new functions usage in an extensive fashion - more details on how to run the tests and prepare your local dev env - more details for the dev when adding a new language or subdivisions to a new country)

### Changed
- Refactorization of the current code (mainly for France departments and regions) to make the functions more uniform.
- Move data from a single file to multiple files in a specific folder.
- Update CI (test the README, style check)

### Fixed
- Make base functions as language or country-agnostic as possible

### Removed
- Anything related to python 2
