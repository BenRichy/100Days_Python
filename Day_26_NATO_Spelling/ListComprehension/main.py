import pandas as pd


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# square the numbers
square_numbers = [number ** 2 for number in numbers]
print(square_numbers)

# only even numbers
even_numbers = [number for number in numbers if number % 2 ==0]
print(even_numbers)

# get numbers which are in both datasets
list_1 = open("file1.txt").readlines()
list_2 = open("file2.txt").readlines()

result = [int(num) for num in list_1 if num in list_2]
print(result)


