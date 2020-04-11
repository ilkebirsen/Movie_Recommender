import pandas as pd
import random
import sys

#CSV READ & GENRE-TITLE
data = pd.read_csv("data.csv") # https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset/data#IMDb%20movies.csv

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
        elif choice == "exit":
            choice = "exit"
            sys.exit()

        else:
            print("The genre {} doesn't exist".format(choice))
            choice = input('Please enter a word = ')
