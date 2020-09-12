

'''
This is a general variable created to access the alphabet, so it wouldn't need
to be created within every function.
'''
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def load_text(file_name):
    file_hndl = open(file_name,"r")
    file_data = file_hndl.read()
    file_hndl.close()
    return file_data.upper()

'''
This function will save data to a text file.

@params        file_name, the name of the file to be saved
        file_data, the data to be written to the file
@return        none
'''
def save_text (file_name,file_data):
    file_hndl = open(file_name,"w")
    file_hndl.write(file_data)
    file_hndl.close()
    

'''
#The function "Encode" receives two string arguments and producse one string return value.
@params		current_text, the current_text which is encoded 
@return 	There is a string for encryption and decryption
'''

def encode (current_text, alpha):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    var = ''
    var_current_text = ''
    for i in current_text:
        var_current_text += i.upper()
    for b in range(len(var_current_text)):
        if var_current_text[b] in characters:
            for c in range(len(characters)):
                if var_curent_text[b] == characters[c]:
                    var += alpha[c]
        else:
            var += var_current_text[b]
    return var


'''
The function "decode" receives two string arguments and produces one string return value. It decodes the jambled texts.
@params		current_text), the current_text which is suppose to be decoded and the alpha which is required to decode
@return 	There is a string for encryption and decryption 	 
'''

def decode (current_text, alpha):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    var = ''
    var_current_text = ''
    for i in current_text:
        var_current_text += i.upper()
    for b in range(len(var_current_text)):
        if var_current_text[b] in characters:
            for c in range(len(alphabet)):
                if var_current_text[b] == alphabet[c]:
                    var += characters[c]
        else:
            var += var_current_text[b]
    return var


'''
The function Caesar Cipher Alphabet receives one interger argument and return one string return value. The alphabets are shifted according to the user input and displayed. 
@params	a, the integer value which determines the shift
@return	There is a string for encrypton and decryption
'''

def caesar_cipher_alphabet (a):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    start = ''
    finish = ''
    for i in range(len(characters)):
            if i >= a:
                start += characters[i]
            else:
                finish += characters[i]
    return start + finish


'''
The function keyword cipher alphabet receives one string argument and return one string return value. The argument is the keyword used to create a new alphabet for encoding or decoding where the order doesn't change. 
@params		top, it determines the alpha 
@return 	There is a string for encryption or decryption
'''

def keyword_cipher_alphabet (top):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    beg = ''
    last = ''
    var = ''
    for i in range(len(top)):
        if top[i] not in beg:
            beg += top[i].upper()
    last += beg
    while len(var) <= 26:
        for i in range(len(characters)):
            var += characters[i]
    for b in range(len(new)):
        if  var[b] not in final:
            last += var[b]
    return last


'''
The function crytpgram alphabet receives no arguments and produces one string return value. The function will use input to ask the user to type an alphabet.
@params 	none
@return 	There is a string for encryption or decryption 
'''
def cryptogram_alphabet ():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    var = ''
    b = ''
    for i in characters:
        if i not in b:
            b+= i.upper()
    if a.ischaracters() and len(b) == 26:
        for c in b:
            var += c
        return va
    else:
        print("Error!")
        return characters
        


def main(): 

	initial_text = ""
	current_text = ""
	alpha = ""
	print("Initial text:", initial_text)
	print("Currect text:", current_text)
	print("Current Cipher:", alpha)
	print("\tType '0' for detailed instruction")

		
	while (True):	
		
		selection = int(input("\tPlease input the number which you would like to use. (For example, if you want to Decode, press 3).\n"))	
		if (selection == 0):		
				print("WELCOME TO THE CIPHERING MACHINE!\n")
				print("This is your Menu:\n")
	


				print("1. Load - It will load the text file into the running program.")	
				print("2. Encode - This will encoded the text file which was loaded.")
				print("3. Decode - This will decode the text file which was loaded.")
				print("4. caesar cipher alphabet - This function will shift the letter to give a new alphabet wit the letter shift.")
				print("5. keyword cipher alphabet - The user gets to input keyword and it wil create your own cipher alphabet")
				print("6. cryptogram alphabet - This allows the user to put their own cryptogram alphabet")
				print("7. Save - This will save the current text in the text file")
			
		
		

		
	
		


		elif (selection == 1):
				initial_text = load_text(input("Please enter the name of the file"))
				current_text = initial_text
		elif (selection == 2):
				if (current_text == ""):
					print("There is no texted loaded. Try again.")
				else:
					if (alpha == ""):
						print("There is no alphabet loaded. Try again.")
					else:
						current_text = encode(current_text, characters)
		elif (selection == 3):
				if(current_text == ""):
					print("There is no texted loaded. Try again.")
				else:
					if (alpha == ""):
						print("There is no alphabet loaded. Try again.")
					else:
						current_text = decode(current_text, alpha)
		elif (selection == 4):
				switch = int(input("Enter the number of shifts:"))
				if (switch < 0):
					print("The shifts are required to be more than 0.")
				else:
					alphabet = caesar_cipher_alphabet(switch)

		elif (selection == 5):
				alpha = keyword_cipher_alphabet(input("Kindly type of Cipher keyword"))
		elif (selection == 6):
				alpha = cryptogram_alphabet(int(input("Input the number of shifts:")))
		elif (selection == 7):
				save_text(input("Please enter the name of the file:"), current_text)
				print("Congratulations! It is saved!")
		elif (selection == 8):
				alpha = caesar_cipher_alphabet(int(input("Input the number of shifts:"))) 
		else: 
				print("Invalid!")
	


	

	
	



            
'''
This is the main function, responsible for the user interface.

@params        none
@return        none
'''

main()
