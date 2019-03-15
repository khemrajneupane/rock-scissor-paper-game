

import random

def rand(machine):
    if machine == 1:
        machine = "Rock"
    elif machine == 2:
        machine = "Paper"
    elif machine == 3:
        machine = "Scissors"
    return machine

    
def main():
    playCounter = 0
    ownCounter = 0
    tieCounter = 0
  
    
    while True:
        machine = random.randint(1,3)
        yourValue = input("Rock, Paper or Scissors? (Quit ends): ")
        if yourValue != "Quit":
            if yourValue == "Spaceshuttle":
                print("Incorrect selection.")
            else:
                print("You chose: ", yourValue, "Computer chose: ", str(rand(machine)))
                playCounter += 1
            
                if ((yourValue, machine) == ("Rock",1)) or ((yourValue, machine) == ("Scissors",3)):
                    print("It is a tie!")
                    tieCounter += 1
                
                elif ((yourValue, machine) == ("Scissors", 1)) or ((yourValue, machine) == ("Paper", 3)) or ((yourValue, machine) == ("Rock", 2)):
                    print("You LOSE!")
                
                elif (yourValue, machine) == ("Paper", 2):
                    print("Both LOSE!")
                elif ((yourValue, machine) == ( "Rock", 3)) or ((yourValue, machine) == ("Paper", 1)) or ((yourValue, machine) == ("Scissors", 2)):
                    print("You WIN!")
                    ownCounter += 1
        else:
            print("You played {}".format(playCounter)+" rounds, and won {}".format(ownCounter)+ " rounds, playing tie in {} ".format(tieCounter)+" rounds.")
            break
            
    
if __name__ == "__main__":
    main()