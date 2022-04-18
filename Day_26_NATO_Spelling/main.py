student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

#Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_abc_df = pd.read_csv("nato_phonetic_alphabet.csv")
# https://stackoverflow.com/questions/18695605/python-pandas-dataframe-to-dictionary
nato_abc_dict = nato_abc_df.set_index('letter')['code'].to_dict()
print(nato_abc_dict)


#Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_word = input('Please enter a word to convert into the NATO alphabet: ').upper()
    try:
        for letter in user_word:
            word_list = []
            word_list.append(nato_abc_dict[letter])
            print(word_list)
    except KeyError:
        print("Sorry, only words in the alphabet please!")
        generate_phonetic()

generate_phonetic()

