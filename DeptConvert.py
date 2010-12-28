
def departement(value):
	"""
	Convert code dept

	>>> departement('121')
	False

	>>> departement('2A')
	'corse-du-sud'

	>>> departement("cotes d\'armr")
	False

	>>> departement("cotes d\'armor")
	'22'

	"""
	cp= dict()
	cp['01']='ain'
	cp['02']='aisne'
	cp['03']='allier'
	cp['04']='alpes-de-hautes-provence'
	cp['05']='hautes-alpes'
	cp['06']='alpes-maritimes'
	cp['07']='ardeche'
	cp['08']='ardennes'
	cp['09']='ariege'
	cp['10']='aube'
	cp['11']='aude'
	cp['12']='aveyron'
	cp['13']='bouches-du-rhone'
	cp['14']='calvados'
	cp['15']='cantal'
	cp['16']='charente'
	cp['17']='charente-maritime'
	cp['18']='cher'
	cp['19']='correze'
	cp['2A']='corse-du-sud'
	cp['2B']='haute-corse'  
	cp['21']='cote-d\'or'  
	cp['22']='cotes-d\'armor'
	cp['23']='creuse'
	cp['24']='dordogne'
	cp['25']='doubs'
	cp['26']='drome'
	cp['27']='eure'
	cp['28']='eure-et-loir'
	cp['29']='finistere'
	cp['30']='gard'
	cp['31']='haute-garonne'
	cp['32']='gers'
	cp['33']='gironde'
	cp['34']='herault'
	cp['35']='ille-et-vilaine'
	cp['36']='indre'
	cp['37']='indre-et-loire'
	cp['38']='isere'
	cp['39']='jura'
	cp['40']='landes'
	cp['41']='loir-et-cher'
	cp['42']='loire'
	cp['43']='haute-loire'
	cp['44']='loire-atlantique'
	cp['45']='loiret'
	cp['46']='lot'
	cp['47']='lot-et-garonne'
	cp['48']='lozere'
	cp['49']='maine-et-loire'
	cp['50']='manche'
	cp['51']='marne'
	cp['52']='haute-marne'
	cp['53']='mayenne'
	cp['54']='meurthe-et-moselle'
	cp['55']='meuse'
	cp['56']='morbihan'
	cp['57']='moselle'
	cp['58']='nievre'
	cp['59']='nord'
	cp['60']='oise'
	cp['61']='orne'
	cp['62']='pas-de-calais'
	cp['63']='puy-de-dome'
	cp['64']='pyrenees-atlantique'
	cp['65']='hautes-pyrenees'
	cp['66']='pyrenees-orientales'
	cp['67']='bas-rhin'
	cp['68']='haut-rhin'
	cp['69']='rhone'
	cp['70']='haute-saone'
	cp['71']='saone-et-loire'
	cp['72']='sarthe'
	cp['73']='savoie'
	cp['74']='haute-savoie'
	cp['75']='paris'
	cp['76']='seine-maritime'
	cp['77']='seine-et-marne'
	cp['78']='yvelines'
	cp['79']='deux-sevres'
	cp['80']='somme'
	cp['81']='tarn'
	cp['82']='tarn-et-garonne'
	cp['83']='var'
	cp['84']='vaucluse'
	cp['85']='vendee'
	cp['86']='vienne'
	cp['87']='haute-vienne'
	cp['88']='vosges'
	cp['89']='yonne'
	cp['90']='territoire-de-belfort'
	cp['91']='essonne'
	cp['92']='haut-de-seine'
	cp['93']='sein-saint-denis'
	cp['94']='val-de-marne'
	cp['95']='val-d\'oise'
        nom_dep=value.replace(" ","-").lower()
	if value in cp.keys():
	    return cp[value]
        else:            
            if nom_dep in cp.values():
                for key,value in cp.items():
                    if value==nom_dep:
                        return key
            else:
                return False
