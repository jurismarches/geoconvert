from .capitals import capitals_de, capitals_en, capitals_fr, language_to_capital_names
from .countries import (
    ambiguous_countries,
    countries_de,
    countries_en,
    countries_fr,
    countries_pt,
    country_territories,
    language_to_country_names,
    territory_to_country,
)
from .subdivisions.brazil import (
    BR_POSTCODES_RANGE,
    br_postcode_regex,
    br_state_code_regex,
    br_state_name_regex,
    br_states,
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
from .subdivisions.germany import (
    DE_HAUPTSTADT,
    DE_POSTCODE_RANGE,
    de_land_code_regex,
    de_land_hauptstadt_regex,
    de_land_name_regex,
    de_landers,
    de_postcode_regex,
)
from .subdivisions.nuts import (
    ALL_NUTS_CODES,
    NUTS_CODES_BY_COUNTRY,
    all_nuts_regex,
    nuts_regexes_by_country,
)
from .subdivisions.united_states import (
    us_postcode_regex,
    us_state_code_regex,
    us_state_name_regex,
    us_states,
)
