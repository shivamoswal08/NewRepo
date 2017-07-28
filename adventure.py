
def start():
    print "You are in a house"
    print "There is a door in front of you."
    print "\tType \"Open door"
    choice=raw_input("Enter choice : ")    
    if choice=="open":
        tv_room()
    elif "exit" in choice:            
        exit_house()

def tv_room():

    print "You enter the TV room."
    print "You can watch TV here."
    choice=raw_input("Which direction do you want to go ?? ")
        
    if choice=="west":
        library_room()              
    elif choice=="south":
        bed_room()
    elif choice=="north":
        print "You can't go there"
                
def library_room():
    print "You are in the library now"
    print "You can seat here and read the books."
                
def bed_room():
    print "You open the door and you are in the bed room."
    print "there is a huge bed here"
    choice=raw_input("Which direction do you want to go ?? ")
        
    if choice=="west":
        print "Well you are in the gallery"              
    elif choice=="north":
        print "well you are near the swimming pool now"
    elif choice=="east":
        print "You can't go there"


def exit_house():
    print "Bye!!!!"
    exit(0)

start()
  