#Python example

myName = input ("What is your name? ")
print ("Your name (", myName, ")is " , len(myName), " letters long")

for x in range (len (myName)):
    print ("The ", x, "letter in ", myName, "is", myName[x] )
else:
    print ("Finally finished!")
