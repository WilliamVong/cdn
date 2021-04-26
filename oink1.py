#Team TPG - William Vongphanith, Abdal Abir, Zeng Wen Zou
#IntroCS pd6 sec10
#HW20 / Lab6 -- Pig Latin Translation Engine
#2021-04-25
#time cost: 2 hrs

'''
DISCOVERIES:
* Some words from pig latin were actually incorporated into actual English language.
* There is a Python library for pig latin.

UNRESOLVED MYSTERIES:
* What happens if we have an input with an unknown character?
* If we wanted to build a translator and there is an ambiguous word, how will we be able to distinguish between different words?

PIG LATIN RULES:
1. We translate by word, meaning that we'll split the input by spaces.
2. If the word starts with a consonant, we will return the rest of the word except the first letter upto the first vowel, then the first letter, then "ay".
3. If the word starts with a vowel, we will return the word followed by "way"
4. If the word is composed of two or more syllables, each syllable is transcribed seperately

SUMMARY OF APPROACH:
The function "translate" will take the input, whether it is a sentence or a word.
It will break up the input into words (split by spaces)
It will iterate over each word, doing the following for each word:
    It will check if the word starts with a vowel.
    If it does the variable "isVowel" will be set to true.
    If it isn't it will be set to false.
    It will pass the word and "isVowel" to the helper function.
    The helper function will translate the word, and return it.
    The main function will get the word and add it to another list.
When all the words are translated, we will join each word together and add spaces between each word.
We will return the translated word/sentence.

DEVELOPMENT LOG:
2021-04-24 <1 hr>
William Vongphanith spent most time doing the driving.
2021-04-25 <1 hr>
Abdal Abir revised to adhere to proper format and rules.
Zeng wen zou revised and helped in other aspects.
William Vongphanith, Abdal Abir, and Zeng When Zou: finished the assignment.
'''

def wordCheck(word):
    """Checks if the word starts with a vowel."""
    if word[0] in 'aeiou': # checks if the first character is "in" a string containing one of the five vowels.
        return True       # if so, return true
    return False          # if the if statement fails return false

def capitalCheck(word):
    """Checks if the first letter of the word is capital."""
    if word[0].isupper() == True: # checks if the first character is a capital letter.
        return True               # return true if so
    return False                 # if the if statement fails, return false

def position_of_first_vowel(word):
    """Get the index of the first vowel in a word. If no vowels in the word, return -1"""
    for index, char in enumerate(word): # gets each index of the character and the character itself, then for each,
        if char in 'aeiou':             # check if the character is "in" a string containing one of the five (or 6) vowels.
            return index                # return the index of the vowel
        if char in 'y' and word[0] != 'y':
            return index
    return -1                           # else return -1
# included y because
def translate_word(word, isVowel, isCapital):
    """Translates the word given to the function, considering whether the word starts with a vowel or not."""
    word = word.lower() # turn the whole word to lowercase, we can do this since "isCapital" is in the function call
    append = ""         # initialize "append"
    if word[-1].isalpha() == False: # check if the last character is not a letter of the alphabet (for example, a "?")
        append = word[-1]            # if so, set "append" to the last char of the word
        word = ''.join([i for i in word if i.isalpha()]) # remove any non-alphabet characters from the word (because we have the last char stored in "append")
    index = position_of_first_vowel(word) # get the position of the first vowel
    if isVowel == True: # if the word starts with a vowel
        if isCapital == True: # if the first letter of the word was capital
            return word[0].upper() + word[1:] + "way" + append # return the capital first letter, then the rest of the word, then "way", then append, if needed
        return word + "way" + append # else, return the word, followed by "way", then append, if needed.
    if index == -1: # if there were no vowels in the word whatsoever
        if isCapital == True: # if the first letter of the word was capital
            return word[0].upper() + word[1:] + "ay" + append # return the capital first letter, then the rest of the word, then "ay", then append, if needed
        return word + "ay" + append # else return the word, followed by "ay", then by append, if needed.
    else: # else (we've checked if word started by vowel or no vowels at all)
        if isCapital == True: # if first letter of word was capital
            return word[index].upper() + word[index+1:] + word[:index] + "ay" + append # return the first vowel, capitalized, then the rest of the word after the first vowel, then the part of the word before that, then "ay" then append
        return word[index:] + word[:index] + "ay" + append # else return the part of the word including the first vowel to the end, then the part before the first vowel, then "ay", then append

# comment out
# your test cases
# after verifying each fxn works

def translate(phrase):
    """Return Pig Latin equivalent of the string phrase."""
    words = phrase.split(" ") # split the phrase into words
    new_words = [] # initialize "new_words"
    for word in words: # evaluate the following for each word
        new_words.append(translate_word(word, wordCheck(word), capitalCheck(word))) # append the translated word to "new_words"
    return " ".join(new_words) # return "new_words" with each word bound together into a string, joined by a space.


print(translate("What are the rules of Pig Latin?"))
# -> "Atwhay areway ethay ulesray ofway Igpay Atinlay?"
print(translate("What are the rules of Pig Latin?") == "Atwhay areway ethay ulesray ofway Igpay Atinlay?") # validate that it matches

print(translate("the pope rocks red kicks"))
# -> "ethay opepay ocksray edray ickskay"
print(translate("the pope rocks red kicks") == "ethay opepay ocksray edray ickskay") # validate that it matches

print(translate("you yearn to whistle for your younger brother Larry")) #test case for letter y
# -> "ouyay earnyay otay istlewhay orfay ouryay oungeryay otherbray Arrylay"
print(translate("you yearn to whistle for your younger brother Larry") == "ouyay earnyay otay istlewhay orfay ouryay oungeryay otherbray Arrylay")
