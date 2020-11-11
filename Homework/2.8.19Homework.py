#Hailey Tyler
#2-8-19
#Mad Lib
"""Mad Libs is a phrasal template word game that creates amusing sentences with a player's inputs."""
def madlib():
    print("This program will create a sentence based on the words that you supply.")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    adverb = input("Enter an adverb: ")
    verb = input("Enter a verb (present tense): ")
    print("The", adjective, noun, "will", adverb, verb, "over the moon.")
    answer = input("Do you want to play again? (Y/N)").upper()
    #Instead of a loop, I wrote an if else statement that will end the program if the user inputs "N", "n", "no", or "No" or it will run again
    if answer == "N" or answer == "NO":
        print("Thank you for playing!")
        input("Press the <Enter> key to quit.")
    else:
        madlib()
madlib()
