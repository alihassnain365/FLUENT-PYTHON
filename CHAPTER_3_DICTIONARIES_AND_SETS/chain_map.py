from collections import ChainMap

# default: dict[str,str] = {
#     'theme' : 'light',
#     'language':'English',
#     'font':'Ariel'
# }

# user_preferences: dict[str,str] = {
#     'theme':'dark'
# }

# current_session: dict[str,str] = {
#     'language':'Spanish'
# }

# print(default | user_preferences | current_session) # repeated keys are discarded


# user_settings: ChainMap[str,str] = (user_preferences, current_session, default)
# print(user_settings)

# print(user_settings["timezon"]) # checking for the missing keeys


""" updating values in chainmap"""
dict1: dict[str,str] ={
    'name' : 'ali',
}

dict2: dict[str,str] = {
    'name':'Ahmad',
    'city':'lahore'
}

cm: ChainMap[str,str] = ChainMap(dict1,dict2)

cm['city'] = 'karachi'

print(cm)

cm['city'] = 'ghanian'
print(cm)

del cm['city']

print(dict1)
print(dict2)
