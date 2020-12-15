
code = ("#", "@", "&", "$", "^", "%", "|", "*", "~", ">" "<")

def count_char (text, char):
	count = 0
	for c in text:
		if c == char:
			count+=1
	return count

answer = input("What you want?\n")

if answer == "coding":
	text_o = input("input the text: ")

	for char in "абвгдеёжзийклмнопрстуфхцчшщыьэюя":
		perc = 100*count_char(text_o, char)/len(text_o)
		print("{0} - {1}%".format(char, round(perc,2)))

	while True:	
		text = text_o
		key_i = input ("key word: ")
		key_l = list(key_i)
		x=len(key_l)
		i=0
		for i in range(x):
			text=text.replace(key_l[0+i], code[0+i])
		print(text)
		
		answer1 = input("Do you like this wariant?")
		if answer1=="yes":
			file = open("file_coding.txt", "w")
			file.write(str(text))
			file.close()
			break
		if answer1=="no":
			continue
		else:
			print("Error!")

if answer == "uncoding":
	file = open("file_coding.txt", "r")
	text=file.read()
	file.close()
	key_i = input ("key word: ")
	key_l = list(key_i)
	x=len(key_l)
	i=0
	for i in range(x):
		text=text.replace(code[0+i], key_l[0+i])
	print(text)
	
	file = open("file_uncoding.txt", "w")
	file.write(text)
	file.close()
else:
	print("Error")