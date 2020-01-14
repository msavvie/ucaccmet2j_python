import json

# the precipitation.json file is a list of dictionaries
with open('precipitation.json', encoding = 'utf8') as file:
    rainfall_info = json.load(file)

# rainfall_info is now the list of dictionaries instead of the json file
# we want to sort through the list to idenitfy only station US1WAKG0038
# my challenge is to find a way to read the station number from within

seattle_station_code = 'GHCND:US1WAKG0038'

month_data = {}

for generic_raindata in rainfall_info:  # for each rainfall count 
    if (generic_raindata['station']) == seattle_station_code:  # if from Seattle
        month = generic_raindata['date'][5:7]
        # print(month)
        rainfall = generic_raindata['value']
        # print(rainfall)
        if month in month_data.keys():
            month_data[month] += rainfall
        else:
            month_data[month] = rainfall

months_rainfall_list = list(month_data.values())

with open('seattlerainfall.json', 'w') as file:
    json.dump(months_rainfall_list, file)

# to find percent of rain per month of the year we will add the precipitation
# the sum of the variable 'rainfall' will be the annual rainfall in Seattle
annual_rainfall = sum(months_rainfall_list)
print(annual_rainfall)

percent_rain_dictionary = {}
for month in month_data:
    percent_month = (f'{round((month_data[month]/annual_rainfall)*100, 2)}%')
    percent_rain_dictionary[month] = percent_month
print(percent_rain_dictionary)
