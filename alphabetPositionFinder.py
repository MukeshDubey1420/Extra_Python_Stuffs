"""
 let’s write it out as an alphabet variable.
 Each letter of the alphabet has a position, starting at position 0.
 So the letter ‘a’ is at position 0 of the alphabet, and ‘c’ is at position 2.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"


#Next, you’ll need to store the secret key in a variable.

key = 3

#Next, ask the user for a single letter (called a character) to encrypt.

character = input("please enter a character : ")


position = alphabet.find(character)    #Find the position of the character. You can get a letter from your alphabet variable by writing the position in square brackets.

#You can test the stored position by printing it. For example, that character ‘e’ is at position 4 in the alphabet.


print(position)

