PLACEHOLDER = "[name]"

#Read in file of names
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()


for name in names:
    name_trim = name.strip()
    new_letter = letter.replace(PLACEHOLDER, name_trim)
    with open(f"Output/ReadyToSend/letter_for_{name_trim}.txt", mode = "w") as completed_letter:
        completed_letter.write(new_letter)


