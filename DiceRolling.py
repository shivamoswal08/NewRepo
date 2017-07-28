import random
a=1
b=6

roll_again="yeah"

while roll_again=="yeah":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(a,b)
    print random.randint(a,b)

    roll_again=input("Roll the dices again?")