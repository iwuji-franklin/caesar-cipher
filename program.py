from art import logo
print(logo)
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z'
    ]


def encode(word, shift):
    shifted_letters = []
    encoded_word = ''
    # creating our shifted letters from the default letters
    for x in range(shift,len(letters)):
        shifted_letters.append(letters[x])
    # adding the shifted letters to the back of our already shifted letters
    # so that it will also be 26 alphabetical letters
    for x in range(shift):
        shifted_letters.append(letters[x])
    # getting each letter in the inserted text by user
    for letter in word:
        # if an alphabet, then encode it by: 
        if letter.isalpha():
            # tracing the position of the letter in the default letters
            position = letters.index(letter)
            # and using it to trace the same index in the shifted_letters
            encoded_word += shifted_letters[position]
        # if a number/space/symbol don't do anything, add it to the encoded text before moving to the next.      
        else:
            encoded_word += letter
    # returning both the encoded word and the derived shifted_letters
    # why are we returing shifted_letters?
    # because our decode function will use it and not to be repeating ourself below: 
    return encoded_word, shifted_letters
    
def decode(word,shift):
    decoded_word = ""
    # wow, this is where we made use of encode
    shifted_letters = encode(word, shift)[1]
    for letter in word:
        if letter == " ":
            decoded_word += letter
        elif letter.isdigit():
            decoded_word += letter
        elif letter.isalpha():
            positon = shifted_letters.index(letter)
            decoded_word += letters[positon]
        else:
            decoded_word += letter
    return decoded_word    
    
start = input("Press any key to continue!!!\n")
# validating our start statement
while len(start) >= 0 :
    if len(start) == 0:
        print("OOPS, empty text is not allowed!!!")
        start = input("Press any key to continue!!!\n")
    # if the text is a string break the loop and continue the program
    elif start.isalpha():
        print("We are about to start now, gather all your text together...")
        break
    else:
        print("You are only meant to insert only alphabet keys not symbols\\numbers")
        start = input("Press any key to continue!!!\n")
# while start is a true statement
while start:
    # checking if user inserted start value as stop,no,end.
    if start=="stop" or start=="end" or start=="no":
        print("Thanks for making use of our program, will like to see you again!!!")
        break

    text = input("insert your text here...\n").lower()
    shift_num = int(input("What is your shift number\n"))
    coding = input("Do you want to encode or decode?\n (e\\d)").lower()
    # calling on encode function,if coding value is encode
    if coding=="encode" or coding=="e":
        print(encode(text,shift_num)[0])
    # if the user want to decode
    else:
        print(decode(text,shift_num))
    start = input("Press any key to continue!!!\n")

