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
    
  print(f"Encoded message: {cipher_text}")


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
    
  print(f"Decoded Message: {decipher_text}")

#Caesar function- Combined function for both encoding and Decoding
def caesar(message_text,shift_pos,direction):
  char_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  decipher_text = " "

  for char in message_text:
    final_pos = 0
    pos = char_set.index(char)
    if(direction== "decode"):
      if(pos - shift_pos < 0):
        final_pos= pos - shift_pos + 26
      else:
        final_pos= pos - shift_pos 
    else:
      if(pos + shift_pos >= 26):
        final_pos= pos + shift_pos - 26
      else:
        final_pos= pos + shift_pos      
      
    encrypt_letter = char_set[final_pos]
    decipher_text += encrypt_letter 
    
  print(f"Decoded Message: {decipher_text}")
  

# main para of program
end_game= False

while not(end_game):
  direction= input("Type 'Encode' to encrypt, type 'Decode'to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
#  if (direction == "encode"):
#    encrypt_message(text,shift)
  
#  if (direction == "decode"):
#    decrypt_message(text,shift)

#commong function Caeasar for both encryption and Decryption  
  caesar(text,shift,direction)
  game_continue = input("Type 'Y' to continue playing the game, else type 'N' :").lower()
  if(game_continue == "n"):
    end_game= True
  

