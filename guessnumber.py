import random
unknown=random.randint(1,99)
userInput=input("Enter your guess : ")
if unknown==userInput:
  print "Well done!!! You guessed it right"
elif userInput>unknown:
  print "The number is high"
else:
  print "The number is low"