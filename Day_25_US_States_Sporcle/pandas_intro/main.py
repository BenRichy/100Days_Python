# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"].mean())
print(data["temp"].max())

# Day with highest temp
print(data[data["temp"]==max(data["temp"])])

# Monday's temp in Farenheit
print(data["temp"][data["day"]=="Monday"]*(9/5)+32)
