# -*- coding: utf8 -*-
import re

def country2code(country, lang='FR'):
    """
    Get country name and return his code.
    >>> country2code('france')
    'FR'

    >>> country2code('Madagascar')
    'MG'

    >>> country2code(u'S\xe9n\xe9gal')
    'SN'

    >>> country2code('République démocratique du Congo')
    'CD'

    >>> country2code('Mali')
    'ML'

    >>> country2code('Sri Lanka ')
    'LK'

    >>> country2code(u'\xa0V\xe9n\xe9zuela\xa0')
    'VE'

    >>> country2code('Mongolia', lang='EN')
    'MN'

    >>> country2code('Marocco', lang='EN')
    'MA'

    >>> country2code('Georgia', lang='EN')
    'GE'

    >>> country2code('Namibia', lang='EN')
    'NA'

    >>> country2code('Armenia', lang='EN')
    'AM'

    >>> country2code('sweden', lang='EN')
    'SE'

    >>> country2code(u'Vi\xeatnam')
    'VN'

    """
    country_dict_fr = dict()
    country_dict_fr['andorre'] = 'AD'
    country_dict_fr['emirats arabes unis'] = 'AE'
    country_dict_fr['afghanistan'] = 'AF'
    country_dict_fr['antigua et barbuda'] = 'AG'
    country_dict_fr['anguilla'] = 'AI'
    country_dict_fr['albanie'] = 'AL'
    country_dict_fr['armenie'] = 'AM'
    country_dict_fr['antilles neerlandaises'] = 'AN'
    country_dict_fr['angola'] = 'AO'
    country_dict_fr['antarctique'] = 'AQ'
    country_dict_fr['argentine'] = 'AR'
    country_dict_fr['samoa americaines'] = 'AS'
    country_dict_fr['autriche'] = 'AT'
    country_dict_fr['australie'] = 'AU'
    country_dict_fr['aruba'] = 'AW'
    country_dict_fr['aland'] = 'AX'
    country_dict_fr['azerbaidjan'] = 'AZ'
    country_dict_fr['bosnie-herzegovine'] = 'BA'
    country_dict_fr['barbade'] = 'BB'
    country_dict_fr['bangladesh'] = 'BD'
    country_dict_fr['belgique'] = 'BE'
    country_dict_fr['burkina faso'] = 'BF'
    country_dict_fr['bulgarie'] = 'BG'
    country_dict_fr['bahrein'] = 'BH'
    country_dict_fr['burundi'] = 'BI'
    country_dict_fr['benin'] = 'BJ'
    country_dict_fr['bermudes'] = 'BM'
    country_dict_fr['brunei darussalam'] = 'BN'
    country_dict_fr['bolivie'] = 'BO'
    country_dict_fr['bresil'] = 'BR'
    country_dict_fr['bahamas'] = 'BS'
    country_dict_fr['bhoutan'] = 'BT'
    country_dict_fr['bouvet'] = 'BV'
    country_dict_fr['botswana'] = 'BW'
    country_dict_fr['belarus'] = 'BY'
    country_dict_fr['belize'] = 'BZ'
    country_dict_fr['canada'] = 'CA'
    country_dict_fr['r.+publique d.+mocratique du congo'] = 'CD'
    country_dict_fr['cocos (keeling)'] = 'CC'
    country_dict_fr['centrafricaine'] = 'CF'
    country_dict_fr['congo'] = 'CG'
    country_dict_fr['suisse'] = 'CH'
    country_dict_fr['côte d\'ivoire'] = 'CI'
    country_dict_fr['cook'] = 'CK'
    country_dict_fr['chili'] = 'CL'
    country_dict_fr['cameroun'] = 'CM'
    country_dict_fr['chine'] = 'CN'
    country_dict_fr['colombie'] = 'CO'
    country_dict_fr['costa rica'] = 'CR'
    country_dict_fr['cuba'] = 'CU'
    country_dict_fr['cap-vert'] = 'CV'
    country_dict_fr['christmas'] = 'CX'
    country_dict_fr['chypre'] = 'CY'
    country_dict_fr['tcheque'] = 'CZ'
    country_dict_fr['allemagne'] = 'DE'
    country_dict_fr['djibouti'] = 'DJ'
    country_dict_fr['danemark'] = 'DK'
    country_dict_fr['dominique'] = 'DM'
    country_dict_fr['dominicaine'] = 'DO'
    country_dict_fr['algerie'] = 'dZ'
    country_dict_fr['equateur'] = 'EC'
    country_dict_fr['estonie'] = 'EE'
    country_dict_fr['egypte'] = 'EG'
    country_dict_fr['sahara occidental'] = 'EH'
    country_dict_fr['erythree'] = 'ER'
    country_dict_fr['espagne'] = 'ES'
    country_dict_fr['ethiopie'] = 'ET'
    country_dict_fr['finlande'] = 'FI'
    country_dict_fr['fidji'] = 'FJ'
    country_dict_fr['falkland'] = 'FK'
    country_dict_fr['micronesie'] = 'FM'
    country_dict_fr['feroe'] = 'FO'
    country_dict_fr['france'] = 'FR'
    country_dict_fr['gabon'] = 'GA'
    country_dict_fr['royaume-uni'] = 'GB'
    country_dict_fr['grenade'] = 'GD'
    country_dict_fr['georgie'] = 'GE'
    country_dict_fr['guyane francaise'] = 'GF'
    country_dict_fr['guernesey'] = 'GG'
    country_dict_fr['ghana'] = 'GH'
    country_dict_fr['gibraltar'] = 'GI'
    country_dict_fr['groenland'] = 'GL'
    country_dict_fr['gambie'] = 'GM'
    country_dict_fr['guinee'] = 'GN'
    country_dict_fr['guadeloupe'] = 'GP'
    country_dict_fr['guinee equatoriale'] = 'GQ'
    country_dict_fr['grece'] = 'GR'
    country_dict_fr['georgie du sud et les iles sandwich du sud'] = 'GS'
    country_dict_fr['guatemala'] = 'GT'
    country_dict_fr['guam'] = 'GU'
    country_dict_fr['guinee-bissau'] = 'GW'
    country_dict_fr['guyana'] = 'GY'
    country_dict_fr['hong-kong'] = 'HK'
    country_dict_fr['heard'] = 'HM'
    country_dict_fr['honduras'] = 'HN'
    country_dict_fr['croatie'] = 'HR'
    country_dict_fr['haiti'] = 'HT'
    country_dict_fr['hongrie'] = 'HU'
    country_dict_fr['indonesie'] = 'ID'
    country_dict_fr['irlande'] = 'IE'
    country_dict_fr['israël'] = 'IL'
    country_dict_fr['ile de man'] = 'IM'
    country_dict_fr['inde'] = 'IN'
    country_dict_fr['ocean indien'] = 'IO'
    country_dict_fr['iraq'] = 'IQ'
    country_dict_fr['iran'] = 'IR'
    country_dict_fr['islande'] = 'IS'
    country_dict_fr['italie'] = 'IT'
    country_dict_fr['jersey'] = 'JE'
    country_dict_fr['jamaique'] = 'JM'
    country_dict_fr['jordanie'] = 'JO'
    country_dict_fr['japon'] = 'JP'
    country_dict_fr['kenya'] = 'KE'
    country_dict_fr['kirghizistan'] = 'KG'
    country_dict_fr['cambodge'] = 'kH'
    country_dict_fr['kiribati'] = 'KI'
    country_dict_fr['comores'] = 'kM'
    country_dict_fr['saint-kitts-et-nevis'] = 'KN'
    country_dict_fr['kosovo'] = 'KO'
    country_dict_fr['coree'] = 'KP'
    country_dict_fr['coree'] = 'KR'
    country_dict_fr['koweit'] = 'KW'
    country_dict_fr['caimanes'] = 'KY'
    country_dict_fr['kazakhstan'] = 'KZ'
    country_dict_fr['lao'] = 'LA'
    country_dict_fr['liban'] = 'LB'
    country_dict_fr['sainte-lucie'] = 'LC'
    country_dict_fr['liechtenstein'] = 'LI'
    country_dict_fr['sri lanka'] = 'LK'
    country_dict_fr['liberia'] = 'LR'
    country_dict_fr['lesotho'] = 'LS'
    country_dict_fr['lituanie'] = 'LT'
    country_dict_fr['luxembourg'] = 'LU'
    country_dict_fr['lettonie'] = 'LV'
    country_dict_fr['libyenne'] = 'LY'
    country_dict_fr['maroc'] = 'MA'
    country_dict_fr['monaco'] = 'MC'
    country_dict_fr['moldova'] = 'MD'
    country_dict_fr['montenegro'] = 'ME'
    country_dict_fr['saint-martin'] = 'MF'
    country_dict_fr['madagascar'] = 'MG'
    country_dict_fr['marshall'] = 'MH'
    country_dict_fr['macedoine'] = 'MK'
    country_dict_fr['mali'] = 'ML'
    country_dict_fr['myanmar'] = 'MM'
    country_dict_fr['mongolie'] = 'MN'
    country_dict_fr['mongolia'] = 'MN'
    country_dict_fr['macao'] = 'MO'
    country_dict_fr['mariannes du nord'] = 'MP'
    country_dict_fr['martinique'] = 'MQ'
    country_dict_fr['mauritanie'] = 'MR'
    country_dict_fr['montserrat'] = 'MS'
    country_dict_fr['malte'] = 'MT'
    country_dict_fr['maurice'] = 'MU'
    country_dict_fr['maldives'] = 'MV'
    country_dict_fr['malawi'] = 'MW'
    country_dict_fr['mexique'] = 'MX'
    country_dict_fr['malaisie'] = 'MY'
    country_dict_fr['mozambique'] = 'MZ'
    country_dict_fr['namibie'] = 'NA'
    country_dict_fr['nouvelle-caledonie'] = 'NC'
    country_dict_fr['niger'] = 'NE'
    country_dict_fr['norfolk'] = 'NF'
    country_dict_fr['nigeria'] = 'NG'
    country_dict_fr['nicaragua'] = 'NI'
    country_dict_fr['pays-bas'] = 'NL'
    country_dict_fr['norvege'] = 'NO'
    country_dict_fr['nepal'] = 'NP'
    country_dict_fr['nauru'] = 'NR'
    country_dict_fr['niue'] = 'NU'
    country_dict_fr['nouvelle-zelande'] = 'NZ'
    country_dict_fr['oman'] = 'OM'
    country_dict_fr['panama'] = 'PA'
    country_dict_fr['perou'] = 'PE'
    country_dict_fr['polynesie francaise'] = 'PF'
    country_dict_fr['papouasie-nouvelle-guinee'] = 'PG'
    country_dict_fr['philippines'] = 'PH'
    country_dict_fr['pakistan'] = 'PK'
    country_dict_fr['pologne'] = 'PL'
    country_dict_fr['saint-pierre-et-miquelon'] = 'PM'
    country_dict_fr['pitcairn'] = 'PN'
    country_dict_fr['porto rico'] = 'PR'
    country_dict_fr['palestinien occupe'] = 'PS'
    country_dict_fr['portugal'] = 'PT'
    country_dict_fr['palaos'] = 'PW'
    country_dict_fr['paraguay'] = 'PY'
    country_dict_fr['qatar'] = 'QA'
    country_dict_fr['reunion'] = 'RE'
    country_dict_fr['roumanie'] = 'RO'
    country_dict_fr['serbie'] = 'RS'
    country_dict_fr['russie'] = 'RU'
    country_dict_fr['rwanda'] = 'RW'
    country_dict_fr['arabie saoudite'] = 'SA'
    country_dict_fr['salomon'] = 'SB'
    country_dict_fr['seychelles'] = 'SC'
    country_dict_fr['soudan'] = 'SD'
    country_dict_fr['suede'] = 'SE'
    country_dict_fr['singapour'] = 'SG'
    country_dict_fr['sainte-helene'] = 'SH'
    country_dict_fr['slovenie'] = 'SI'
    country_dict_fr['svalbard et ile jan mayen'] = 'SJ'
    country_dict_fr['slovaquie'] = 'SK'
    country_dict_fr['sierra leone'] = 'SL'
    country_dict_fr['saint-marin'] = 'SM'
    country_dict_fr['senegal'] = 'SN'
    country_dict_fr['somalie'] = 'SO'
    country_dict_fr['suriname'] = 'SR'
    country_dict_fr['sao tome-et-principe'] = 'ST'
    country_dict_fr['el salvador'] = 'SV'
    country_dict_fr['syrienne'] = 'SY'
    country_dict_fr['swaziland'] = 'SZ'
    country_dict_fr['turks et caiques'] = 'TC'
    country_dict_fr['tchad'] = 'TD'
    country_dict_fr['terres australes francaises'] = 'TF'
    country_dict_fr['togo'] = 'TG'
    country_dict_fr['thailande'] = 'TH'
    country_dict_fr['tadjikistan'] = 'TJ'
    country_dict_fr['tokelau'] = 'TK'
    country_dict_fr['timor-leste'] = 'TL'
    country_dict_fr['turkmenistan'] = 'TM'
    country_dict_fr['tunisie'] = 'TN'
    country_dict_fr['tonga'] = 'TO'
    country_dict_fr['turquie'] = 'TR'
    country_dict_fr['trinite-et-Tobago'] = 'TT'
    country_dict_fr['tuvalu'] = 'TV'
    country_dict_fr['taiwan'] = 'TW'
    country_dict_fr['tanzanie'] = 'TZ'
    country_dict_fr['tanzania'] = 'TZ'
    country_dict_fr['ukraine'] = 'UA'
    country_dict_fr['ouganda'] = 'UG'
    country_dict_fr['iles mineures eloignees des etats-unis'] = 'UM'
    country_dict_fr['etats-unis'] = 'US'
    country_dict_fr['uruguay'] = 'UY'
    country_dict_fr['ouzbekistan'] = 'UZ'
    country_dict_fr['vatican'] = 'VA'
    country_dict_fr['saint-vincent-et-les grenadines'] = 'VC'
    country_dict_fr['venezuela'] = 'VE'
    country_dict_fr['iles vierges britanniques'] = 'VG'
    country_dict_fr['iles vierges des etats-unis'] = 'VI'
    country_dict_fr['viet nam'] = 'VN'
    country_dict_fr['vietnam'] = 'VN'
    country_dict_fr['vanuatu'] = 'VU'
    country_dict_fr['wallis et futuna'] = 'WF'
    country_dict_fr['samoa'] = 'WS'
    country_dict_fr['yemen'] = 'YE'
    country_dict_fr['mayotte'] = 'YT'
    country_dict_fr['afrique du sud'] = 'ZA'
    country_dict_fr['zambie'] = 'ZM'
    country_dict_fr['zimbabwe'] = 'ZW'

    country_dict_en = dict()
    country_dict_en['afghanistan'] = 'AF'
    country_dict_en['åland islands'] = 'AX'
    country_dict_en['albania'] = 'AL'
    country_dict_en['algeria'] = 'DZ'
    country_dict_en['american samoa'] = 'AS'
    country_dict_en['andorra'] = 'AD'
    country_dict_en['angola'] = 'AO'
    country_dict_en['anguilla'] = 'AI'
    country_dict_en['antarctica'] = 'AQ'
    country_dict_en['antigua and barbuda'] = 'AG'
    country_dict_en['argentina'] = 'AR'
    country_dict_en['armenia'] = 'AM'
    country_dict_en['aruba'] = 'AW'
    country_dict_en['australia'] = 'AU'
    country_dict_en['austria'] = 'AT'
    country_dict_en['azerbaijan'] = 'AZ'
    country_dict_en['bahamas'] = 'BS'
    country_dict_en['bahrain'] = 'BH'
    country_dict_en['bangladesh'] = 'BD'
    country_dict_en['barbados'] = 'BB'
    country_dict_en['belarus'] = 'BY'
    country_dict_en['belgium'] = 'BE'
    country_dict_en['belize'] = 'BZ'
    country_dict_en['benin'] = 'BJ'
    country_dict_en['bermuda'] = 'BM'
    country_dict_en['bhutan'] = 'BT'
    country_dict_en['bolivia, plurinational state of'] = 'BO'
    country_dict_en['bonaire, saint eustatius and saba'] = 'BQ'
    country_dict_en['bosnia and herzegovina'] = 'BA'
    country_dict_en['botswana'] = 'BW'
    country_dict_en['bouvet island'] = 'BV'
    country_dict_en['brazil'] = 'BR'
    country_dict_en['british indian ocean territory'] = 'IO'
    country_dict_en['brunei darussalam'] = 'BN'
    country_dict_en['bulgaria'] = 'BG'
    country_dict_en['burkina faso'] = 'BF'
    country_dict_en['burundi'] = 'BI'
    country_dict_en['cambodia'] = 'KH'
    country_dict_en['cameroon'] = 'CM'
    country_dict_en['canada'] = 'CA'
    country_dict_en['cape verde'] = 'CV'
    country_dict_en['cayman islands'] = 'KY'
    country_dict_en['central african republic'] = 'CF'
    country_dict_en['chad'] = 'TD'
    country_dict_en['chile'] = 'CL'
    country_dict_en['china'] = 'CN'
    country_dict_en['christmas island'] = 'CX'
    country_dict_en['cocos (keeling) islands'] = 'CC'
    country_dict_en['colombia'] = 'CO'
    country_dict_en['comoros'] = 'KM'
    country_dict_en['congo'] = 'CG'
    country_dict_en['congo, the democratic republic of the'] = 'CD'
    country_dict_en['cook islands'] = 'CK'
    country_dict_en['costa rica'] = 'CR'
    country_dict_en['côte d\'ivoire'] = 'CI'
    country_dict_en['croatia'] = 'HR'
    country_dict_en['curaçao'] = 'CW'
    country_dict_en['cuba'] = 'CU'
    country_dict_en['cyprus'] = 'CY'
    country_dict_en['czech republic'] = 'CZ'
    country_dict_en['denmark'] = 'DK'
    country_dict_en['djibouti'] = 'DJ'
    country_dict_en['dominica'] = 'DM'
    country_dict_en['dominican republic'] = 'DO'
    country_dict_en['ecuador'] = 'EC'
    country_dict_en['egypt'] = 'EG'
    country_dict_en['el salvador'] = 'SV'
    country_dict_en['equatorial guinea'] = 'GQ'
    country_dict_en['eritrea'] = 'ER'
    country_dict_en['estonia'] = 'EE'
    country_dict_en['ethiopia'] = 'ET'
    country_dict_en['falkland islands (malvinas)'] = 'FK'
    country_dict_en['faroe islands'] = 'FO'
    country_dict_en['fiji'] = 'FJ'
    country_dict_en['finland'] = 'FI'
    country_dict_en['france'] = 'FR'
    country_dict_en['french guiana'] = 'GF'
    country_dict_en['french polynesia'] = 'PF'
    country_dict_en['french southern territories'] = 'TF'
    country_dict_en['gabon'] = 'GA'
    country_dict_en['gambia'] = 'GM'
    country_dict_en['georgia'] = 'GE'
    country_dict_en['germany'] = 'DE'
    country_dict_en['ghana'] = 'GH'
    country_dict_en['gibraltar'] = 'GI'
    country_dict_en['greece'] = 'GR'
    country_dict_en['greenland'] = 'GL'
    country_dict_en['grenada'] = 'GD'
    country_dict_en['guadeloupe'] = 'GP'
    country_dict_en['guam'] = 'GU'
    country_dict_en['guatemala'] = 'GT'
    country_dict_en['guernsey'] = 'GG'
    country_dict_en['guinea'] = 'GN'
    country_dict_en['guinea-bissau'] = 'GW'
    country_dict_en['guyana'] = 'GY'
    country_dict_en['haiti'] = 'HT'
    country_dict_en['heard island'] = 'HM'
    country_dict_en['holy see'] = 'VA'
    country_dict_en['honduras'] = 'HN'
    country_dict_en['hong kong'] = 'HK'
    country_dict_en['hungary'] = 'HU'
    country_dict_en['iceland'] = 'IS'
    country_dict_en['india'] = 'IN'
    country_dict_en['indonesia'] = 'ID'
    country_dict_en['iran'] = 'IR'
    country_dict_en['iraq'] = 'IQ'
    country_dict_en['ireland'] = 'IE'
    country_dict_en['isle of man'] = 'IM'
    country_dict_en['israel'] = 'IL'
    country_dict_en['italy'] = 'IT'
    country_dict_en['jamaica'] = 'JM'
    country_dict_en['japan'] = 'JP'
    country_dict_en['jersey'] = 'JE'
    country_dict_en['jordan'] = 'JO'
    country_dict_en['kazakhstan'] = 'KZ'
    country_dict_en['kenya'] = 'KE'
    country_dict_en['kiribati'] = 'KI'
    country_dict_en['korea'] = 'KP'
    country_dict_en['korea'] = 'KR'
    country_dict_en['kuwait'] = 'KW'
    country_dict_en['kyrgyzstan'] = 'KG'
    country_dict_en['kyrgyz republic'] = 'KG'
    country_dict_en['lao people\'s democratic republic'] = 'LA'
    country_dict_en['latvia'] = 'LV'
    country_dict_en['lebanon'] = 'LB'
    country_dict_en['lesotho'] = 'LS'
    country_dict_en['liberia'] = 'LR'
    country_dict_en['libyan arab jamahiriya'] = 'LY'
    country_dict_en['liechtenstein'] = 'LI'
    country_dict_en['lithuania'] = 'LT'
    country_dict_en['luxembourg'] = 'LU'
    country_dict_en['macao'] = 'MO'
    country_dict_en['macedonia'] = 'MK'
    country_dict_en['madagascar'] = 'MG'
    country_dict_en['malawi'] = 'MW'
    country_dict_en['malaysia'] = 'MY'
    country_dict_en['maldives'] = 'MV'
    country_dict_en['mali'] = 'ML'
    country_dict_en['malta'] = 'MT'
    country_dict_en['marshall islands'] = 'MH'
    country_dict_en['martinique'] = 'MQ'
    country_dict_en['mauritania'] = 'MR'
    country_dict_en['mauritius'] = 'MU'
    country_dict_en['mayotte'] = 'YT'
    country_dict_en['mexico'] = 'MX'
    country_dict_en['micronesia'] = 'FM'
    country_dict_en['moldova'] = 'MD'
    country_dict_en['monaco'] = 'MC'
    country_dict_en['mongolia'] = 'MN'
    country_dict_en['montenegro'] = 'ME'
    country_dict_en['montserrat'] = 'MS'
    country_dict_en['morocco'] = 'MA'
    country_dict_en['marocco'] = 'MA'
    country_dict_en['mozambique'] = 'MZ'
    country_dict_en['myanmar'] = 'MM'
    country_dict_en['namibia'] = 'NA'
    country_dict_en['nauru'] = 'NR'
    country_dict_en['nepal'] = 'NP'
    country_dict_en['netherlands'] = 'NL'
    country_dict_en['new caledonia'] = 'NC'
    country_dict_en['new zealand'] = 'NZ'
    country_dict_en['nicaragua'] = 'NI'
    country_dict_en['niger'] = 'NE'
    country_dict_en['nigeria'] = 'NG'
    country_dict_en['niue'] = 'NU'
    country_dict_en['norfolk island'] = 'NF'
    country_dict_en['northern mariana islands'] = 'MP'
    country_dict_en['norway'] = 'NO'
    country_dict_en['oman'] = 'OM'
    country_dict_en['pakistan'] = 'PK'
    country_dict_en['palau'] = 'PW'
    country_dict_en['palestinian territory, occupied'] = 'PS'
    country_dict_en['panama'] = 'PA'
    country_dict_en['papua new guinea'] = 'PG'
    country_dict_en['paraguay'] = 'PY'
    country_dict_en['peru'] = 'PE'
    country_dict_en['philippines'] = 'PH'
    country_dict_en['pitcairn'] = 'PN'
    country_dict_en['poland'] = 'PL'
    country_dict_en['portugal'] = 'PT'
    country_dict_en['puerto rico'] = 'PR'
    country_dict_en['qatar'] = 'QA'
    country_dict_en['reunion'] = 'RE'
    country_dict_en['romania'] = 'RO'
    country_dict_en['russian federation'] = 'RU'
    country_dict_en['rwanda'] = 'RW'
    country_dict_en['saint barthélemy'] = 'BL'
    country_dict_en['saint helena'] = 'SH'
    country_dict_en['saint kitts and nevis'] = 'KN'
    country_dict_en['saint lucia'] = 'LC'
    country_dict_en['saint martin'] = 'MF'
    country_dict_en['saint pierre and miquelon'] = 'PM'
    country_dict_en['saint vincent and the grenadines'] = 'VC'
    country_dict_en['samoa'] = 'WS'
    country_dict_en['san marino'] = 'SM'
    country_dict_en['sao tome and principe'] = 'ST'
    country_dict_en['saudi arabia'] = 'SA'
    country_dict_en['senegal'] = 'SN'
    country_dict_en['serbia'] = 'RS'
    country_dict_en['seychelles'] = 'SC'
    country_dict_en['sierra leone'] = 'SL'
    country_dict_en['singapore'] = 'SG'
    country_dict_en['sint maarten'] = 'SX'
    country_dict_en['slovakia'] = 'SK'
    country_dict_en['slovenia'] = 'SI'
    country_dict_en['solomon islands'] = 'SB'
    country_dict_en['somalia'] = 'SO'
    country_dict_en['south africa'] = 'ZA'
    country_dict_en['south georgia and the south sandwich islands'] = 'GS'
    country_dict_en['spain'] = 'ES'
    country_dict_en['sri lanka'] = 'LK'
    country_dict_en['sudan'] = 'SD'
    country_dict_en['suriname'] = 'SR'
    country_dict_en['svalbard and jan mayen'] = 'SJ'
    country_dict_en['swaziland'] = 'SZ'
    country_dict_en['sweden'] = 'SE'
    country_dict_en['switzerland'] = 'CH'
    country_dict_en['syrian arab republic'] = 'SY'
    country_dict_en['taiwan, province of china'] = 'TW'
    country_dict_en['tajikistan'] = 'TJ'
    country_dict_en['tanzania, united republic of'] = 'TZ'
    country_dict_en['thailand'] = 'TH'
    country_dict_en['timor-leste'] = 'TL'
    country_dict_en['togo'] = 'TG'
    country_dict_en['tokelau'] = 'TK'
    country_dict_en['tonga'] = 'TO'
    country_dict_en['trinidad and tobago'] = 'TT'
    country_dict_en['tunisia'] = 'TN'
    country_dict_en['turkey'] = 'TR'
    country_dict_en['turkmenistan'] = 'TM'
    country_dict_en['turks and caicos islands'] = 'TC'
    country_dict_en['tuvalu'] = 'TV'
    country_dict_en['uganda'] = 'UG'
    country_dict_en['ukraine'] = 'UA'
    country_dict_en['united arab emirates'] = 'AE'
    country_dict_en['united kingdom'] = 'GB'
    country_dict_en['united states'] = 'US'
    country_dict_en['united states minor outlying islands'] = 'UM'
    country_dict_en['uruguay'] = 'UY'
    country_dict_en['uzbekistan'] = 'UZ'
    country_dict_en['vanuatu'] = 'VU'
    country_dict_en['venezuela, bolivarian republic of'] = 'VE'
    country_dict_en['viet nam'] = 'VN'
    country_dict_en['virgin islands, british'] = 'VG'
    country_dict_en['virgin islands, u.s.'] = 'VI'
    country_dict_en['wallis and futuna'] = 'WF'
    country_dict_en['western sahara'] = 'EH'
    country_dict_en['yemen'] = 'YE'
    country_dict_en['zambia'] = 'ZM'
    country_dict_en['zimbabwe'] = 'ZW'
    if country:
        if lang == 'EN':
            country_dict = country_dict_en
        else:
            country_dict = country_dict_fr

        try:
            country = country.lower().strip().encode('ASCII', 'replace').replace('?', '.')
        except:
            country = country.lower().strip()
        for key,value in country_dict.items():
            if re.search(r"^%s" % country, key) or re.search(key, country):
                return value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
