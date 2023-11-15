import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato_df)

#Loop through rows of a data frame
nato_dict = {row.letter : row.code for (index, row) in nato_df.iterrows()}

#print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

nato_list = []

for letter in word:
    if letter in nato_dict.keys():
        nato_list.append(nato_dict[letter])


print(nato_list)
