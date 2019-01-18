# ============================================================
#
# Student Name (as it appears on cuLearn): Yiming He
# Student ID (9 digits in angle brackets): <101090748>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

'''
This function will load a text file.
@params		file_name, the name of the file to be loaded
@return		an uppercase string containing the data read from the file
'''
def load_text(file_name):
	file_hndl=open(file_name,"r")
	file_data=file_hndl.read()
	file_hndl.close()
	return file_data.upper()

'''
This function will save data to a text file.

@params		file_name, the name of the file to be saved
		file_data, the data to be written to the file
@returen	none
'''
def save_text(file_name, file_data):
	file_hndl=open(file_name,"W")
	file_hndl.write(file_data)
	file_hndl.close()



'''
This is the encode function, it is used to encode the text by user into special alphabt

@params		a, the alphabt that user want to encode
		b, the special alphabt which the encode is based on
@return 	c, the encoded alphabt
'''

def encode(a,b):
	defualta=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	a_list=list(a)
	b_list=list(b)
	defualta_list=list(defualta)
	c=""
	for i in a_list:
		count=0
		flag=True
		while flag:
			if count ==26:
				c+=i
				flag=False
			elif i==defualta_list[count]:

				c+=b_list[count]
				flag=False
			else:
				count=count+1
			 
	return c		

'''
This is the decode function, it is used to decode the text by user from special alphabt

@params		a, the alphabt that user want to decode
		b, the special alphabt which the decode is based on
@return 	c, the decoded alphabt
'''

def decode(a,b):
	a_list=list(a)
	b_list=list(b)
	defualta_list=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	c=""
	for i in a_list:
		count=0
		flag=True
		while flag:
			if count==26:
				c+=i
				flag=False
			elif i==b_list[count]:
				c+=defualta_list[count]
				flag=False
		
			else:
				count+=1
		
	return c


'''
This is the caesar_cipher_alphabet function, it is used to shift alphabet by users.

@params		d, the number that user want to shift
@return 	f+e, the alphabet which has shifted d times.
'''

def caesar_cipher_alphabet(d):
	defualta="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	e=""
	f=""
	for i in range (0,d):
		
		e+=defualta[i]
	for j in range (d,26):
		
		f+=defualta[j]
	return f+e

'''
This is the cryptogram_alphabt function, it is used to make a new alphabt by user.

@params		NONE
@return 	left, the alphabt that write by userself
'''

def cryptogram_alphabt():
	defualta="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	while True:	
		g=input("please write your 26 different letters.").upper()
		#g_list=list(g)
		#oa_list=list(oa)		
		left=""

		x1=0
		for x in g:
			count=0
			x1=x1+1
			y1=0
			for y in g:
				y1=y1+1				
				if x==y:
					count=count+1
				if (count==1) and (x1==y1) :
					left+=y
		if len(left)== 26:
			break
	return left
	


'''
This is the keyword_cipher_alphabet function, it is used to let user write some alphabets, removing and putting these in front of the default alphabet.

@params		NONE
@return 	left+oleft, the alphabt that write by userself with the default alphabet.
'''

def keyword_cipher_alphabet():
	h=input("please write the letters for the front of alphabt.").upper()
	defualta="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	left=""
	oleft=""
	
	x1=0
	for x in h:
		count=0
		x1=x1+1
		y1=0
		for y in h:
			y1=y1+1				
			if x==y:
				count=count+1
			if (count==1) and (x1==y1) :
				left+=y
	for i in defualta:
		if not i in left:
			oleft+=i
	return left+oleft

'''
This is the main function, responsible for the user interface. At first, it gives users two choices load or start a new one. when users choice start a new one, users could choice they want encode or decode their text. And at each of encode and decode, there are three type of cryptograms alphabet model that users can choice by themseleves. at the end of program, they can choice save the file or quit the program.

@params		none
@return		none
'''
def main():
	print("welcome to my cryptograms program, the following is the list of option you can choice:")
	print("1,load files.")
	print("2,start a new one.")

	print("0,Exit")
	flag=True
	while flag:
		firsti=int(input("which option you want choice?"))
		if 0<=firsti<3:
			flag=False
	if firsti==1:
		file_name=input("what is filename you want to load?")
		print(load_text(file_name))

	elif firsti==2:
		print("3,encode your letters.")
		print("4,decode your letters.")
		flag=True
		while flag:
			secondi=int(input("which option you want choice?"))
			if 2<secondi<5:
				flag=False
		if secondi==3:
			print("chioce one of these three type to modify your cryptograms alphabet:")
			print("5,shift the alphabet from defualt alphabet.")
			print("6,write your own 26 alphabet")
			print("7,choice the front letters at defualt alphabet.")		
			flag=True
			while flag:
				thirdi=int(input("which option you want choice?"))
				if 4<thirdi<8:
					flag=False
			if thirdi==5:
				d=input("how many times you want shift the defualt alphabet?")
				print(caesar_cipher_alphabet(int(d)))
				encode1=input("what letters you want to encode?").upper()
				print(encode(encode1,caesar_cipher_alphabet(int(d))))

				print("1,save")
				print("2,quit")
				encodechoice1=input("your code has been encode, you can type yes/no to choice save/quit.").upper()			
				if encodechoice1=="YES":
					file_name=input("what is filename you want to save?")
					print(save_text(file_name, file_data))				
				else:
					exit()
			elif thirdi==6:
				encode2=input("what letters you want to encode?").upper()
				print(encode(encode2,cryptogram_alphabt()))	
				print("1,save")
				print("2,quit")
				encodechoice2=input("your code has been encode, you can type yes/no to choice save/quit.").upper()			
				if encodechoice2=="YES":
					file_name=input("what is filename you want to save?")
					print(save_text(file_name, file_data))				
				else:
					exit()
			elif thirdi==7:
				encode3=input("what letters you want to encode?").upper()
				print(encode(encode3,keyword_cipher_alphabet()))
				print("1,save")
				print("2,quit")
				encodechoice3=input("your code has been encode, you can type yes/no to choice save/quit.").upper()			
				if encodechoice3=="YES":
					file_name=input("what is filename you want to save?")
					print(save_text(file_name, file_data))				
				else:
					exit()
		elif secondi==4:
			print("chioce one of these three type to modify your cryptograms alphabet:")
			print("5,shift the alphabet from defualt alphabet.")
			print("6,write your own 26 alphabet")
			print("7,choice the front letters at defualt alphabet.")		
			flag=True
			while flag:
				thirdj=int(input("which option you want choice?"))
				if 4<thirdj<8:
					flag=False
			if thirdj==5:
				d=input("how many times you want shift the defualt alphabet?")
				print(caesar_cipher_alphabet(int(d)))
				decode1=input("what letters you want to decode?").upper()
				print(decode(decode1,caesar_cipher_alphabet(int(d))))
				print("1,save")
				print("2,quit")
				decodechoice1=input("your code has been decode, you can type yes/no to choice save/quit.").upper()			
				if decodechoice1=="YES":
					file_name=input("what is filename you want to save?")
					print(save_text(file_name, file_data))				
				else:
					exit()
			elif thirdj==6:

				decode2=input("what letters you want to decode?").upper()
				print(decode(decode2,cryptogram_alphabt()))	
				print("1,save")
				print("2,quit")
				decodechoice2=input("your code has been decode, you can type yes/no to choice save/quit.").upper()			
				if decodechoice2=="YES":
					file_name=input("what is filename you want to save?")
					print(save_text(file_name, file_data))				
				else:
					exit()
			elif thirdj==7:

				decode3=input("what letters you want to decode?").upper()
				print(decode(decode3,keyword_cipher_alphabet()))
				print("1,save")
				print("2,quit")
				decodechoice3=input("your code has been decode, you can type yes/no to choice save/quit.").upper()			
				if decodechoice3=="YES":
					file_name=input("what is filename you want to save?")
					print(save_text(file_name, file_data))				
				else:
					exit()

	elif firsti==0:
		exit()
main()
	

