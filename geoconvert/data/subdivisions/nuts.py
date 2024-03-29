import re

NUTS_CODES_BY_COUNTRY = {
    "DE": {
        "DE1": "BW",
        "DE11": "BW",
        "DE111": "BW",
        "DE112": "BW",
        "DE113": "BW",
        "DE114": "BW",
        "DE115": "BW",
        "DE116": "BW",
        "DE117": "BW",
        "DE118": "BW",
        "DE119": "BW",
        "DE11A": "BW",
        "DE11B": "BW",
        "DE11C": "BW",
        "DE11D": "BW",
        "DE12": "BW",
        "DE121": "BW",
        "DE122": "BW",
        "DE123": "BW",
        "DE124": "BW",
        "DE125": "BW",
        "DE126": "BW",
        "DE127": "BW",
        "DE128": "BW",
        "DE129": "BW",
        "DE12A": "BW",
        "DE12B": "BW",
        "DE12C": "BW",
        "DE13": "BW",
        "DE131": "BW",
        "DE132": "BW",
        "DE133": "BW",
        "DE134": "BW",
        "DE135": "BW",
        "DE136": "BW",
        "DE137": "BW",
        "DE138": "BW",
        "DE139": "BW",
        "DE13A": "BW",
        "DE14": "BW",
        "DE141": "BW",
        "DE142": "BW",
        "DE143": "BW",
        "DE144": "BW",
        "DE145": "BW",
        "DE146": "BW",
        "DE147": "BW",
        "DE148": "BW",
        "DE149": "BW",
        "DE2": "BY",
        "DE21": "BY",
        "DE211": "BY",
        "DE212": "BY",
        "DE213": "BY",
        "DE214": "BY",
        "DE215": "BY",
        "DE216": "BY",
        "DE217": "BY",
        "DE218": "BY",
        "DE219": "BY",
        "DE21A": "BY",
        "DE21B": "BY",
        "DE21C": "BY",
        "DE21D": "BY",
        "DE21E": "BY",
        "DE21F": "BY",
        "DE21G": "BY",
        "DE21H": "BY",
        "DE21I": "BY",
        "DE21J": "BY",
        "DE21K": "BY",
        "DE21L": "BY",
        "DE21M": "BY",
        "DE21N": "BY",
        "DE22": "BY",
        "DE221": "BY",
        "DE222": "BY",
        "DE223": "BY",
        "DE224": "BY",
        "DE225": "BY",
        "DE226": "BY",
        "DE227": "BY",
        "DE228": "BY",
        "DE229": "BY",
        "DE22A": "BY",
        "DE22B": "BY",
        "DE22C": "BY",
        "DE23": "BY",
        "DE231": "BY",
        "DE232": "BY",
        "DE233": "BY",
        "DE234": "BY",
        "DE235": "BY",
        "DE236": "BY",
        "DE237": "BY",
        "DE238": "BY",
        "DE239": "BY",
        "DE23A": "BY",
        "DE24": "BY",
        "DE241": "BY",
        "DE242": "BY",
        "DE243": "BY",
        "DE244": "BY",
        "DE245": "BY",
        "DE246": "BY",
        "DE247": "BY",
        "DE248": "BY",
        "DE249": "BY",
        "DE24A": "BY",
        "DE24B": "BY",
        "DE24C": "BY",
        "DE24D": "BY",
        "DE25": "BY",
        "DE251": "BY",
        "DE252": "BY",
        "DE253": "BY",
        "DE254": "BY",
        "DE255": "BY",
        "DE256": "BY",
        "DE257": "BY",
        "DE258": "BY",
        "DE259": "BY",
        "DE25A": "BY",
        "DE25B": "BY",
        "DE25C": "BY",
        "DE26": "BY",
        "DE261": "BY",
        "DE262": "BY",
        "DE263": "BY",
        "DE264": "BY",
        "DE265": "BY",
        "DE266": "BY",
        "DE267": "BY",
        "DE268": "BY",
        "DE269": "BY",
        "DE26A": "BY",
        "DE26B": "BY",
        "DE26C": "BY",
        "DE27": "BY",
        "DE271": "BY",
        "DE272": "BY",
        "DE273": "BY",
        "DE274": "BY",
        "DE275": "BY",
        "DE276": "BY",
        "DE277": "BY",
        "DE278": "BY",
        "DE279": "BY",
        "DE27A": "BY",
        "DE27B": "BY",
        "DE27C": "BY",
        "DE27D": "BY",
        "DE27E": "BY",
        "DE3": "BE",
        "DE30": "BE",
        "DE300": "BE",
        "DE4": "BB",
        "DE41": "BB",
        "DE411": "BB",
        "DE412": "BB",
        "DE413": "BB",
        "DE414": "BB",
        "DE415": "BB",
        "DE416": "BB",
        "DE417": "BB",
        "DE418": "BB",
        "DE42": "BB",
        "DE421": "BB",
        "DE422": "BB",
        "DE423": "BB",
        "DE424": "BB",
        "DE425": "BB",
        "DE426": "BB",
        "DE427": "BB",
        "DE428": "BB",
        "DE429": "BB",
        "DE42A": "BB",
        "DE5": "HB",
        "DE50": "HB",
        "DE501": "HB",
        "DE502": "HB",
        "DE6": "HH",
        "DE60": "HH",
        "DE600": "HH",
        "DE7": "HE",
        "DE71": "HE",
        "DE711": "HE",
        "DE712": "HE",
        "DE713": "HE",
        "DE714": "HE",
        "DE715": "HE",
        "DE716": "HE",
        "DE717": "HE",
        "DE718": "HE",
        "DE719": "HE",
        "DE71A": "HE",
        "DE71B": "HE",
        "DE71C": "HE",
        "DE71D": "HE",
        "DE71E": "HE",
        "DE72": "HE",
        "DE721": "HE",
        "DE722": "HE",
        "DE723": "HE",
        "DE724": "HE",
        "DE725": "HE",
        "DE73": "HE",
        "DE731": "HE",
        "DE732": "HE",
        "DE733": "HE",
        "DE734": "HE",
        "DE735": "HE",
        "DE736": "HE",
        "DE737": "HE",
        "DE8": "MV",
        "DE80": "MV",
        "DE801": "MV",
        "DE802": "MV",
        "DE803": "MV",
        "DE804": "MV",
        "DE805": "MV",
        "DE806": "MV",
        "DE807": "MV",
        "DE808": "MV",
        "DE809": "MV",
        "DE80A": "MV",
        "DE80B": "MV",
        "DE80C": "MV",
        "DE80D": "MV",
        "DE80E": "MV",
        "DE80F": "MV",
        "DE80G": "MV",
        "DE80H": "MV",
        "DE80I": "MV",
        "DE9": "NI",
        "DE91": "NI",
        "DE911": "NI",
        "DE912": "NI",
        "DE913": "NI",
        "DE914": "NI",
        "DE915": "NI",
        "DE916": "NI",
        "DE917": "NI",
        "DE918": "NI",
        "DE919": "NI",
        "DE91A": "NI",
        "DE91B": "NI",
        "DE92": "NI",
        "DE922": "NI",
        "DE923": "NI",
        "DE925": "NI",
        "DE926": "NI",
        "DE927": "NI",
        "DE928": "NI",
        "DE929": "NI",
        "DE93": "NI",
        "DE931": "NI",
        "DE932": "NI",
        "DE933": "NI",
        "DE934": "NI",
        "DE935": "NI",
        "DE936": "NI",
        "DE937": "NI",
        "DE938": "NI",
        "DE939": "NI",
        "DE93A": "NI",
        "DE93B": "NI",
        "DE94": "NI",
        "DE941": "NI",
        "DE942": "NI",
        "DE943": "NI",
        "DE944": "NI",
        "DE945": "NI",
        "DE946": "NI",
        "DE947": "NI",
        "DE948": "NI",
        "DE949": "NI",
        "DE94A": "NI",
        "DE94B": "NI",
        "DE94C": "NI",
        "DE94D": "NI",
        "DE94E": "NI",
        "DE94F": "NI",
        "DE94G": "NI",
        "DE94H": "NI",
        "DEA": "NW",
        "DEA1": "NW",
        "DEA11": "NW",
        "DEA12": "NW",
        "DEA13": "NW",
        "DEA14": "NW",
        "DEA15": "NW",
        "DEA16": "NW",
        "DEA17": "NW",
        "DEA18": "NW",
        "DEA19": "NW",
        "DEA1A": "NW",
        "DEA1B": "NW",
        "DEA1C": "NW",
        "DEA1D": "NW",
        "DEA1E": "NW",
        "DEA1F": "NW",
        "DEA2": "NW",
        "DEA21": "NW",
        "DEA22": "NW",
        "DEA23": "NW",
        "DEA24": "NW",
        "DEA25": "NW",
        "DEA26": "NW",
        "DEA27": "NW",
        "DEA28": "NW",
        "DEA29": "NW",
        "DEA2A": "NW",
        "DEA2B": "NW",
        "DEA2C": "NW",
        "DEA3": "NW",
        "DEA31": "NW",
        "DEA32": "NW",
        "DEA33": "NW",
        "DEA34": "NW",
        "DEA35": "NW",
        "DEA36": "NW",
        "DEA37": "NW",
        "DEA38": "NW",
        "DEA4": "NW",
        "DEA41": "NW",
        "DEA42": "NW",
        "DEA43": "NW",
        "DEA44": "NW",
        "DEA45": "NW",
        "DEA46": "NW",
        "DEA47": "NW",
        "DEA5": "NW",
        "DEA51": "NW",
        "DEA52": "NW",
        "DEA53": "NW",
        "DEA54": "NW",
        "DEA55": "NW",
        "DEA56": "NW",
        "DEA57": "NW",
        "DEA58": "NW",
        "DEA59": "NW",
        "DEA5A": "NW",
        "DEA5B": "NW",
        "DEA5C": "NW",
        "DEB": "RP",
        "DEB1": "RP",
        "DEB11": "RP",
        "DEB12": "RP",
        "DEB13": "RP",
        "DEB14": "RP",
        "DEB15": "RP",
        "DEB16": "RP",
        "DEB17": "RP",
        "DEB18": "RP",
        "DEB19": "RP",
        "DEB1A": "RP",
        "DEB1B": "RP",
        "DEB2": "RP",
        "DEB21": "RP",
        "DEB22": "RP",
        "DEB23": "RP",
        "DEB24": "RP",
        "DEB25": "RP",
        "DEB3": "RP",
        "DEB31": "RP",
        "DEB32": "RP",
        "DEB33": "RP",
        "DEB34": "RP",
        "DEB35": "RP",
        "DEB36": "RP",
        "DEB37": "RP",
        "DEB38": "RP",
        "DEB39": "RP",
        "DEB3A": "RP",
        "DEB3B": "RP",
        "DEB3C": "RP",
        "DEB3D": "RP",
        "DEB3E": "RP",
        "DEB3F": "RP",
        "DEB3G": "RP",
        "DEB3H": "RP",
        "DEB3I": "RP",
        "DEB3J": "RP",
        "DEB3K": "RP",
        "DEC": "SL",
        "DEC0": "SL",
        "DEC01": "SL",
        "DEC02": "SL",
        "DEC03": "SL",
        "DEC04": "SL",
        "DEC05": "SL",
        "DEC06": "SL",
        "DED": "SN",
        "DED1": "SN",
        "DED11": "SN",
        "DED12": "SN",
        "DED13": "SN",
        "DED14": "SN",
        "DED15": "SN",
        "DED16": "SN",
        "DED17": "SN",
        "DED18": "SN",
        "DED19": "SN",
        "DED1A": "SN",
        "DED1B": "SN",
        "DED1C": "SN",
        "DED2": "SN",
        "DED21": "SN",
        "DED22": "SN",
        "DED23": "SN",
        "DED24": "SN",
        "DED25": "SN",
        "DED26": "SN",
        "DED27": "SN",
        "DED28": "SN",
        "DED29": "SN",
        "DED2A": "SN",
        "DED2B": "SN",
        "DED3": "SN",
        "DED31": "SN",
        "DED32": "SN",
        "DED33": "SN",
        "DED34": "SN",
        "DED35": "SN",
        "DED36": "SN",
        "DEE": "ST",
        "DEE0": "ST",
        "DEE01": "ST",
        "DEE02": "ST",
        "DEE03": "ST",
        "DEE04": "ST",
        "DEE05": "ST",
        "DEE06": "ST",
        "DEE07": "ST",
        "DEE08": "ST",
        "DEE09": "ST",
        "DEE0A": "ST",
        "DEE0B": "ST",
        "DEE0C": "ST",
        "DEE0D": "ST",
        "DEE0E": "ST",
        "DEF": "SH",
        "DEF0": "SH",
        "DEF01": "SH",
        "DEF02": "SH",
        "DEF03": "SH",
        "DEF04": "SH",
        "DEF05": "SH",
        "DEF06": "SH",
        "DEF07": "SH",
        "DEF08": "SH",
        "DEF09": "SH",
        "DEF0A": "SH",
        "DEF0B": "SH",
        "DEF0C": "SH",
        "DEF0D": "SH",
        "DEF0E": "SH",
        "DEF0F": "SH",
        "DEG": "TH",
        "DEG0": "TH",
        "DEG01": "TH",
        "DEG02": "TH",
        "DEG03": "TH",
        "DEG04": "TH",
        "DEG05": "TH",
        "DEG06": "TH",
        "DEG07": "TH",
        "DEG09": "TH",
        "DEG0A": "TH",
        "DEG0B": "TH",
        "DEG0C": "TH",
        "DEG0D": "TH",
        "DEG0E": "TH",
        "DEG0F": "TH",
        "DEG0G": "TH",
        "DEG0H": "TH",
        "DEG0I": "TH",
        "DEG0J": "TH",
        "DEG0K": "TH",
        "DEG0L": "TH",
        "DEG0M": "TH",
        "DEG0N": "TH",
        "DEG0P": "TH",
        # Not a subdivision but can be used to detect country
        "DEZ": None,
        "DEZZ": None,
        "DEZZZ": None,
    },
    "FR": {
        # old regions
        "FR1": None,
        "FR10": None,
        "FR101": "75",
        "FR102": "77",
        "FR103": "78",
        "FR104": "91",
        "FR105": "92",
        "FR106": "93",
        "FR107": "94",
        "FR108": "95",
        "FR2": None,
        "FR21": None,
        "FR211": "08",
        "FR212": "10",
        "FR213": "51",
        "FR214": "52",
        "FR22": None,
        "FR221": "02",
        "FR222": "60",
        "FR223": "80",
        "FR23": None,
        "FR231": "27",
        "FR232": "76",
        "FR24": None,
        "FR241": "18",
        "FR242": "28",
        "FR243": "36",
        "FR244": "37",
        "FR245": "41",
        "FR246": "45",
        "FR25": None,
        "FR251": "14",
        "FR252": "50",
        "FR253": "61",
        "FR26": None,
        "FR261": "21",
        "FR262": "58",
        "FR263": "71",
        "FR264": "89",
        "FR3": None,
        "FR30": None,
        "FR301": "59",
        "FR302": "62",
        "FR4": None,
        "FR41": None,
        "FR411": "54",
        "FR412": "55",
        "FR413": "57",
        "FR414": "88",
        "FR42": None,
        "FR421": "67",
        "FR422": "68",
        "FR43": None,
        "FR431": "25",
        "FR432": "39",
        "FR433": "70",
        "FR434": "90",
        "FR5": None,
        "FR51": None,
        "FR511": "44",
        "FR512": "49",
        "FR513": "53",
        "FR514": "72",
        "FR515": "85",
        "FR52": None,
        "FR521": "22",
        "FR522": "29",
        "FR523": "35",
        "FR524": "56",
        "FR53": None,
        "FR531": "16",
        "FR532": "17",
        "FR533": "79",
        "FR534": "86",
        "FR6": None,
        "FR61": None,
        "FR611": "24",
        "FR612": "33",
        "FR613": "40",
        "FR614": "47",
        "FR615": "64",
        "FR62": None,
        "FR621": "09",
        "FR622": "12",
        "FR623": "31",
        "FR624": "32",
        "FR625": "46",
        "FR626": "65",
        "FR627": "81",
        "FR628": "82",
        "FR63": None,
        "FR631": "19",
        "FR632": "23",
        "FR633": "87",
        "FR7": None,
        "FR71": None,
        "FR711": "01",
        "FR712": "07",
        "FR713": "26",
        "FR714": "38",
        "FR715": "42",
        "FR716": "69",
        "FR717": "73",
        "FR718": "74",
        "FR72": None,
        "FR721": "03",
        "FR722": "15",
        "FR723": "43",
        "FR724": "63",
        "FR8": None,
        "FR81": None,
        "FR811": "11",
        "FR812": "30",
        "FR813": "34",
        "FR814": "48",
        "FR815": "66",
        "FR82": None,
        "FR821": "04",
        "FR822": "05",
        "FR823": "06",
        "FR824": "13",
        "FR825": "83",
        "FR826": "84",
        "FR83": "20A",
        "FR831": "20A",
        "FR832": "20B",
        "FR9": None,
        "FR91": None,
        "FR910": None,
        "FR92": None,
        "FR920": None,
        "FR93": "973",
        "FR930": "973",
        "FR94": "974",
        "FR940": "974",
        "FRA": None,
        "FRA1": "971",
        "FRA10": "971",
        "FRA2": "972",
        "FRA20": "972",
        "FRA3": "973",
        "FRA30": "973",
        "FRA4": "974",
        "FRA40": "974",
        "FRA5": "976",
        "FRA50": "976",
        # new regions
        "FRB": None,
        "FRB0": None,
        "FRB01": "18",
        "FRB02": "28",
        "FRB03": "36",
        "FRB04": "37",
        "FRB05": "41",
        "FRB06": "45",
        "FRC": None,
        "FRC1": None,
        "FRC11": "21",
        "FRC12": "58",
        "FRC13": "71",
        "FRC14": "89",
        "FRC2": None,
        "FRC21": "25",
        "FRC22": "39",
        "FRC23": "70",
        "FRC24": "90",
        "FRD": None,
        "FRD1": None,
        "FRD11": "14",
        "FRD12": "50",
        "FRD13": "61",
        "FRD2": None,
        "FRD21": "27",
        "FRD22": "76",
        "FRE": None,
        "FRE1": "59",
        "FRE11": "59",
        "FRE12": "62",
        "FRE2": None,
        "FRE21": "02",
        "FRE22": "60",
        "FRE23": "80",
        "FRF": None,
        "FRF1": None,
        "FRF11": "67",
        "FRF12": "68",
        "FRF2": None,
        "FRF21": "08",
        "FRF22": "10",
        "FRF23": "51",
        "FRF24": "52",
        "FRF3": None,
        "FRF31": "54",
        "FRF32": "55",
        "FRF33": "57",
        "FRF34": "88",
        "FRG": None,
        "FRG0": None,
        "FRG01": "44",
        "FRG02": "49",
        "FRG03": "53",
        "FRG04": "72",
        "FRG05": "85",
        "FRH": None,
        "FRH0": None,
        "FRH01": "22",
        "FRH02": "29",
        "FRH03": "35",
        "FRH04": "56",
        "FRI": None,
        "FRI1": None,
        "FRI11": "24",
        "FRI12": "33",
        "FRI13": "40",
        "FRI14": "47",
        "FRI15": "64",
        "FRI2": None,
        "FRI21": "19",
        "FRI22": "23",
        "FRI23": "87",
        "FRI3": None,
        "FRI31": "16",
        "FRI32": "17",
        "FRI33": "79",
        "FRI34": "86",
        "FRJ": None,
        "FRJ1": None,
        "FRJ11": "11",
        "FRJ12": "30",
        "FRJ13": "34",
        "FRJ14": "48",
        "FRJ15": "66",
        "FRJ2": None,
        "FRJ21": "09",
        "FRJ22": "12",
        "FRJ23": "31",
        "FRJ24": "32",
        "FRJ25": "46",
        "FRJ26": "65",
        "FRJ27": "81",
        "FRJ28": "82",
        "FRK": None,
        "FRK1": None,
        "FRK11": "03",
        "FRK12": "15",
        "FRK13": "43",
        "FRK14": "63",
        "FRK2": None,
        "FRK21": "01",
        "FRK22": "07",
        "FRK23": "26",
        "FRK24": "38",
        "FRK25": "42",
        "FRK26": "69",
        "FRK27": "73",
        "FRK28": "74",
        "FRL": None,
        "FRL0": None,
        "FRL01": "04",
        "FRL02": "05",
        "FRL03": "06",
        "FRL04": "13",
        "FRL05": "83",
        "FRL06": "84",
        "FRM": None,
        "FRM0": None,
        "FRM01": "20A",
        "FRM02": "20B",
        "FRY": None,
        "FRY1": "971",
        "FRY10": "971",
        "FRY2": "972",
        "FRY20": "972",
        "FRY3": "973",
        "FRY30": "973",
        "FRY4": "974",
        "FRY40": "974",
        "FRY5": "976",
        "FRY50": "976",
        # Not a subdivision but can be used to detect country
        "FRZ": None,
        "FRZZ": None,
        "FRZZZ": None,
    },
}

ALL_NUTS_CODES = {
    nuts_code: subdivision
    for nuts_by_country in NUTS_CODES_BY_COUNTRY.values()
    for nuts_code, subdivision in nuts_by_country.items()
}

# Regexes
nuts_regexes_by_country = {
    country: re.compile(r"|".join(rf"\b{code}\b" for code in nuts_codes.keys()), re.I)
    for country, nuts_codes in NUTS_CODES_BY_COUNTRY.items()
}
all_nuts_regex = re.compile(
    r"|".join(rf"\b{code}\b" for code in ALL_NUTS_CODES.keys()),
    re.I,
)
