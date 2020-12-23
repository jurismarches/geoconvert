from .capitals import capitals_de, capitals_en, capitals_fr, language_to_capital_names
from .countries import (
    countries_de,
    countries_en,
    countries_fr,
    countries_pt,
    country_territories,
    language_to_country_names,
    territory_to_country,
)
from .subdivisions.canada import (
    CA_POSTCODE_FIRST_LETTER_TO_PROVINCE_CODE,
    ca_postcode_regex,
    ca_province_code_regex,
    ca_province_name_regex,
    ca_provinces,
)
from .subdivisions.france import (
    fr_department_name_regex,
    fr_departments,
    fr_postcode_regex,
    fr_principal_places,
    fr_region_name_regex,
    fr_regions,
)
from .subdivisions.united_states import (
    US_POSTCODE_PREFIX_TO_STATE_CODE,
    us_postcode_regex,
    us_state_code_regex,
    us_state_name_regex,
    us_states,
)
