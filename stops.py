line1Seq = ['Van Cortlandt Park - 242 St', '238 St', '231 St', 'Marble Hill - 225 St', '215 St', '207 St', 'Dyckman St', '191 St', '181 St', '168 St - Washington Hts', '157 St', '145 St', '137 St - City College', '125 St', '116 St - Columbia University', 'Cathedral Pkwy', '103 St', '96 St', '86 St', '79 St', '72 St', '66 St - Lincoln Center', '59 St - Columbus Circle', '50 St', 'Times Sq - 42 St', '34 St - Penn Station', '28 St', '23 St', '18 St', '14 St', 'Christopher St - Sheridan Sq', 'Houston St', 'Canal St', 'Franklin St', 'Chambers St', 'Cortlandt St', 'Rector St', 'South Ferry Loop']
line1 = {'135': 'Canal St', '134': 'Houston St', '115': '137 St - City College', '114': '145 St', '117': '116 St - Columbia University', '116': '125 St', '111': '181 St', '110': '191 St', '113': '157 St', '112': '168 St - Washington Hts', '139': 'Rector St', '138': 'Cortlandt St', '119': '103 St', '118': 'Cathedral Pkwy', '130': '23 St', '129': '28 St', '140': 'South Ferry Loop', '120': '96 St', '121': '86 St', '122': '79 St', '123': '72 St', '124': '66 St - Lincoln Center', '125': '59 St - Columbus Circle', '126': '50 St', '127': 'Times Sq - 42 St', '128': '34 St - Penn Station', '103': '238 St', '101': 'Van Cortlandt Park - 242 St', '106': 'Marble Hill - 225 St', '107': '215 St', '104': '231 St', '133': 'Christopher St - Sheridan Sq', '132': '14 St', '108': '207 St', '131': '18 St', '109': 'Dyckman St', '137': 'Chambers St', '136': 'Franklin St'}
line1Nbound = {'Christopher St - Sheridan Sq': '133N', '231 St': '104N', '238 St': '103N', '137 St - City College': '115N', 'Houston St': '134N', '96 St': '120N', 'Cathedral Pkwy': '118N', 'Franklin St': '136N', '18 St': '131N', '86 St': '121N', '207 St': '108N', 'Cortlandt St': '138N', '215 St': '107N', '125 St': '116N', '191 St': '110N', '14 St': '132N', '28 St': '129N', '103 St': '119N', 'Times Sq - 42 St': '127N', '72 St': '123N', '59 St - Columbus Circle': '125N', '23 St': '130N', '50 St': '126N', '66 St - Lincoln Center': '124N', 'Chambers St': '137N', '168 St - Washington Hts': '112N', '79 St': '122N', '34 St - Penn Station': '128N', 'Rector St': '139N', 'Canal St': '135N', 'Van Cortlandt Park - 242 St': '101N', '157 St': '113N', '145 St': '114N', 'South Ferry Loop': '140N', '116 St - Columbia University': '117N', 'Marble Hill - 225 St': '106N', '181 St': '111N', 'Dyckman St': '109N'}
line1Sbound = {'Christopher St - Sheridan Sq': '133S', '231 St': '104S', '238 St': '103S', '137 St - City College': '115S', 'Houston St': '134S', '96 St': '120S', 'Cathedral Pkwy': '118S', 'Franklin St': '136S', '18 St': '131S', '86 St': '121S', '207 St': '108S', 'Cortlandt St': '138S', '215 St': '107S', '125 St': '116S', '191 St': '110S', '14 St': '132S', '28 St': '129S', '103 St': '119S', 'Times Sq - 42 St': '127S', '72 St': '123S', '59 St - Columbus Circle': '125S', '23 St': '130S', '50 St': '126S', '66 St - Lincoln Center': '124S', 'Chambers St': '137S', '168 St - Washington Hts': '112S', '79 St': '122S', '34 St - Penn Station': '128S', 'Rector St': '139S', 'Canal St': '135S', 'Van Cortlandt Park - 242 St': '101S', '157 St': '113S', '145 St': '114S', 'South Ferry Loop': '140S', '116 St - Columbia University': '117S', 'Marble Hill - 225 St': '106S', '181 St': '111S', 'Dyckman St': '109S'}
line2Seq = ['Wakefield - 241 St', 'Nereid Av', '233 St', '225 St', '219 St', 'Gun Hill Rd', 'Burke Av', 'Allerton Av', 'Pelham Pkwy', 'Bronx Park East', 'E 180 St', 'West Farms Sq - E Tremont Av', '174 St', 'Freeman St', 'Simpson St', 'Intervale Av', 'Prospect Av', 'Jackson Av', '3 Av - 149 St', '149 St - Grand Concourse', '135 St', '125 St', '116 St', 'Central Park North (110 St)', 'Park Pl', 'Fulton St', 'Wall St', 'Clark St', 'Borough Hall', 'Hoyt St', 'Nevins St', 'Atlantic Av - Barclays Ctr', 'Bergen St', 'Grand Army Plaza', 'Eastern Pkwy - Brooklyn Museum', 'Franklin Av', 'President St', 'Sterling St', 'Winthrop St', 'Church Av', 'Beverly Rd', 'Newkirk Av', 'Flatbush Av - Brooklyn College', 'Nostrand Av', 'Kingston Av', 'Crown Hts - Utica Av', 'Sutter Av - Rutland Rd', 'Saratoga Av', 'Rockaway Av', 'Junius St', 'Pennsylvania Av', 'Van Siclen Av', 'New Lots Av']
line2 = {'216': 'Freeman St', '217': 'Simpson St', '214': 'West Farms Sq - E Tremont Av', '215': '174 St', '212': 'Bronx Park East', '213': 'E 180 St', '210': 'Allerton Av', '211': 'Pelham Pkwy', '242': 'Sterling St', '218': 'Intervale Av', '219': 'Prospect Av', '252': 'Saratoga Av', '238': 'Eastern Pkwy - Brooklyn Museum', '239': 'Franklin Av', '253': 'Rockaway Av', '234': 'Nevins St', '235': 'Atlantic Av - Barclays Ctr', '236': 'Bergen St', '237': 'Grand Army Plaza', '230': 'Wall St', '231': 'Clark St', '232': 'Borough Hall', '233': 'Hoyt St', '251': 'Sutter Av - Rutland Rd', '256': 'Van Siclen Av', '248': 'Nostrand Av', '243': 'Winthrop St', '254': 'Junius St', '250': 'Crown Hts - Utica Av', '255': 'Pennsylvania Av', '201': 'Wakefield - 241 St', '205': '233 St', '204': 'Nereid Av', '207': '219 St', '206': '225 St', '209': 'Burke Av', '208': 'Gun Hill Rd', '245': 'Beverly Rd', '244': 'Church Av', '247': 'Flatbush Av - Brooklyn College', '246': 'Newkirk Av', '241': 'President St', '229': 'Fulton St', '228': 'Park Pl', '227': 'Central Park North (110 St)', '226': '116 St', '225': '125 St', '224': '135 St', '249': 'Kingston Av', '222': '149 St - Grand Concourse', '221': '3 Av - 149 St', '220': 'Jackson Av', '257': 'New Lots Av'}
line2Nbound = {'225N': '125 St', '237N': 'Grand Army Plaza', '216N': 'Freeman St', '235N': 'Atlantic Av - Barclays Ctr', '210N': 'Allerton Av', '206N': '225 St', '250N': 'Crown Hts - Utica Av', '239N': 'Franklin Av', '214N': 'West Farms Sq - E Tremont Av', '256N': 'Van Siclen Av', '251N': 'Sutter Av - Rutland Rd', '241N': 'President St', '231N': 'Clark St', '208N': 'Gun Hill Rd', '249N': 'Kingston Av', '204N': 'Nereid Av', '253N': 'Rockaway Av', '227N': 'Central Park North (110 St)', '221N': '3 Av - 149 St', '233N': 'Hoyt St', '212N': 'Bronx Park East', '252N': 'Saratoga Av', '218N': 'Intervale Av', '254N': 'Junius St', '255N': 'Pennsylvania Av', '228N': 'Park Pl', '246N': 'Newkirk Av', '244N': 'Church Av', '243N': 'Winthrop St', '236N': 'Bergen St', '224N': '135 St', '201N': 'Wakefield - 241 St', '226N': '116 St', '207N': '219 St', '211N': 'Pelham Pkwy', '215N': '174 St', '217N': 'Simpson St', '238N': 'Eastern Pkwy - Brooklyn Museum', '222N': '149 St - Grand Concourse', '230N': 'Wall St', '213N': 'E 180 St', '242N': 'Sterling St', '234N': 'Nevins St', '232N': 'Borough Hall', '220N': 'Jackson Av', '205N': '233 St', '248N': 'Nostrand Av', '209N': 'Burke Av', '219N': 'Prospect Av', '245N': 'Beverly Rd', '229N': 'Fulton St', '247N': 'Flatbush Av - Brooklyn College', '257N': 'New Lots Av'}
line2Sbound = {'221S': '3 Av - 149 St', '254S': 'Junius St', '212S': 'Bronx Park East', '233S': 'Hoyt St', '204S': 'Nereid Av', '227S': 'Central Park North (110 St)', '208S': 'Gun Hill Rd', '249S': 'Kingston Av', '231S': 'Clark St', '241S': 'President St', '255S': 'Pennsylvania Av', '214S': 'West Farms Sq - E Tremont Av', '239S': 'Franklin Av', '253S': 'Rockaway Av', '210S': 'Allerton Av', '235S': 'Atlantic Av - Barclays Ctr', '206S': '225 St', '225S': '125 St', '216S': 'Freeman St', '237S': 'Grand Army Plaza', '257S': 'New Lots Av', '244S': 'Church Av', '252S': 'Saratoga Av', '246S': 'Newkirk Av', '250S': 'Crown Hts - Utica Av', '228S': 'Park Pl', '218S': 'Intervale Av', '242S': 'Sterling St', '251S': 'Sutter Av - Rutland Rd', '256S': 'Van Siclen Av', '232S': 'Borough Hall', '205S': '233 St', '220S': 'Jackson Av', '213S': 'E 180 St', '234S': 'Nevins St', '230S': 'Wall St', '222S': '149 St - Grand Concourse', '248S': 'Nostrand Av', '217S': 'Simpson St', '238S': 'Eastern Pkwy - Brooklyn Museum', '215S': '174 St', '207S': '219 St', '226S': '116 St', '211S': 'Pelham Pkwy', '236S': 'Bergen St', '201S': 'Wakefield - 241 St', '224S': '135 St', '247S': 'Flatbush Av - Brooklyn College', '229S': 'Fulton St', '245S': 'Beverly Rd', '243S': 'Winthrop St', '219S': 'Prospect Av', '209S': 'Burke Av'}
line3Seq = ['Harlem - 148 St', '145 St']
line3 = {'301': 'Harlem - 148 St', '302': '145 St'}
line3Nbound = {'302N': '145 St', '301N': 'Harlem - 148 St'}
line3Sbound = {'301S': 'Harlem - 148 St', '302S': '145 St'}
line4Seq = ['Woodlawn', 'Mosholu Pkwy', 'Bedford Park Blvd - Lehman College', 'Kingsbridge Rd', 'Fordham Rd', '183 St', 'Burnside Av', '176 St', 'Mt Eden Av', '170 St', '167 St', '161 St - Yankee Stadium', '149 St - Grand Concourse', '138 St - Grand Concourse', 'Fulton St', 'Wall St', 'Bowling Green', 'Borough Hall']
line4 = {'414': '161 St - Yankee Stadium', '411': 'Mt Eden Av', '415': '149 St - Grand Concourse', '416': '138 St - Grand Concourse', '419': 'Wall St', '407': 'Fordham Rd', '406': 'Kingsbridge Rd', '405': 'Bedford Park Blvd - Lehman College', '410': '176 St', '402': 'Mosholu Pkwy', '401': 'Woodlawn', '413': '167 St', '420': 'Bowling Green', '423': 'Borough Hall', '418': 'Fulton St', '412': '170 St', '409': 'Burnside Av', '408': '183 St'}
line4Nbound = {'423N': 'Borough Hall', '414N': '161 St - Yankee Stadium', '420N': 'Bowling Green', '402N': 'Mosholu Pkwy', '415N': '149 St - Grand Concourse', '418N': 'Fulton St', '410N': '176 St', '419N': 'Wall St', '411N': 'Mt Eden Av', '407N': 'Fordham Rd', '401N': 'Woodlawn', '413N': '167 St', '416N': '138 St - Grand Concourse', '405N': 'Bedford Park Blvd - Lehman College', '406N': 'Kingsbridge Rd', '409N': 'Burnside Av', '408N': '183 St', '412N': '170 St'}
line4Sbound = {'409S': 'Burnside Av', '406S': 'Kingsbridge Rd', '408S': '183 St', '405S': 'Bedford Park Blvd - Lehman College', '415S': '149 St - Grand Concourse', '401S': 'Woodlawn', '418S': 'Fulton St', '413S': '167 St', '414S': '161 St - Yankee Stadium', '419S': 'Wall St', '407S': 'Fordham Rd', '412S': '170 St', '410S': '176 St', '402S': 'Mosholu Pkwy', '420S': 'Bowling Green', '416S': '138 St - Grand Concourse', '423S': 'Borough Hall', '411S': 'Mt Eden Av'}
line5Seq = ['Eastchester - Dyre Av', 'Baychester Av', 'Gun Hill Rd', 'Pelham Pkwy', 'Morris Park']
line5 = {'504': 'Pelham Pkwy', '505': 'Morris Park', '502': 'Baychester Av', '503': 'Gun Hill Rd', '501': 'Eastchester - Dyre Av'}
line5Nbound = {'503N': 'Gun Hill Rd', '504N': 'Pelham Pkwy', '505N': 'Morris Park', '501N': 'Eastchester - Dyre Av', '502N': 'Baychester Av'}
line5Sbound = {'502S': 'Baychester Av', '501S': 'Eastchester - Dyre Av', '504S': 'Pelham Pkwy', '503S': 'Gun Hill Rd', '505S': 'Morris Park'}
line6Seq = ['Pelham Bay Park', 'Buhre Av', 'Middletown Rd', 'Westchester Sq - E Tremont Av', 'Zerega Av', 'Castle Hill Av', 'Parkchester', 'St Lawrence Av', 'Morrison Av- Sound View', 'Elder Av', 'Whitlock Av', 'Hunts Point Av', 'Longwood Av', 'E 149 St', "E 143 St - St Mary's St", 'Cypress Av', 'Brook Av', '3 Av - 138 St', '125 St', '116 St', '110 St', '103 St', '96 St', '86 St', '77 St', '68 St - Hunter College', '59 St', '51 St', 'Grand Central - 42 St', '33 St', '28 St', '23 St', '14 St - Union Sq', 'Astor Pl', 'Bleecker St', 'Spring St', 'Canal St', 'Brooklyn Bridge - City Hall']
line6 = {'623': '110 St', '604': 'Westchester Sq - E Tremont Av', '607': 'Castle Hill Av', '606': 'Zerega Av', '601': 'Pelham Bay Park', '626': '86 St', '603': 'Middletown Rd', '602': 'Buhre Av', '629': '59 St', '628': '68 St - Hunter College', '609': 'St Lawrence Av', '608': 'Parkchester', '633': '28 St', '627': '77 St', '621': '125 St', '625': '96 St', '624': '103 St', '632': '33 St', '638': 'Spring St', '639': 'Canal St', '630': '51 St', '631': 'Grand Central - 42 St', '618': 'Brook Av', '619': '3 Av - 138 St', '634': '23 St', '635': '14 St - Union Sq', '636': 'Astor Pl', '637': 'Bleecker St', '612': 'Whitlock Av', '613': 'Hunts Point Av', '610': 'Morrison Av- Sound View', '611': 'Elder Av', '616': "E 143 St - St Mary's St", '617': 'Cypress Av', '614': 'Longwood Av', '615': 'E 149 St', '640': 'Brooklyn Bridge - City Hall', '622': '116 St'}
line6Nbound = {'623N': '110 St', '603N': 'Middletown Rd', '637N': 'Bleecker St', '607N': 'Castle Hill Av', '619N': '3 Av - 138 St', '631N': 'Grand Central - 42 St', '629N': '59 St', '611N': 'Elder Av', '613N': 'Hunts Point Av', '638N': 'Spring St', '635N': '14 St - Union Sq', '622N': '116 St', '601N': 'Pelham Bay Park', '617N': 'Cypress Av', '624N': '103 St', '609N': 'St Lawrence Av', '640N': 'Brooklyn Bridge - City Hall', '615N': 'E 149 St', '621N': '125 St', '627N': '77 St', '633N': '28 St', '630N': '51 St', '636N': 'Astor Pl', '602N': 'Buhre Av', '618N': 'Brook Av', '606N': 'Zerega Av', '604N': 'Westchester Sq - E Tremont Av', '610N': 'Morrison Av- Sound View', '628N': '68 St - Hunter College', '626N': '86 St', '634N': '23 St', '608N': 'Parkchester', '632N': '33 St', '616N': "E 143 St - St Mary's St", '612N': 'Whitlock Av', '614N': 'Longwood Av', '639N': 'Canal St', '625N': '96 St'}
line6Sbound = {'640S': 'Brooklyn Bridge - City Hall', '601S': 'Pelham Bay Park', '635S': '14 St - Union Sq', '613S': 'Hunts Point Av', '633S': '28 St', '629S': '59 St', '627S': '77 St', '611S': 'Elder Av', '625S': '96 St', '621S': '125 St', '619S': '3 Av - 138 St', '603S': 'Middletown Rd', '637S': 'Bleecker St', '623S': '110 St', '624S': '103 St', '632S': '33 St', '615S': 'E 149 St', '639S': 'Canal St', '609S': 'St Lawrence Av', '617S': 'Cypress Av', '634S': '23 St', '626S': '86 St', '610S': 'Morrison Av- Sound View', '628S': '68 St - Hunter College', '622S': '116 St', '618S': 'Brook Av', '606S': 'Zerega Av', '636S': 'Astor Pl', '602S': 'Buhre Av', '630S': '51 St', '638S': 'Spring St', '631S': 'Grand Central - 42 St', '604S': 'Westchester Sq - E Tremont Av', '614S': 'Longwood Av', '612S': 'Whitlock Av', '607S': 'Castle Hill Av', '616S': "E 143 St - St Mary's St", '608S': 'Parkchester'}
lineLSeq = ['8 Av', '6 Av', 'Union Sq - 14 St', '3 Av', '1 Av', 'Bedford Av', 'Lorimer St', 'Graham Av', 'Grand St', 'Montrose Av', 'Morgan Av', 'Jefferson St', 'DeKalb Av', 'Myrtle - Wyckoff Avs', 'Halsey St', 'Wilson Av', 'Bushwick Av - Aberdeen St', 'Broadway Jct', 'Atlantic Av', 'Sutter Av', 'Livonia Av', 'New Lots Av', 'E 105 St', 'Canarsie - Rockaway Pkwy']
lineL = {'L19': 'Halsey St', 'L14': 'Morgan Av', 'L15': 'Jefferson St', 'L16': 'DeKalb Av', 'L17': 'Myrtle - Wyckoff Avs', 'L10': 'Lorimer St', 'L11': 'Graham Av', 'L12': 'Grand St', 'L13': 'Montrose Av', 'L21': 'Bushwick Av - Aberdeen St', 'L20': 'Wilson Av', 'L22': 'Broadway Jct', 'L25': 'Sutter Av', 'L24': 'Atlantic Av', 'L27': 'New Lots Av', 'L26': 'Livonia Av', 'L29': 'Canarsie - Rockaway Pkwy', 'L28': 'E 105 St', 'L08': 'Bedford Av', 'L06': '1 Av', 'L05': '3 Av', 'L03': 'Union Sq - 14 St', 'L02': '6 Av', 'L01': '8 Av'}
lineLNbound = {'L08N': 'Bedford Av', 'L16N': 'DeKalb Av', 'L21N': 'Bushwick Av - Aberdeen St', 'L06N': '1 Av', 'L27N': 'New Lots Av', 'L02N': '6 Av', 'L10N': 'Lorimer St', 'L14N': 'Morgan Av', 'L12N': 'Grand St', 'L25N': 'Sutter Av', 'L29N': 'Canarsie - Rockaway Pkwy', 'L05N': '3 Av', 'L17N': 'Myrtle - Wyckoff Avs', 'L15N': 'Jefferson St', 'L26N': 'Livonia Av', 'L19N': 'Halsey St', 'L22N': 'Broadway Jct', 'L20N': 'Wilson Av', 'L11N': 'Graham Av', 'L28N': 'E 105 St', 'L03N': 'Union Sq - 14 St', 'L24N': 'Atlantic Av', 'L01N': '8 Av', 'L13N': 'Montrose Av'}
lineLSbound = {'L27S': 'New Lots Av', 'L06S': '1 Av', 'L16S': 'DeKalb Av', 'L21S': 'Bushwick Av - Aberdeen St', 'L08S': 'Bedford Av', 'L29S': 'Canarsie - Rockaway Pkwy', 'L12S': 'Grand St', 'L25S': 'Sutter Av', 'L14S': 'Morgan Av', 'L10S': 'Lorimer St', 'L02S': '6 Av', 'L20S': 'Wilson Av', 'L19S': 'Halsey St', 'L22S': 'Broadway Jct', 'L15S': 'Jefferson St', 'L26S': 'Livonia Av', 'L05S': '3 Av', 'L17S': 'Myrtle - Wyckoff Avs', 'L01S': '8 Av', 'L13S': 'Montrose Av', 'L24S': 'Atlantic Av', 'L28S': 'E 105 St', 'L03S': 'Union Sq - 14 St', 'L11S': 'Graham Av'}