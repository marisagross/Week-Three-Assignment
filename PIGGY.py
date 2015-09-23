# Marisa Gross
# Piggy.py
# Week 3: Pig Latin Assignment

#This program will translate words into Simple Pig Latin.

print("This program gives words in Pig Latin")
word=input("Enter an English word to translate: ")
vowel = "aeiou"
    
if word[0] in vowel:
    print(word + "yay")
else:
    print(word[1:] + word[0] + "ay")
    
    


# Create a framework of comments for each step in the specification.  
#Create a variable to hold the original word.  
#Create a variable to hold the translated word and Initialize it with an empty string ""  
#Create a variable to hold the first letter of the original word.  
#Test the first letter to see if it is a vowel or consonant. *See How To*  
	#If the first letter is a vowel, add the original word + "yay" to the translated word.    
	#Else, add all the remaining characters in the word to the translated word, + the first letter, + "ay" to get your translated word.  
#Test your program with the following words:
	#1. yello
	#2. hello
	#3. awesome
	#4. scratch
    