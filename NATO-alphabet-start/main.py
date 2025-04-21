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
natodata = pandas.read_csv(open("nato_phonetic_alphabet.csv"))
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass

students = {index:row.student for (index,row) in student_data_frame.iterrows()}
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
letters_nato = {letter_nato.letter:letter_nato.code for letter,letter_nato in natodata.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
result = [letters_nato[nato_letter] for nato_letter in user_input]
print(result)
