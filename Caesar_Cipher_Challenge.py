def encrypt_message(message_text,shift_pos):
  char_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  cipher_text = " "

#approach 1  
  #input_message = []
  #blank = " "  
  #for i in range(0,len(message_text)):
  # input_message.insert(i,blank)
      
  #for i in range(0,len(message_text)):
  # for j in range(0,len(char_set)):
  #    if(message_text[i] == char_set[j]):
  #      if(j+shift_pos > 26):
  #        input_message[i]= char_set[j+shift_pos - 26]
  #      else:
  #        input_message[i]= char_set[j+shift_pos]
  #      break
  #print(input_message)

#approach 2  
  for char in message_text:
    pos = char_set.index(char)
    if(pos+shift_pos > 26):
      encrypt_letter = char_set[pos+shift_pos - 26]
    else:
      encrypt_letter = char_set[pos+shift_pos]
    cipher_text += encrypt_letter   
    
  print(cipher_text)


#Decrypt function
def decrypt_message(message_text,shift_pos):
  char_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  decipher_text = " "


  for char in message_text:
    pos = char_set.index(char)
    if(pos - shift_pos < 0):
      encrypt_letter = char_set[pos - shift_pos + 26]
    else:
      encrypt_letter = char_set[pos - shift_pos]
    decipher_text += encrypt_letter 
    
  print(decipher_text)  

  

# main para of program

direction= input("Type 'encode' to encrypt, type 'decode'to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if (direction == "encode"):
  encrypt_message(text,shift)

if (direction == "decode"):
  decrypt_message(text,shift)