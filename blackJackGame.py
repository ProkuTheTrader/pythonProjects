import random

from blackjack import logo
print(logo)

diretso = True 

# Do you want to Deal or no?
yesOrNo = input("Do you want to Deal? 'yes' or 'no'?:")
if yesOrNo == "yes":
    diretso = True
elif yesOrNo == "no":
    diretso = False 

totalplayerCards = 0
totalDealerCards = 0

# loop of adding cards until diretso is False
while diretso == True:
    playerCards = random.sample(range(2, 11), 2)
    print(f"This are your Cards: {playerCards}")

    totalplayerCards = 0
    for each in range(0, len(playerCards)):
        totalplayerCards += playerCards[each]
    print(totalplayerCards)
    if totalplayerCards == 21:
        diretso = False 
        print(f"Black Jack, YOU WON!!!")


    dealerCards = random.sample(range(2, 11), 1)
    dealerCards += []
    print(f"Dealer's Cards {dealerCards}")
    totalDealerCards = 0
    for each in range(0, len(dealerCards)):
        totalDealerCards = totalDealerCards + dealerCards[each]
    print(totalDealerCards)
    if dealerCards == 21:
        diretso = False 
        print(f"Black Jack, YOU WON!!!")



    hitItOrStand = True
# Hit or Stand
    while hitItOrStand:
        onlyFiveTimes = 0 
        hitOrStand = input("Do you want to 'hit' or 'stand'?: ")
        if hitOrStand == "hit":
            hitItOrStand = True
            diretso = False
            new_random_card  = random.sample(range(2, 11), 1)
            playerCards += new_random_card
            print(f"Your Cards: {playerCards}")
            totalplayerCards = sum(playerCards)
            print(totalplayerCards)
            onlyFiveTimes += 1
        if totalplayerCards == 21:
            hitItOrStand = False
            print("BLACK JACK")
        if totalplayerCards > 21 or onlyFiveTimes == 5:
            hitItOrStand = False 
            diretso = False
            print("BUST")
            
        elif hitOrStand == "stand":
            hitItOrStand = False
            diretso = False
            dealerCards += random.sample(range(2, 11), 1)
            dealerCards += random.sample(range(2, 11), 1)
            totalDealerCards = sum(dealerCards)

            print(f"Dealer's Cards: {dealerCards}")
            print(totalDealerCards)

            print(f"Your Cards: {playerCards}")
            print(totalplayerCards)
            if totalDealerCards == 21:
                print("Dealer Wins, Black Jack")
            if totalplayerCards == 21:
                print("You Win, Black Jack")
            if totalDealerCards > 21:
                print("You Win, BUST")
            if totalplayerCards > 21:
                print("You Lost, BUST")
            if totalDealerCards > totalplayerCards:
                print("You Lost")
            elif totalDealerCards < totalplayerCards:
                print("You Won")
            elif totalDealerCards == totalplayerCards:
                print("Punch")

            dealAgain = input("Wanna Deal Again? yes or no?")
            if dealAgain == "yes":
                diretso = True
            elif dealAgain == "no":
                diretso = False