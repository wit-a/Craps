import random
print("- - - Craps Spiel - - -")
def wuerfeln():
    x1 = random.randrange(1,7)
    print(" erste Zahl:", x1,end='')
    x2 = random.randrange(1,7)
    print(" erste Zahl:", x2,end='')
    summe = x1 + x2
    print(" Summe: ",summe)
    return summe
print("--- 1. runde ---")
erste_runde = wuerfeln()
if(erste_runde == 2 or erste_runde == 3 or erste_runde == 12 ):
    print("VERLOREN IN ERSTER RUNDE")
if(erste_runde == 7 or erste_runde == 11 ):
    print("GEWONNEN IN DER ERSTEN RUNDE")
else:
    while True:
        print("--- 2. runde --- ")
        zweite_runde = wuerfeln()
        if(zweite_runde == 7):
            print("verloren in der zweiten runde")
            break
        if(erste_runde == zweite_runde):
            print("GEWONNEN")
            break
        else:
            zweite_runde = wuerfeln()
            


