dial_codes = [ 
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]


codes_dict = {country:code for code,country in dial_codes}
print(codes_dict)

filtered_dict = {country.upper():code for country,code in dial_codes  }
print(filtered_dict)
