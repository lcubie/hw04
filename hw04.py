# ------------------------------------------------------
#        Name: Lina
#       Peers: None
#  References: Presentations for syntax and google for variable.find
# ------------------------------------------------------
#We discussed pytest 4.3 (which I failed despite the code working) as something necessary to check

import sys

secret_word = "food"

# Task 1
def check_text():
    """ See if an string has "dog", "Dog" or a secret word, otherwise it makes you input another string"""
    #loop that runs unless broken
    while True:
        sentence = input("Give me a sentence: ")
        if sentence.find("Dog") != -1 or sentence.find("dog")!= -1:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break #String contains "Dog" or "dog" so leave the loop and tell the user
        
        elif secret_word in sentence:
            print("You used the secret word!")
            break #String contains secret_word so leave the loop and tell the user
        
        else:
            print("Try again")
            continue #meets neither of the conditions so loop continues

# Task 2
def check_greater():
    """ Checks which of two given input numbers is greater """
    #loop that runs unless broken
    while True:
        #Get the first and second input
        num1 = input("Give me a first integer: ")
        num2 = input("Give me a second integer: ")
        if num1 > num2:
            print("First is Greater")
            break
        elif num1 < num2:
            print("Second is Greater")
            break
        else:
            print("Try again")
            continue  #inputs are equal or not numbers so it continues until you put in two different numbers



# Task 3
def get_special_numbers():
    """ prints number between 1 and 41 that are multiples of three and not multiples of 2 or 5 """
    for counter in range(1,41):
        if counter % 2 == 0: #if multiple of 2 continue iteration
            continue
        elif counter %3 !=0: #if not a multiple of 3 continue iteration
            continue
        elif counter %5 ==0: #if multiple of 5 continue iteration
            continue
        else: 
            print(counter) #print what meets all criteria
            continue


# Task 4.a
def my_for_loop():
    """ Tells the user which letters are vowels or consonants in a string input that is 2-5 letters long and has no spaces"""
    word = input("Give me a string: ")
    
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    
    if len(word) < 2 or len(word) > 5 or word.find(" ") != -1: #check that it is 2-5 letters long with no spaces
        print("bad word") #if true, the function exits and prints "bad word"
        return
    else: #If the string is valid it iterates through each letter
        for counter in range(len(word)): 
            if word[counter] in vowels: #If the letter is in the vowels list above, it prints that it is a vowel
                let = word[counter]
                print(f"letter {let} is a vowel")
            else: #if it is not in the vowels list, it is a consonant
                let = word[counter]
                print(f"letter {let} is a consonant")
        

# Task 4.b
def my_while_loop():
    """ Returns different outputs for a, b, and c and repeats if not one of the three options """
    while True:
        selection = input("Choose one option: a, b, or c: ")
        if selection == "a": #will ask for a, b, c again if a is selected
            continue
        elif selection == "b": #Will leave the function and print Goodbye if b is selected
            print("Goodbye")
            return
        elif selection == "c": #Will exit main if c is selected
            exit()
        else: #asks for another input if it is not a, b, or c
            print("try again")
            continue

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
