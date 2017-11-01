# 1.) random word for dictionary txt file

initialdict = open(dictionary.txt)
raw = initialdict.readlines()
close(initialdict)

for word in raw:
    word = word.strip('\n')

wordlist = raw.split()

import random
mystery = random.choice(wordlist)
mystery = mystery.upper()
mysteryList = []

underscore = []
guesses = []
setGuess = set(guesses)
userIntent = True
    
def stringer(guess):
    for l in range(0,len(mysteryList)):
        for letter in mysteryList[l]:
            if guess == letter:
                guesses.append(guess)
                mysteryList[l], underscore[l] == underscore[l], mysteryLisy[l]
                    
            
        
# 2,3,4,5.)
while (userIntent == True):
    mysteryList = mystery.split('')
    underscore = list('_'*len(mysteryList))
    
    guess = input('Please guess a letter:').upper()
    stringer(guess)
    print(underscore)
    
 
