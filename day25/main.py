import csv
import pandas
# with open("weather_data .csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#data = pandas.read_csv("weather_data .csv")
#print(data)
#print(data["temp"])
#data_dict = data.to_dict()
#print(data_dict)
#temp_list = data["temp"].to_list()
#print(temp_list)
# total = sum(temp_list)
# items = len(temp_list)
# print(total/items)
#print(data["temp"].mean())
# max = 0
# for temp in temp_list:
#     if temp > max:
#         max = temp
# print(max)
#print(data["temp"].max())
#print(data.condition)
#print(data[data.day == "Monday"])
#max = data.temp.max()
#print(data[data.temp==data.temp.max()])
#print(data[data.day=="Monday"])
#monday = data[data.day=="Monday"]
#print(monday.condition)
#print(monday.temp)
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("file_name")