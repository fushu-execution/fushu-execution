# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:16:53 2021

@author: Asus
"""

from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
from pyecharts.faker import Faker
#1930 0
y=[[('Canada',1),('Australia',1),('New Zealand',1),('South Africa',1),('United Kingdom',1),('Iraq',1),
    ('Jordan',1),#1946
    ('India',1),('Bangladesh',1),('Pakistan',1),#1947
    ('Sri Lanka',1),('Myanmar',1),#1948
    ('Egypt',1),#1952
    ('Sudan',1),('S.Sudan',1),#1956
    ('Malaysia',1),('Ghana',1),#1957
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]]
#1931 1
y.append([('United Kingdom',1),
    ('Iraq',1),#1932
    ('Jordan',1),#1946
    ('India',1),('Bangladesh',1),('Pakistan',1),#1947
    ('Sri Lanka',1),('Myanmar',1),#1948
    ('Egypt',1),#1952
    ('Sudan',1),('S.Sudan',1),#1956
    ('Malaysia',1),('Ghana',1),#1957
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
#1932 2
y.append([('United Kingdom',1),
    ('Jordan',1),#1946
    ('India',1),('Bangladesh',1),('Pakistan',1),#1947
    ('Sri Lanka',1),('Myanmar',1),#1948
    ('Egypt',1),#1952
    ('Sudan',1),('S.Sudan',1),#1956
    ('Malaysia',1),('Ghana',1),#1957
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
#1946 3
y.append([('United Kingdom',1),
    ('India',1),('Bangladesh',1),('Pakistan',1),#1947
    ('Sri Lanka',1),('Myanmar',1),#1948
    ('Egypt',1),#1952
    ('Sudan',1),('S.Sudan',1),#1956
    ('Malaysia',1),('Ghana',1),#1957
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
#47 4
y.append([('United Kingdom',1),
    ('Sri Lanka',1),('Myanmar',1),#1948
    ('Egypt',1),#1952
    ('Sudan',1),('S.Sudan',1),#1956
    ('Malaysia',1),('Ghana',1),#1957
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
#48 5
y.append([('United Kingdom',1),
    ('Egypt',1),#1952
    ('Sudan',1),('S.Sudan',1),#1956
    ('Malaysia',1),('Ghana',1),#1957
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
#52 6
y.append([('United Kingdom',1),
    ('Sudan',1),('S.Sudan',1),#1956
    ('Malaysia',1),('Ghana',1),#1957
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Malaysia',1),('Ghana',1),#1957
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Somalia',1),('Cyprus',1),#1960
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Sieraa Leone',1),('Kuwait',1),#61
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Jamaica',1),('Trinidad and Tobago',1),('Uganda',1),#62
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Singapore',1),('Kenya',1),#63
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Tanzania',1),('Malawi',1),('Malta',1),('Zambia',1),#64
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Gambia',1),#65
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Guyana',1),('Botswana',1),('Lesotho',1),('Barbados',1),#66
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Yemen',1),#67
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Nauru',1),('Mauritius',1),('Swaziland',1),#68
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Tonga',1),('Fiji',1),#70
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Bahrain',1),('United Arab Emirates',1),('Qatar',1),#
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Bahamas',1),#73
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Grenada',1),#74
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Seychelles',1),#76
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Djibouti',1),#77
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Solomon Is.',1),('Tuvalu',1),('Dominican',1),#78
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Saint Lucia',1),('Kiribati',1),('St. Vin. and Gren.',1),#79
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Zimbabwe',1),('Vanuatu',1),#80
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Belize',1),('Antigua and Barb.',1),#81
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1),
    ('Brunei',1)#84
    ]
    )
y.append([('United Kingdom',1)
    ]
    )
print(len(y))
years=[1930,1931,1932,1946,1947,1948,1952,1956,1957,1960,1961,1962,1963,1964,1965,1966,1967,1968,1970,
          1971,1973,1974,1976,1977,1978,1979,1980,1981,1984]
tl = Timeline()
for i in range(0,29):
    map0 = (
        Map()
        .add("殖民地", y[i], "world")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="英国{}年的殖民地".format(years[i])),
            visualmap_opts=opts.VisualMapOpts(
                range_text=["是", "否"],
                range_color=["white", "red"],
                max_=1,
                #min_=0
        )
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
    tl.add(map0, "{}年".format(years[i]))
tl.render("./timeline_map.html")

