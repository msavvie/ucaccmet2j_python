import json

# the precipitation.json file is a list of dictionaries
with open('precipitation.json', encoding = 'utf8') as file:
    rainfall_info = json.load(file)

# rainfall_info is now the list of dictionaries instead of the json file
# we want to sort through the list to idenitfy only station US1WAKG0038
# my challenge is to find a way to read the station number from within

seattle_station_code = 'GHCND:US1WAKG0038'

month_data = {}

for generic_raindata in rainfall_info:  # For each measurement 
    if (generic_raindata['station']) == seattle_station_code:  # If from Seattle
        month = generic_raindata['date'][5:7]
        # print(month)
        rainfall = generic_raindata['value']
        # print(rainfall)
        if month in month_data.keys():
            month_data[month] += rainfall
        else:
            month_data[month] = rainfall

        
print(month_data)



