"""
IS4010 final project: Pig-Latin converter
Author: Sean Spector
Date: April 2026
This program takes an English word input and converts it to Pig Latin. The rules for Pig Latin are:
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
    
    #The second part of the code should have a main function that prompts the user to enter a word. It should then print the converted word. As a Python programmer, implement the main function below. 
def main(): 
    word = input("Enter a word in English: ") #Prompt the user to enter a word in English
    print(word + " in Pig Latin is " + english_to_pig_latin(word)) #Convert to Pig Latin and print the result
if __name__ == "__main__":    main() #Call the main function so the program can run

#Everything below is strictly for testing purposes. It should not be printed when the program is run.
#Make a meaningful test case to demonstrate the functionality of the program. Use the word "Hello" as the input and show the output.
#Test case : Input "Hello"
#Output: "Hello in Pig Latin is elloHay"
def test_cases():
    """
    Demonstrates and tests the functionality of the Pig Latin converter by converting
    the word "Hello" to Pig Latin, and printing the results.
    """
    # Test case 1: "Hello"
    english_word = "Hello"
    pig_latin_result = english_to_pig_latin(english_word)
     # print(f"{english_word} in Pig Latin is {pig_latin_result}")  # Expected output: "Hello in Pig Latin is elloHay"

    
    # Assertions for robust testing
    assert english_to_pig_latin("Hello") == "elloHay", "Test failed: 'Hello' should convert to 'elloHay'"

if __name__ == "__main__":
    # Uncomment one of the following lines to run either the main program or the tests
    # main()
    test_cases() #Call the test cases to demonstrate the functionality of the program