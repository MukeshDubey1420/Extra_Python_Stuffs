"""
 let’s write it out as an alphabet variable.
 Each letter of the alphabet has a position, starting at position 0.
 So the letter ‘a’ is at position 0 of the alphabet, and ‘c’ is at position 2.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

#Next, ask the user for a single letter (called a character) to encrypt.

character = input("please enter a character : ")

# store the  key in a variable.

key = int(input("enter the no. by which you shifted the character : "))




position = alphabet.find(character)    #Find the position of the character. You can get a letter from your alphabet variable by writing the position in square brackets.

#You can test the stored position by printing it. For example, that character ‘e’ is at position 4 in the alphabet.


print(position)

#To encrypt the character, you should add the key to the position.

# newPosition = position + key


#Test out your new code. As your key is 3, it should add 3 to the position and store it in your newPosition variable.

# print(newPosition)

#What happens when you try and encrypt the letter ‘y’?
#Notice how the newPosition is 27, and there aren’t 27 letters in the alphabet!
#You can use a % to tell the new position to go back to position 0 once it gets to position 26.
newPosition = (position + key) % 26
print(newPosition)

#Finally, you want to print the letter at the new position.

#For example, adding the key to the letter ‘e’ gives 7, and the letter at position 7 of the alphabet is ‘h’.

newCharacter = alphabet[newPosition]
print(newCharacter)

#Try out your code. You can also remove some of your print statements, just printing the new character at the end.

print("The new Character is " , newCharacter)
