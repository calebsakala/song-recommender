import os

def create_array(source, dest):
	words_array = []

	with open(source, "r") as file:
		for line in file:
			words_array.append(line.strip())

	print(f'The last ten elements of your array are {words_array[-10:-1]}')
	print(f'The length of your array is {len(words_array)}')

	destination_file = '{}.txt'.format(dest)

	with open(destination_file, "w") as writefile:
		writefile.write("{")
		for element in words_array:
			writefile.write(f"\"{element}\",")
		writefile.write("}")

	return words_array

source = input("Enter the name of the file that contains the data you need made into an array. \nInclude extensions like .txt or .docx\n> ")
dest = input("What would you like to call the file that this program will output? \nDo not include extensions.\n> ")

create_array(source, dest)