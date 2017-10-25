### Michael Aduana
### CSC 241-Besana
### Homework 6
import os

#PART 1: cleanData function that takes 2 parameters
def cleanData(x,y):
    #empty list,dict to hold data during cleaning and writing to output
    cleanraw = []
    cleannumbers = []
    names = []
    cleandict = {}
    eliminated = {}

    #open initial txt file and outputfile
    initial = open(x)
    clean = open(y, mode = 'w')

    #read the txt file into container and closes it 
    raw = initial.readlines()
    initial.close()

    #cleans \n of the end of each line in text
    for line in raw:
        line = line.strip('\n')
        cleanraw.append(line)
    print(cleanraw)

    #original txt file formatted 12 characters from first number. seperates the first 12 characters
    #adds it to names list. Then append the rest of the line as a list seperated by space to a list called clean numbers
    for y in cleanraw:
        names.append(y[:12])
        x = y[12:].split(' ')
        cleannumbers.append(x)

    #this part looks at cleannumbers list and replaces the string values of the list to a float type
    for z in cleannumbers:
        for i in range(0,len(z)):
            numbers = float(z[i])
            z[i],numbers = numbers,z[i]
    #print(cleannumbers)

    #finally this part analyzes each float type in list object in list cleannumbers if it is less then 0 or greater than 10
    # if its either it removes the float object from the list
    for numbers in cleannumbers:
        for i in range(0,len(numbers)-1):
            if numbers[i] > 10 or numbers[i] < 0:
                numbers.remove(numbers[i])
    #print(cleannumbers)

    #this then merges the list into a dictionary object  
    for item in range(0,len(names)):
        cleandict[names[item]] = cleannumbers[item]
    #print(cleandict)

    # this then checks each dictionary object for 8 scores, if it has 8 scores then adds it to output file
    # if not then adds it to a dictionary for elimiated athletes
    for cleaninfo in cleandict:
        if len(cleandict[cleaninfo]) == 8:
            clean.write(cleaninfo + str(cleandict[cleaninfo]) +'\n')
        else:
            eliminated[cleaninfo] = cleandict[cleaninfo]
    print(eliminated)                
       
initialfile = input('Please enter the name of the file you would like to clean:')
cleanoutput = input('Please enter the name of the output file:')

cleanData(initialfile,cleanoutput)
