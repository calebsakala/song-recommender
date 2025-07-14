import arraymaker


def format(dest, string_list):
	
  for element in string_list:
    string = ''
		split_sentence = element.split()
		for word in split_sentence:
			if word == 'verb' or word == 'adj.' or word == 'noun' or word == 'pron.' or word == 'interj.' or word == 'adv':
				word += ':'
			string += word + ' '

  destination_file = 'Output\dictionarymaker\{}.txt'.format(dest)
  
  with open(destination_file, "w") as writefile:
    writefile.write("{")
    for element in words_array:
      writefile.write(f"\"{element}\",")
    writefile.write("}")
  
  return destination_file
  


string_list = ["abject - adj. showing humiliation or submissiveness; of the most contemptible kind; most unfortunate or miserable; showing utter resignation or hopelessness", "aberration – noun: an optical phenomenon resulting from the failure of a lens or mirror to produce a good image; a disorder in one's mental state; a state or condition markedly different from the norm",
"abjure - verb formally reject or disavow a formerly held belief, usually under pressure"]

if __name__ == "__main__":
  source = input("Enter the name of the file that contains the data you need made into an array. \nInclude extensions like .txt or .docx\n> ")
  dest = input("What would you like to call the file that this program will output? \nDo not include extensions.\n> ")
  format(dest, arraymaker.create_array(source, dest))