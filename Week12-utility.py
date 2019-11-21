
# Manisha Jaiswal
# CSCI 101 – Section C
# Week 12 - Part A

# the incremental build model.


import math

#1

def PrintOutput(words_output):
    print("OUTPUT:",words_output)

#2
def LoadFile(lfile):
    afile = open(lfile)
    contents = afile.readlines() 
    return contents
#3
def UpdateString(string1,string2, index):
    #letter = string2[index]
    emptystring = ''
    for i in range(len(string1)):
        if i != index:
           emptystring += string1[i]
        else:
            emptystring += string2   
    print("OUTPUT", emptystring)
#4
def FindWordCount(list1, string):
    count = 0
    for i in list1:
        if i == string:
            count +=1 #count is how many times
    print("OUTPUT", count)

#5
def ScoreFinder(list1, list2, names):
    count = 0
    score = 0
    playerfound = False
    for i in list1:
        if i.lower() == names:
            score = list2[count]
            playerfound = True
        count += 1
    if playerfound == False:
        print("player not found")
    else:
        print("OUTPUT",names, "got a score of", score)
'''       
#6 Union
def Union():

#7 Intersection
def Intersection():

#8 NotIn
def NotIn():
'''


    
