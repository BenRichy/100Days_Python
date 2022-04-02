sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# use dictionary comprehension to take each word then calc number of letters in each word

# Write your code below:

words = sentence.split()
print(words)
result = {word:len(word) for word in words}


print(result)
