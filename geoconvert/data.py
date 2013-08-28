# -*- coding: utf8 -*-

regions = {
    "42": "alsace",
    "72": "aquitaine",
    "83": "auvergne",
    "26": "bourgogne",
    "53": "bretagne",
    "24": "centre",
    "21": "champagne ardenne",
    "94": "corse",
    "43": "franche comte",
    "01": "guadeloupe",
    "03": "guyane",
    "11": "ile de france",
    "91": "languedoc roussillon",
    "74": "limousin",
    "41": "lorraine",
    "02": "martinique",
    "06": "mayotte",
    "73": "midi pyrenees",
    "31": "nord pas de calais",
    "25": "basse normandie",
    "23": "haute normandie",
    "52": "pays de la loire",
    "22": "picardie",
    "54": "poitou charentes",
    "93": "provence alpes cote d'azur",
    "04": "reunion",
    "82": "rhone alpes"
}

# Region ID => Dept chef lieu id, (List of region"s dept)
principal_places = {
    "42": ("67", ["67", "68"]),
    "72": ("33", ["24", "33", "40", "47", "64"]),
    "83": ("63", ["03", "15", "43", "63"]),
    "26": ("21", ["21", "58", "71", "89"]),
    "53": ("35", ["22", "29", "35", "56"]),
    "24": ("45", ["18", "28", "36", "37", "41", "45"]),
    "21": ("51", ["08", "10", "51", "52"]),
    "94": ("20A", ["20A", "20B"]),
    "43": ("25", ["25", "39", "70", "90"]),
    "01": ("971", ["971"]),
    "03": ("973", ["973"]),
    "11": ("75", ["75", "77", "78", "91", "92", "93", "94", "95"]),
    "91": ("34", ["11", "30", "34", "48", "66"]),
    "74": ("87", ["19", "23", "87"]),
    "41": ("57", ["54", "55", "57", "88"]),
    "02": ("972", ["972"]),
    "06": ("976", ["976"]),
    "73": ("31", ["09", "12", "31", "32", "46", "65", "81", "82"]),
    "31": ("59", ["59", "62"]),
    "25": ("14", ["14", "50", "61"]),
    "23": ("76", ["27", "76"]),
    "52": ("44", ["44", "49", "53", "72", "85"]),
    "22": ("80", ["02", "60", "80"]),
    "54": ("86", ["16", "17", "79", "86"]),
    "93": ("13", ["04", "05", "06", "13", "83", "84"]),
    "04": ("974", ["974"]),
    "82": ("69", ["01", "07", "26", "38", "42", "69", "73", "74"])
}

departments = {
"01": "ain",
"02": "aisne",
"03": "allier",
"04": "alpes-de-hautes-provence",
"04": "alpes-de-haute-provence",
"05": "hautes-alpes",
"06": "alpes-maritimes",
"07": "ardeche",
"08": "ardennes",
"09": "ariege",
"10": "aube",
"11": "aude",
"12": "aveyron",
"13": "bouches-du-rhone",
"14": "calvados",
"15": "cantal",
"16": "charente",
"17": "charente-maritime",
"18": "cher",
"19": "correze",
"20A": "corse-du-sud",
"20B": "haute-corse",
"21": "cote-d'or",
"22": "cotes-d'armor",
"23": "creuse",
"24": "dordogne",
"25": "doubs",
"26": "drome",
"27": "eure",
"28": "eure-et-loir",
"29": "finistere",
"30": "gard",
"31": "haute-garonne",
"32": "gers",
"33": "gironde",
"34": "herault",
"35": "ille-et-vilaine",
"36": "indre",
"37": "indre-et-loire",
"38": "isere",
"39": "jura",
"40": "landes",
"41": "loir-et-cher",
"42": "loire",
"43": "haute-loire",
"44": "loire-atlantique",
"45": "loiret",
"46": "lot",
"47": "lot-et-garonne",
"48": "lozere",
"49": "maine-et-loire",
"50": "manche",
"51": "marne",
"52": "haute-marne",
"53": "mayenne",
"54": "meurthe-et-moselle",
"55": "meuse",
"56": "morbihan",
"57": "moselle",
"58": "nievre",
"59": "nord",
"60": "oise",
"61": "orne",
"62": "pas-de-calais",
"63": "puy-de-dome",
"64": "pyrenees-atlantique",
"64": "pyrenees-atlantiques",
"65": "hautes-pyrenees",
"66": "pyrenees-orientales",
"67": "bas-rhin",
"68": "haut-rhin",
"69": "rhone",
"70": "haute-saone",
"71": "saone-et-loire",
"72": "sarthe",
"73": "savoie",
"74": "haute-savoie",
"75": "paris",
"76": "seine-maritime",
"77": "seine-et-marne",
"78": "yvelines",
"79": "deux-sevres",
"80": "somme",
"81": "tarn",
"82": "tarn-et-garonne",
"83": "var",
"84": "vaucluse",
"85": "vendee",
"86": "vienne",
"87": "haute-vienne",
"88": "vosges",
"89": "yonne",
"90": "territoire-de-belfort",
"91": "essonne",
"92": "hauts-de-seine",
"93": "seine-saint-denis",
"94": "val-de-marne",
"95": "val-d'oise",
"971": "guadeloupe",
"972": "martinique",
"973": "guyane",
"974": "la-reunion",
"974": "ile-de-la-reunion",
"975": "saint-pierre-et-miquelon",
"976": "mayotte",
"984": "terres-australes-et-antarctiques",
"986": "wallis-et-futuna",
"987": "polynesie-francaise",
"988": "nouvelle-caledonie"
}

countries_fr = {
	"emirats arabes unis": "AE",
	"afghanistan": "AF",
	"antigua et barbuda": "AG",
	"anguilla": "AI",
	"albanie": "AL",
	"armenie": "AM",
	"antilles neerlandaises": "AN",
	"angola": "AO",
	"antarctique": "AQ",
	"argentine": "AR",
	"samoa americaines": "AS",
	"autriche": "AT",
	"australie": "AU",
	"aruba": "AW",
	"aland": "AX",
	"azerbaidjan": "AZ",
	"bosnie-herzegovine": "BA",
	"barbade": "BB",
	"bangladesh": "BD",
	"belgique": "BE",
	"burkina faso": "BF",
	"bulgarie": "BG",
	"bahrein": "BH",
	"burundi": "BI",
	"benin": "BJ",
	"bermudes": "BM",
	"brunei darussalam": "BN",
	"bolivie": "BO",
	"bresil": "BR",
	"bahamas": "BS",
	"bhoutan": "BT",
	"bouvet": "BV",
	"botswana": "BW",
	"belarus": "BY",
	"belize": "BZ",
	"canada": "CA",
	"r.+publique d.+mocratique du congo": "CD",
	"cocos (keeling)": "CC",
	"centrafricaine": "CF",
	"congo": "CG",
	"suisse": "CH",
	"cote d'ivoire": "CI",
	"cook": "CK",
	"chili": "CL",
	"cameroun": "CM",
	"chine": "CN",
	"colombie": "CO",
	"costa rica": "CR",
	"cuba": "CU",
	"cap-vert": "CV",
	"cap vert": "CV",
	"christmas": "CX",
	"chypre": "CY",
	"tcheque": "CZ",
	"allemagne": "DE",
	"djibouti": "DJ",
	"danemark": "DK",
	"dominique": "DM",
	"dominicaine": "DO",
	"algerie": "dZ",
	"equateur": "EC",
	"estonie": "EE",
	"egypte": "EG",
	"sahara occidental": "EH",
	"erythree": "ER",
	"espagne": "ES",
	"ethiopie": "ET",
	"finlande": "FI",
	"fidji": "FJ",
	"falkland": "FK",
	"micronesie": "FM",
	"feroe": "FO",
	"france": "FR",
	"gabon": "GA",
	"royaume-uni": "GB",
	"grenade": "GD",
	"georgie": "GE",
	"guyane francaise": "GF",
	"guernesey": "GG",
	"ghana": "GH",
	"gibraltar": "GI",
	"groenland": "GL",
	"gambie": "GM",
	"guinee": "GN",
	"guadeloupe": "GP",
	"guinee equatoriale": "GQ",
	"grece": "GR",
	"georgie du sud et les iles sandwich du sud": "GS",
	"guatemala": "GT",
	"guam": "GU",
	"guinee-bissau": "GW",
	"guinee bissau": "GW",
	"guyana": "GY",
	"hong-kong": "HK",
	"heard": "HM",
	"honduras": "HN",
	"croatie": "HR",
	"haiti": "HT",
	"hongrie": "HU",
	"indonesie": "ID",
	"irlande": "IE",
	"israël": "IL",
	"ile de man": "IM",
	"inde": "IN",
	"ocean indien": "IO",
	"iraq": "IQ",
	"iran": "IR",
	"islande": "IS",
	"italie": "IT",
	"jersey": "JE",
	"jamaique": "JM",
	"jordanie": "JO",
	"japon": "JP",
	"kenya": "KE",
	"kirghizistan": "KG",
	"cambodge": "kH",
	"kiribati": "KI",
	"comores": "kM",
	"saint-kitts-et-nevis": "KN",
	"kosovo": "KO",
	"coree": "KP",
	"coree": "KR",
	"koweit": "KW",
	"caimanes": "KY",
	"kazakhstan": "KZ",
	"lao": "LA",
	"liban": "LB",
	"sainte-lucie": "LC",
	"liechtenstein": "LI",
	"sri lanka": "LK",
	"liberia": "LR",
	"lesotho": "LS",
	"lituanie": "LT",
	"luxembourg": "LU",
	"lettonie": "LV",
	"libyenne": "LY",
	"maroc": "MA",
	"monaco": "MC",
	"moldova": "MD",
	"montenegro": "ME",
	"saint-martin": "MF",
	"madagascar": "MG",
	"marshall": "MH",
	"macedoine": "MK",
	"mali": "ML",
	"myanmar": "MM",
	"mongolie": "MN",
	"mongolia": "MN",
	"macao": "MO",
	"mariannes du nord": "MP",
	"martinique": "MQ",
	"mauritanie": "MR",
	"montserrat": "MS",
	"malte": "MT",
	"maurice": "MU",
	"maldives": "MV",
	"malawi": "MW",
	"mexique": "MX",
	"malaisie": "MY",
	"mozambique": "MZ",
	"namibie": "NA",
	"nouvelle-caledonie": "NC",
	"niger": "NE",
	"norfolk": "NF",
	"nigeria": "NG",
	"nicaragua": "NI",
	"pays-bas": "NL",
	"norvege": "NO",
	"nepal": "NP",
	"nauru": "NR",
	"niue": "NU",
	"nouvelle-zelande": "NZ",
	"oman": "OM",
	"panama": "PA",
	"perou": "PE",
	"polynesie francaise": "PF",
	"papouasie-nouvelle-guinee": "PG",
	"philippines": "PH",
	"pakistan": "PK",
	"pologne": "PL",
	"saint-pierre-et-miquelon": "PM",
	"pitcairn": "PN",
	"porto rico": "PR",
	"palestinien occupe": "PS",
	"portugal": "PT",
	"palaos": "PW",
	"paraguay": "PY",
	"qatar": "QA",
	"reunion": "RE",
	"roumanie": "RO",
	"serbie": "RS",
	"russie": "RU",
	"rwanda": "RW",
	"arabie saoudite": "SA",
	"salomon": "SB",
	"seychelles": "SC",
	"soudan": "SD",
	"suede": "SE",
	"singapour": "SG",
	"sainte-helene": "SH",
	"slovenie": "SI",
	"svalbard et ile jan mayen": "SJ",
	"slovaquie": "SK",
	"sierra leone": "SL",
	"saint-marin": "SM",
	"senegal": "SN",
	"somalie": "SO",
	"suriname": "SR",
	"sao tome-et-principe": "ST",
	"sao tome et principe": "ST",
	"el salvador": "SV",
	"syrienne": "SY",
	"swaziland": "SZ",
	"turks et caiques": "TC",
	"tchad": "TD",
	"terres australes francaises": "TF",
	"togo": "TG",
	"thailande": "TH",
	"tadjikistan": "TJ",
	"tokelau": "TK",
	"timor-leste": "TL",
	"turkmenistan": "TM",
	"tunisie": "TN",
	"tonga": "TO",
	"turquie": "TR",
	"trinite-et-Tobago": "TT",
	"tuvalu": "TV",
	"taiwan": "TW",
	"tanzanie": "TZ",
	"tanzania": "TZ",
	"ukraine": "UA",
	"ouganda": "UG",
	"iles mineures eloignees des etats-unis": "UM",
	"etats-unis": "US",
	"uruguay": "UY",
	"ouzbekistan": "UZ",
	"vatican": "VA",
	"saint-vincent-et-les grenadines": "VC",
	"venezuela": "VE",
	"iles vierges britanniques": "VG",
	"iles vierges des etats-unis": "VI",
	"viet nam": "VN",
	"vietnam": "VN",
	"vanuatu": "VU",
	"wallis et futuna": "WF",
	"samoa": "WS",
	"yemen": "YE",
	"mayotte": "YT",
	"afrique du sud": "ZA",
	"zambie": "ZM",
	"zimbabwe": "ZW"
}

countries_en = {
    "afghanistan": "AF",
    "åland islands": "AX",
    "albania": "AL",
    "algeria": "DZ",
    "american samoa": "AS",
    "andorra": "AD",
    "angola": "AO",
    "anguilla": "AI",
    "antarctica": "AQ",
    "antigua and barbuda": "AG",
    "argentina": "AR",
    "armenia": "AM",
    "aruba": "AW",
    "australia": "AU",
    "austria": "AT",
    "azerbaijan": "AZ",
    "bahamas": "BS",
    "bahrain": "BH",
    "bangladesh": "BD",
    "barbados": "BB",
    "belarus": "BY",
    "belgium": "BE",
    "belize": "BZ",
    "benin": "BJ",
    "bermuda": "BM",
    "bhutan": "BT",
    "bolivia, plurinational state of": "BO",
    "bonaire, saint eustatius and saba": "BQ",
    "bosnia and herzegovina": "BA",
    "botswana": "BW",
    "bouvet island": "BV",
    "brazil": "BR",
    "british indian ocean territory": "IO",
    "brunei darussalam": "BN",
    "bulgaria": "BG",
    "burkina faso": "BF",
    "burundi": "BI",
    "cambodia": "KH",
    "cameroon": "CM",
    "canada": "CA",
    "cape verde": "CV",
    "cayman islands": "KY",
    "central african republic": "CF",
    "chad": "TD",
    "chile": "CL",
    "china": "CN",
    "christmas island": "CX",
    "cocos (keeling) islands": "CC",
    "colombia": "CO",
    "comoros": "KM",
    "congo": "CG",
    "congo, the democratic republic of the": "CD",
    "cook islands": "CK",
    "costa rica": "CR",
    "cote d'ivoire": "CI",
    "croatia": "HR",
    "curaçao": "CW",
    "cuba": "CU",
    "cyprus": "CY",
    "czech republic": "CZ",
    "denmark": "DK",
    "djibouti": "DJ",
    "dominica": "DM",
    "dominican republic": "DO",
    "ecuador": "EC",
    "egypt": "EG",
    "el salvador": "SV",
    "equatorial guinea": "GQ",
    "eritrea": "ER",
    "estonia": "EE",
    "ethiopia": "ET",
    "falkland islands (malvinas)": "FK",
    "faroe islands": "FO",
    "fiji": "FJ",
    "finland": "FI",
    "france": "FR",
    "french guiana": "GF",
    "french polynesia": "PF",
    "french southern territories": "TF",
    "gabon": "GA",
    "gambia": "GM",
    "georgia": "GE",
    "germany": "DE",
    "ghana": "GH",
    "gibraltar": "GI",
    "greece": "GR",
    "greenland": "GL",
    "grenada": "GD",
    "guadeloupe": "GP",
    "guam": "GU",
    "guatemala": "GT",
    "guernsey": "GG",
    "guinea": "GN",
    "guinea-bissau": "GW",
    "guyana": "GY",
    "haiti": "HT",
    "heard island": "HM",
    "holy see": "VA",
    "honduras": "HN",
    "hong kong": "HK",
    "hungary": "HU",
    "iceland": "IS",
    "india": "IN",
    "indonesia": "ID",
    "iran": "IR",
    "iraq": "IQ",
    "ireland": "IE",
    "isle of man": "IM",
    "israel": "IL",
    "italy": "IT",
    "jamaica": "JM",
    "japan": "JP",
    "jersey": "JE",
    "jordan": "JO",
    "kazakhstan": "KZ",
    "kenya": "KE",
    "kiribati": "KI",
    "korea": "KP",
    "korea": "KR",
    "kuwait": "KW",
    "kyrgyzstan": "KG",
    "kyrgyz republic": "KG",
    "lao people's democratic republic": "LA",
    "latvia": "LV",
    "lebanon": "LB",
    "lesotho": "LS",
    "liberia": "LR",
    "libyan arab jamahiriya": "LY",
    "liechtenstein": "LI",
    "lithuania": "LT",
    "luxembourg": "LU",
    "macao": "MO",
    "macedonia": "MK",
    "madagascar": "MG",
    "malawi": "MW",
    "malaysia": "MY",
    "maldives": "MV",
    "mali": "ML",
    "malta": "MT",
    "marshall islands": "MH",
    "martinique": "MQ",
    "mauritania": "MR",
    "mauritius": "MU",
    "mayotte": "YT",
    "mexico": "MX",
    "micronesia": "FM",
    "moldova": "MD",
    "monaco": "MC",
    "mongolia": "MN",
    "montenegro": "ME",
    "montserrat": "MS",
    "morocco": "MA",
    "marocco": "MA",
    "mozambique": "MZ",
    "myanmar": "MM",
    "namibia": "NA",
    "nauru": "NR",
    "nepal": "NP",
    "netherlands": "NL",
    "new caledonia": "NC",
    "new zealand": "NZ",
    "nicaragua": "NI",
    "niger": "NE",
    "nigeria": "NG",
    "niue": "NU",
    "norfolk island": "NF",
    "northern mariana islands": "MP",
    "norway": "NO",
    "oman": "OM",
    "pakistan": "PK",
    "palau": "PW",
    "palestinian territory, occupied": "PS",
    "panama": "PA",
    "papua new guinea": "PG",
    "paraguay": "PY",
    "peru": "PE",
    "philippines": "PH",
    "pitcairn": "PN",
    "poland": "PL",
    "portugal": "PT",
    "puerto rico": "PR",
    "qatar": "QA",
    "reunion": "RE",
    "romania": "RO",
    "russian federation": "RU",
    "rwanda": "RW",
    "saint barthélemy": "BL",
    "saint helena": "SH",
    "saint kitts and nevis": "KN",
    "saint lucia": "LC",
    "saint martin": "MF",
    "saint pierre and miquelon": "PM",
    "saint vincent and the grenadines": "VC",
    "samoa": "WS",
    "san marino": "SM",
    "sao tome and principe": "ST",
    "saudi arabia": "SA",
    "senegal": "SN",
    "serbia": "RS",
    "seychelles": "SC",
    "sierra leone": "SL",
    "singapore": "SG",
    "sint maarten": "SX",
    "slovakia": "SK",
    "slovenia": "SI",
    "solomon islands": "SB",
    "somalia": "SO",
    "south africa": "ZA",
    "southern africa": "ZA",
    "south georgia and the south sandwich islands": "GS",
    "spain": "ES",
    "sri lanka": "LK",
    "sudan": "SD",
    "suriname": "SR",
    "svalbard and jan mayen": "SJ",
    "swaziland": "SZ",
    "sweden": "SE",
    "switzerland": "CH",
    "syrian arab republic": "SY",
    "taiwan, province of china": "TW",
    "tajikistan": "TJ",
    "tanzania, united republic of": "TZ",
    "thailand": "TH",
    "timor-leste": "TL",
    "togo": "TG",
    "tokelau": "TK",
    "tonga": "TO",
    "trinidad and tobago": "TT",
    "tunisia": "TN",
    "turkey": "TR",
    "turkmenistan": "TM",
    "turks and caicos islands": "TC",
    "tuvalu": "TV",
    "uganda": "UG",
    "ukraine": "UA",
    "united arab emirates": "AE",
    "united kingdom": "GB",
    "united states": "US",
    "united states minor outlying islands": "UM",
    "uruguay": "UY",
    "uzbekistan": "UZ",
    "vanuatu": "VU",
    "venezuela, bolivarian republic of": "VE",
    "viet nam": "VN",
    "virgin islands, british": "VG",
    "virgin islands, u.s.": "VI",
    "wallis and futuna": "WF",
    "western sahara": "EH",
    "yemen": "YE",
    "zambia": "ZM",
    "zimbabwe": "ZW"
}