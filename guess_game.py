import random
target=random.randint(0,100)
while True:
      userchoice=int(input("guess the target :"))
      if userchoice == target:
           print("success : correct guess !!")
         break
    elif userchoice<target:
             print("guessed smaller number::")
         else :
            print("guessed larger number ::")
 print( "------GAME OVER-------)
