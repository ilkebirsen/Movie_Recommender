import pandas as pd
import random

#CSV READ & GENRE-TITLE
data = pd.read_csv("data.csv")

#CHOICE INPUT
choice = input('Please enter a word = ')

#SUGGESTION LOOP
while choice != "exit":
    choice = choice.lower()
    for index, row in data.iterrows():
        if choice in row['genre'].lower():
            result = [row['title']]
            print(random.sample(result, 1)[0])
            choice = input('Please enter a word = ')
