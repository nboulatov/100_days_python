import csv
import pandas
data = pandas.read_csv("squirrel.csv")
gray = data['Primary Fur Color'].value_counts()['Gray']
cinnamon = data['Primary Fur Color'].value_counts()['Cinnamon']
black = data['Primary Fur Color'].value_counts()['Black']

data2 = pandas.DataFrame({
    'Fur Color': ["gray","cinnamon","black"],
    'Count': [gray,cinnamon,black],
})
data2.to_csv("squirrel_count")
