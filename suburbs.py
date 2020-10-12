header = ['Date', 'Product','Price', 'Brand', 'Address', 'Suburb']

#*****************************************
#*****************************************
product = {'1' : 'Unleaded Petrol', '2' : 'Premium Unleaded', '4': 'Diesel', '5' : 'LPG', '6': '98 RON', '10': 'E85', '11': 'Brand diesel'}
#*****************************************
#*****************************************
suburbs = ['<Suburb>','Albany', 'Alexander Heights', 'Alfred Cove', 'Alkimos', 'Applecross', 'Armadale', 'Ascot', 'Ashby', 'Attadale', 
'Augusta', 'Australind', 'Aveley', 'Balcatta', 'Baldivis', 'Balga', 'Balingup', 'Ballajura', 'Banksia Grove', 'Barragup', 
'Baskerville', 'Bassendean', 'Bayswater', 'Beckenham', 'Bedfordale', 'Beechboro', 'Beeliar', 'Beldon', 'Bellevue', 'Belmont', 
'Bentley', 'Bertram', 'Bibra Lake', 'Bicton', 'Binningup', 'Boulder', 'Boyanup', 'Brentwood', 'Bridgetown', 'Broadwater', 'Broome',
 'Brunswick', 'Bull Creek', 'Bullsbrook', 'Bunbury', 'Burswood', 'Busselton', 'Butler', 'Byford', 'Canning Vale', 'Cannington', 
 'Capel', 'Carbunup River', 'Carine', 'Carlisle', 'Carnarvon', 'Cataby', 'Caversham', 'Chidlow', 'Claremont', 'Clarkson', 
 'Cloverdale', 'Cockburn Central', 'Collie', 'Como', 'Coolgardie', 'Coolup', 'Cowaramup', 'Cunderdin', 'Currambine', 'Dalwallinu', 
 'Dampier', 'Dardanup', 'Dawesville', 'Dayton', 'Denmark', 'Derby', 'Dianella', 'Dongara', 'Donnybrook', 'Doubleview', 'Duncraig', 
 'Dunsborough', 'Dwellingup', 'East Fremantle', 'East Perth', 'East Rockingham', 'East Victoria Park', 'Eaton', 'Edgewater', 
 'Ellenbrook', 'Embleton', 'Erskine', 'Esperance', 'Exmouth', 'Falcon', 'Fitzroy Crossing', 'Floreat', 'Forrestdale', 
 'Forrestfield', 'Fremantle', 'Gelorup', 'Geraldton', 'Gidgegannup', 'Girrawheen', 'Glen Forrest', 'Glen Iris', 'Glendalough', 
 'Glenfield', 'Gnangara', 'Gosnells', 'Gracetown', 'Greenbushes', 'Greenfields', 'Greenough', 'Greenwood', 'Guildford', 'Gwelup', 
 'Halls Head', 'Hamilton Hill', 'Harrisdale', 'Harvey', 'Henderson', 'Henley Brook', 'Herne Hill', 'High Wycombe', 'Hillarys', 
 'Huntingdale', 'Innaloo', 'Jandakot', 'Jarrahdale', 'Jindalee', 'Jolimont', 'Joondalup', 'Jurien Bay', 'Kalamunda', 'Kalgoorlie', 
 'Kambalda East', 'Karawara', 'Kardinya', 'Karnup', 'Karragullen', 'Karratha', 'Karridale', 'Karrinyup', 'Kellerberrin', 
 'Kelmscott', 'Kewdale', 'Kiara', 'Kingsley', 'Kojonup', 'Koondoola', 'Kununurra', 'Kwinana Beach', 'Kwinana Town Centre', 
 'Lakelands', 'Landsdale', 'Langford', 'Leda', 'Leederville', 'Leeming', 'Lesmurdie', 'Lexia', 'Lynwood', 'Maddington', 'Madeley',
 'Maida Vale', 'Malaga', 'Mandurah', 'Manjimup', 'Manning', 'Manypeaks', 'Margaret River', 'Meadow Springs', 'Meckering',
 'Meekatharra', 'Merriwa', 'Middle Swan', 'Midvale', 'Mindarie', 'Mirrabooka', 'Moonyoonooka', 'Moora', 'Morley', 'Mosman Park', 
 'Mount Barker', 'Mt Helena', 'Mt Lawley', 'Mt Pleasant', 'Mullaloo', 'Mullewa', 'Mundaring', 'Mundijong', 'Munglinup', 'Munster', 
 'Murdoch', 'Myalup', 'Myaree', 'Narngulu', 'Narrogin', 'Naval Base', 'Nedlands', 'Neerabup', 'Newman', 'Nollamara', 'Noranda', 'Norseman', 
 'North Bannister', 'North Dandalup', 'North Fremantle', 'North Perth', 'North Yunderup', 'Northam', 'Northbridge', 'Northcliffe', 'Nowergup',
 'O Connor', 'Ocean Reef', 'Osborne Park', 'Padbury', 'Palmyra', 'Pearsall', 'Pemberton', 'Perth', 'Picton', 'Picton East', 'Pinjarra', 
 'Port Hedland', 'Port Kennedy', 'Preston Beach', 'Queens Park', 'Quinns Rocks', 'Ravensthorpe', 'Ravenswood', 'Redcliffe', 'Regans Ford', 
 'Ridgewood', 'Riverton', 'Rivervale', 'Rockingham', 'Roleystone', 'Rosa Brook', 'Safety Bay', 'Sawyers Valley', 'Scarborough', 
 'Secret Harbour', 'Serpentine', 'Seville Grove', 'Siesta Park', 'Singleton', 'Sorrento', 'South Fremantle', 'South Hedland', 'South Lake', 
 'South Perth', 'South Yunderup', 'Southern River', 'Spearwood', 'Stratham', 'Stratton', 'Subiaco', 'Success', 'Swan View', 'Swanbourne',
 'Tammin', 'The Lakes', 'Thornlie', 'Tuart Hill', 'Upper Swan', 'Vasse', 'Victoria Park', 'Waikiki', 'Walkaway', 'Walpole', 'Wangara', 
 'Wanneroo', 'Warnbro', 'Waroona', 'Warwick', 'Waterloo', 'Wattle Grove', 'Wedgefield', 'Wellstead', 'Welshpool', 'Wembley', 'West Busselton',
 'West Kalgoorlie', 'West Perth', 'West Pinjarra', 'West Swan', 'Westminster', 'Willetton', 'Williams', 'Witchcliffe', 'Woodbridge', 
 'Woodvale', 'Wubin', 'Wundowie', 'Yanchep', 'Yangebup', 'Yokine', 'York', 'Youngs Siding']