"""
IS4010 final project: Pig-Latin converter
Author: Sean Spector
Date: April 2026
This program takes an English word input and converts it to Pig Latin and vice versa. The rules for Pig Latin are:
 1. If the words begins with a vowel, add "yay" to the end of the word.
 2. If the word begins with a consonant, move the first letter to the end of the word and add "ay".
3. If the word begins with multiple consants move all the consonants to the end of the word and add "ay".
"""
#The first part of the code should define a function that converts English to pig latin. It should take a string as input and return the pig latin version of the string. It should handle both uppercase and lowercase letters and preserve the original case. As a Python programmer, implement the function below.
def english_to_pig_latin(word):
    # Check if the first letter is a vowel
    vowels = "AEIOUaeiou"
    if word[0] in vowels:
        return word + "yay" #If the first letter is a vowel, add "yay" to end of the word
    else:
        # Find the index of the first vowel
        for i in range(len(word)): #Loop through the word to find first vowel
            if word[i] in vowels: #If the letter is a vowel, move all prior consonants to the end of the word + "ay"
                return word[i:] + word[:i] + "ay" 
        # If there are no vowels, treat the whole word as consonants
        return word + "ay" 

#The second part of the code should define a function that converts Pig Latin back to English. It should take a string as input and return the English version of the string. It should be able to handle both uppercase and lowercase letters as well as preserve the original case. AS a Python programmer, implement the function below.
def pig_latin_to_english(word): #Check if the word ends with "yay" or "ay" to determine of it's Pig Latin or English
    if word.endswith("yay"):
        return word[:-3] #If the word ends with "yay", remove those letters to find the English version of the word
    elif word.endswith("ay"):
        # Remove the "ay" at the end
        core_word = word[:-2] #If the words ends with "ay", remove those letters to find English version of the word
        # Find the last consonant cluster
        for i in range(len(core_word)-1, -1, -1): #Loop through the core word backwards to find the cluster of consonants
            if core_word[i] in "AEIOUaeiou": #If the letter is a vowel, move all later consonants to the front
                return core_word[i+1:] + core_word[:i+1] 
        return core_word  # If there are no vowels, return the core word
    
    #The third part of the code should have a main function that prompts the user to enter a word and then calls the correct function based on whether the input is in English or Pig Latin. It should then print the converted word. As a Python programmer, implement the main function below. 
def main(): 
    word = input("Enter a word in English or Pig Latin: ") #Prompt the user to enter a word
    if word.endswith("yay") or word.endswith("ay"): #check if the word is in Pig Latin or English
        print(word + " in English is " + pig_latin_to_english(word)) #If the word is in Pig Latin, convert to English and print the result
    else: 
        print(word + " in Pig Latin is " + english_to_pig_latin(word)) #If the word is in English, convert to Pig Latin and print the result
if __name__ == "__main__":    main() #Call the main function so the program can run