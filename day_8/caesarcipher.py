from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesarcipher(input_text, input_shift, cipher_direction):
  message_output = ""
  if cipher_direction == "decode":
    input_shift *= -1
  for char in input_text:
   
    if char in alphabet:
      current_position = alphabet.index(char)
      new_position = current_position + input_shift
      message_output += alphabet[new_position]
    else:
      message_output += char
  print(f"Your {cipher_direction}d message is : {message_output}")


keep_ciphering = True
while keep_ciphering == True:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % 26

  caesarcipher(input_text=text, input_shift=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    keep_ciphering = False
    print("Goodbye")
    


