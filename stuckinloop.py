secret_message = "chupacabra"
user_input= str(input("Enter a word: "))
while user_input != secret_message:
    user_input= str(input("Enter a word: "))
    if user_input == secret_message:
        print("You've successfully left the loop")
        break
        print("User Input: ", user_input)

"""Ugly Letter Word"""
# Prompt the user to enter a word
user_word = str(input("Enter a word:"))
# and assign it to the user_word variable.
user_word = user_word.upper()


for letter in user_word:
    # Complete the body of the for loop.
    if letter in "AEIOU":
        continue
    print("Remaining letters: ", letter)
    
"""Pretty letter word"""
word_without_vowels = ""

user_word = str(input("Enter a word:"))
# and assign it to the user_word variable.
user_word = user_word.upper()


for letter in user_word:
    # Complete the body of the loop.
    if letter in "AEIOU":
        continue
    word_without_vowels+=letter
        
    
# Print the word assigned to word_without_vowels.
print("words without vowels",word_without_vowels)
