weather_c = {
    "Mon":12,
    "Tue":14,
    "Wed":15,
    "Thu":14,
    "Fri":21,
    "Sat":22,
    "Sun":24,
}

keys_list = weather_c.keys()
values_list = weather_c.values()
temp_f = [(temp*9/5)+32 for temp in values_list]
myDict = { k:v for (k,v) in zip(keys_list, temp_f)}
print(myDict)
weather_f = {day:(temp*9/5)+32 for (day,temp) in weather_c.items()}
print(weather_f)
#print(weather_c.items())
#print(weather_c)