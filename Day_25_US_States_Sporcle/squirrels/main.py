import pandas as pd
#load in squirrel data
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#count number of squirrels by fur colour
squirrel_count = squirrel_data.groupby(['Primary Fur Color']).size()

print(squirrel_count)

# save squirrel numbers to csv
squirrel_count.to_csv("squirrel_fur_count.csv")