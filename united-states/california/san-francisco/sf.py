"""
Breaks are defined as intersections where there should be
no path connecting that intersection with the next one.

Breaks always go from west -> east, or south -> north.

For example: there is a break on 2nd Ave at Lincoln Way, since
you can't get to 2nd Ave @ Fulton (the next intersection)
without taking a turn. Lincoln is the south intersection, hence,
south -> north.



Each region is a list of buckets.
Each bucket contains a set of paths.
For a region, the paths in one bucket are all parallel and never intersect.
"""

city = 'San Francisco, CA'

regions = [
    # NOPA
    [
        [
            'Geary Blvd', "O'Farrell St", "Turk St", "Turk Blvd",
            'Ellis St', 'Eddy St',
            'Golden Gate Ave', 'McAllister St', 'Fulton St',
            'Grove St', 'Hayes St', 'Fell St', 'Oak St',
            'Page St', 'Haight St', 'Waller St',
        ],
        [
            'Van Ness Ave', 'Franklin St', 'Gough St',
            'Octavia Blvd', 'Octavia St', 'Laguna St', 'Buchanan St',
            'Webster St', 'Fillmore St', 'Steiner St', 'Pierce St', 'Scott St',
            # Div -> Masonic
            'Divisadero St', "Broderick St", 'Baker St', 'Lyon St', 'Central Ave', 'Masonic Ave',
            # Masonic -> Stanyan
            'Ashbury St', 'Clayton St', 'Belvedere St', 'Parker Ave', 'Cole St', 'Shrader St', 'Stanyan St',
        ],
    ],
    # Richmond/Sunset
    [
        # west -> east streets
        [
            'Lake St', 'California St', 'Clement St', 'Geary Blvd',
            'Anza St', 'Balboa St', 'Cabrillo St', 'Fulton St',
            'Lincoln Way', 'Frederick St', 'Hugo St',
            'Irving St', 'Judah St',
            'Kirkham St', 'Lawton St', 'Moraga St',
            'Noriega St', 'Ortega St', 'Pacheco St',
            'Quintara St', 'Rivera St', 'Santiago St',
            'Taraval St', 'Ulloa St',
        ],

        # south -> north streets
        [
            # the aves ( no 13th )
            '2nd Ave', '3rd Ave', '4th Ave', '5th Ave', '6th Ave', '7th Ave', '8th Ave', '9th Ave', '10th Ave', '11th Ave', '12th Ave', '14th Ave', '15th Ave', '16th Ave', '17th Ave', '18th Ave', '19th Ave', '20th Ave', '21st Ave', '22nd Ave', '23rd Ave', '24th Ave', '25th Ave', '26th Ave', '27th Ave', '28th Ave', '29th Ave', '30th Ave', '31st Ave', '32nd Ave', '33rd Ave', '34th Ave', '35th Ave', '36th Ave', '37th Ave', '38th Ave', '39th Ave', '40th Ave', '41st Ave', '42nd Ave', '43rd Ave', '44th Ave', '45th Ave', '46th Ave', '47th Ave', '48th Ave',
            # other streets
            'Arguello Blvd', 'Sunset Blvd', 'Funston Ave', 'Park Presidio Blvd', 'Willard St',
        ],
    ],

    # Marina / Pac Hgts / Fillmore / Nob Hill / North Beach / TL
    [
        # west -> east streets
        [
            'Oak St', 'Fell St', 'Hayes St', 'Grove St',
            'McAllister St', 'Golden Gate Ave', 'Turk St',
            'Eddy St', 'Ellis St', "O'Farrell St", 'Geary St',
            'Post St', 'Sutter St', 'Bush St', 'Pine St',
            'California St', 'Sacramento St', 'Clay St',
            'Washington St', 'Jackson St', 'Pacific Ave',
            'Broadway St', 'Vallejo St', 'Green St',
            'Union St', 'Filbert St', 'Greenwich St',
            'Lombard St', 'Chestnut St', 'Francisco St',
            'Bay St', 'North Point St', 'Beach St',
        ],

        # south -> north streets
        [
            'Lyon St', 'Baker St', 'Broderick St', 'Divisadero St',
            'Scott St', 'Pierce St', 'Steiner St', 'Fillmore St',
            'Webster St', 'Buchanan St', 'Laguna St', 'Octavia Blvd', 'Octavia St',
            'Gough St', 'Franklin St', 'Van Ness Ave',
            'Polk St', 'Larkin St', 'Hyde St', 'Leavenworth St',
            'Jones St', 'Taylor St', 'Mason St',
            'Powell St', 'Stockton St', 'Grant Ave',
            'Montgomery St', 'Sansome St',
            'Battery St', 'Front St', 'Davis St', 'Drumm St',
        ],
        # weirdo diagonal streets
        [
            'Columbus Ave', 'The Embarcadero', 'Market St'
        ]
    ],

    # Holly Park Circle
    [
        [
            'Holly Park Cir'
        ],
        [
            'Highland Ave', 'Park St', 'Murray St',
            'Appleton Ave', 'Elsie St', 'Bocana St',
        ]
    ],

    # Laurel Heights
    [
        # west -> east streets
        [
            'Pacific Ave', 'Jackson St', 'Washington St',
            'Clay St', 'Sacramento St', 'California St',
            'Mayfair Dr', 'Euclid Ave', 'Geary Blvd',
            'Anza St', 'Terra Vista Ave', 'Edward St',
            'Anza Vista Ave', 'McAllister St', 'Golden Gate Ave',
        ],

        [
            'Arguello Blvd', 'Cherry St', 'Maple St', 'Spruce St',
            'Locust St', 'Laurel St', 'Walnut St', 'Presidio Ave',
            'Palm Ave', 'Jordan Ave', 'Commonwealth Ave', 'Parker Ave',
            'Collins St', 'Stanyan St',
            'Wood St', 'Beaumont Ave', 'Willard N',
            'Baker St', "St Joseph's Ave"
        ],

    ],

    # I need to bike home from Crocker Amazon, fuuu
    [
        # west->east streets
        [
            'Geneva Ave', 'Amazon Ave', 'Italy Ave', 'France Ave',
            'Russia Ave', 'Persia Ave', 'Brazil Ave', 'Excelsior Ave',
            'Avalon Ave', 'Silver Ave', 'Maynard St', 'Ney St',
            'Trumbull St', 'Alemany Blvd', 'Bosworth St', 'Crescent Ave',
            'Richland Ave', 'Park St', 'Highland Ave', 'Appleton Ave',
            'Randall St', '30th St', 'Day St',
            '29th St', '28th St', '27th St', '26th St', '25th St', '24th St',
            '23rd St', '22nd St', '21st St', '20th St', '19th St', '18th St',
            '17th St', '16th St',
        ],

        # mission st, lol
        [
            'Mission St', 'Dolores St'
        ],
    ],

    # Ashbury Heights / Duboce Triangle / Frederick Knob

    [
        # west->east streets
        [
            'Beulah St', 'Frederick St', 'Carl St', 'Parnassus Ave',
            'Grattan St', 'Alma St', 'Rivoli St',
            'Duboce Ave', 'Hermann St', 'Germania St', 'Henry St',
            '14th St', '15th St', '16th St', '17th St'
        ],

        # north->south streets
        [
            '4th Ave', '3rd Ave', 'Hillway Ave', 'Willard St', 'Arguello Blvd',
            'Stanyan St', 'Shrader St', 'Cole St', 'Belvedere St', 'Clayton St',
            'Downey St', 'Ashbury St', 'Delmar St', 'Masonic Ave',
            'Divisadero St', 'Castro St', 'Scott St', 'Noe St', 'Steiner St',
            'Sanchez St', 'Fillmore St', 'Church St', 'Webster St', 'Buchanan St',
            'Laguna St'
        ],
        ['Market St'],
    ],

    # SOMA
    [
        # northwest->southeast streets
        [
            'Spear St', 'Main St', 'Beale St', 'Fremont St',
            '1st St', '2nd St', 'New Montgomery St', '3rd St',
            '4th St', '5th St', '6th St', '7th St', '8th St',
            '9th St', '10th St', '11th St', '12th St'
        ],

        # northeast->southwest streets
        [
            'Market St', 'Mission St', 'Howard St',
            'Folsom St', 'Harrison St', 'Bryant St', 'Brannan St',
            'Townsend St', 'King St'
        ],

        ['Van Ness Ave'],

    ],

    # The Mission
    [
        # west->east streets
        [
            'Duboce Ave', 'Division St', '14th St', 'Alameda St',
            '15th St', '16th St', '17th St', '18th St', 'Mariposa St',
            '19th St', '20th St', '21st St', '22nd St', '23rd St', '24th St',
            '25th St', '26th St', 'Cesar Chavez St', '27th St', '28th St',
            'Clipper St', 'Elizabeth St', '29th St', 'Day St', '30th St',
        ],

        # north->south streets
        [
            'Douglass St', 'Diamond St', 'Collingwood St', 'Castro St',
            'Noe St', 'Sanchez St', 'Church St', 'Dolores St', 'Guerrero St',
            'Valencia St', 'Mission St', 'Capp St', 'Van Ness Ave', 'Shotwell St',
            'Folsom St', 'Harrison St', 'Alabama St', 'Florida St', 'Bryant St',
            'York St', 'Hampshire St', 'Potrero Ave', 'Utah St', 'Vermont St',
            'Kansas St', 'Rhode Island St', 'De Haro St', 'Carolina St',
            'Arkansas St', 'Connecticut St', 'Missouri St', 'Mississippi St',
            'Pennsylvania Ave', 'Indiana St', 'Minnesota St', 'Tennessee St',
            '3rd St', 'Illinois St'
        ],

    ],

]

breaks = {

    ##################
    # west -> east streets
    # BREAKS ON WEST SIDE
    ##################
    'Golden Gate Ave': set(['Stanyan St']),
    'McAllister St': set(['Parker Ave']),
    'Grove St': set(['Scott St']),
    'Waller St': set(['Central Ave']),

    'Anza St': set(['32nd Ave']),

    'Pacheco St': set(['41st Ave']),
    'Quintara St': set(['39th Ave']),


    ##############################
    # south -> north streets
    # BREAKS ON SOUTH SIDE
    ##############################


    'Pierce St': set(['Hayes St']),
    'Lyon St': set(['Turk Blvd', 'Oak St']),
    'Central Ave': set(['Oak St']),
    'Ashbury St': set(['Oak St']),
    'Clayton St': set(['Oak St']),
    'Cole St': set(['Oak St']),
    'Shrader St': set(['Oak St']),


    # The Aves (and arguello/funston, lol)
    'Arguello Blvd': set(['Frederick St']),
    '2nd Ave': set(['Lincoln Way']),
    '3rd Ave': set(['Lincoln Way']),
    '4th Ave': set(['Kirkham St', 'Lincoln Way']),
    '5th Ave': set(['Lincoln Way']),
    '6th Ave': set(['Lincoln Way']),
    '7th Ave': set(['Lincoln Way']),
    '8th Ave': set(['Lincoln Way']),
    '9th Ave': set(['Lincoln Way']),
    '10th Ave': set(['Lincoln Way']),
    '11th Ave': set(['Lincoln Way']),
    '12th Ave': set(['Lincoln Way']),
    'Funston Ave': set(['Lincoln Way']),
    '14th Ave': set(['Lincoln Way']),
    '15th Ave': set(['Lincoln Way', 'Lawton St']),
    '16th Ave': set(['Lincoln Way', 'Lawton St']),
    '17th Ave': set(['Lincoln Way']),
    '18th Ave': set(['Lincoln Way']),
    '19th Ave': set(['Lincoln Way']),
    '20th Ave': set(['Lincoln Way']),
    '21st Ave': set(['Lincoln Way']),
    '22nd Ave': set(['Lincoln Way']),
    '23rd Ave': set(['Lincoln Way']),
    '24th Ave': set(['Lincoln Way']),
    '25th Ave': set(['Lincoln Way']),
    '26th Ave': set(['Lincoln Way']),
    '27th Ave': set(['Lincoln Way']),
    '28th Ave': set(['Lincoln Way']),
    '29th Ave': set(['Lincoln Way']),
    '30th Ave': set(['Lincoln Way']),
    '31st Ave': set(['Lincoln Way', 'Balboa St']),
    '32nd Ave': set(['Lincoln Way']),
    '33rd Ave': set(['Lincoln Way']),
    '34th Ave': set(['Lincoln Way']),
    '35th Ave': set(['Lincoln Way']),
    '36th Ave': set(['Lincoln Way']),
    '37th Ave': set(['Lincoln Way']),
    '38th Ave': set(['Lincoln Way', 'Rivera St']),
    '39th Ave': set(['Lincoln Way', 'Quintara St']),
    '40th Ave': set(['Lincoln Way', 'Quintara St']),
    '41st Ave': set(['Lincoln Way']),
    '42nd Ave': set(['Lincoln Way']),
    '43rd Ave': set(['Lincoln Way']),
    '44th Ave': set(['Lincoln Way']),
    '45th Ave': set(['Lincoln Way']),
    '46th Ave': set(['Lincoln Way']),
    '47th Ave': set(['Lincoln Way']),
    '48th Ave': set(['Lincoln Way']),
}



# For curved roads, where we will need to call the google maps
# directions API, define which parts of which paths are curved.
# WEST -> EAST
# SOUTH -> NORTH
curved_roads = {
    'Lawton St': [('16th Ave', 'Funston Ave')],
    '15th Ave': [('Noriega St', 'Lawton St')],
    'Clayton St': [('Market St', '17th St')],
    'Market St': [('Clayton St', 'Castro St')],
}

# These will be copied straight into the paths json object.
# All addresses in the paths will be looked up and given NEXT
# attributes.
custom_paths = {
    'The Panhandle / SF Bike Route 30': {
        'path': [
            'Baker St and Fell St',
            'San Francisco Bicycle Route 30 and Masonic Ave',
            'Kezar Dr and Stanyan St',
        ],
        'type': 'path'
    },
    'Lincoln Way to Frederick St': {
        'path': [
            '2nd Ave and Lincoln Way',
            'Arguello Blvd and Frederick St',
        ],
    },
}


# Define bike paths, bike routes, here!
# WEST -> EAST
# SOUTH -> NORTH
route_directives = {
    'Post St': [('Scott St', 'Steiner St', 'path'), ('Steiner St', 'Montgomery St', 'route')],
}
