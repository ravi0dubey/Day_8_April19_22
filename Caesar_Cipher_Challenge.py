def encrypt_message(message_text,shift_pos):
  input_message = []
  pos = 0
  blank = " "
  char_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  for i in range(0,len(message_text)):
    input_message.insert(i,blank)
 
      
  for i in range(0,len(message_text)):
    for j in range(0,len(char_set)):
      if(message_text[i] == char_set[j]):
        input_message[i]= char_set[j+shift_pos]
        break
      
  
  print(input_message)



direction= input("Type 'encode' to encrypt, type 'decode'to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt_message(text,shift)