import random

vowels = ["a", "i", "u", "e", "o"]
consants = ["k","g","s","z","t","t","d","n","h","b","p","m","r"]
others = ["ya", "yu", "yo", "wa", " "]
space = " "
new = vowels + consants
words = ""
syl = " "
newRange = int(input("length of text is:"))

for ii in range(0, newRange):
	isOther = random() % 25
	if(((isOther > 18) & (ii > 2) & (ii < (newRange - 2)) & (syl != space)) | (syl == "n")):
		syl = space
	else:
		isOther = random() % 25

		if((isOther > 20) & (syl != space)):
			syl = "n"
		elif(isOther > 17):
			syl = vowels[random() % 5]
		elif(isOther > 3):
			v = vowels[random() % 5]
			c = consants[random() % 13]
			syl = c+v
		else:
			syl = others[random() % 4]
	words = words + syl
	print(words)
