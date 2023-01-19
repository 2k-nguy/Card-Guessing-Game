

while (fuckUpCount != fuckUps) and cardCount != 52 and guess != "done":
        currCard = fullDeck[randrange(len(fullDeck))]
        print("TYPE THESE AND PRESS ENTER:",currCard.color, currCard.suit, currCard.value)
        guess = input("What is the card color? (Type Red or Black, SPELLING MUST BE EXACT)\n")
        if guess != currCard.color:
            fuckUpCount += 1
            print("You lost the card\n")
            print(f"Cards: {cardCount}/52")
            print(f"fuckUpCount:{fuckUpCount}")
            del currCard
            continue

        elif guess == currCard.color:
            print("\nYour color guess is correct. Now guess the suit\n")
            print(f"Cards: {cardCount}/52")
            print(f"fuckUpCount:{fuckUpCount}")

            guess = input("What is the card color? (Type Spade, Club, Diamond, or Heart, SPELLING MUST BE EXACT)\n")
            if guess != currCard.suit:
                print("You lost the card\n")
                print(f"Cards: {cardCount}/52")
                print(f"fuckUpCount:{fuckUpCount}")
                fuckUpCount += 1
                del currCard
                continue
                    
            elif guess == currCard.suit:
                print("\nYour suit guess is correct. Now guess the valuse\n")
                print(f"Cards: {cardCount}/52")
                print(f"fuckUpCount:{fuckUpCount}")
                        
                guess = input("What is the card color? (Type 2-10, Jack, Queen, King or Ace, SPELLING MUST BE EXACT)\n")
                if guess != currCard.value:
                    print("You lost the card\n")
                    print(f"Cards: {cardCount}/52")
                    print(f"fuckUpCount:{fuckUpCount}")
                    fuckUpCount += 1
                    del currCard
                    continue
                        
                elif guess == currCard.value:
                    cardCount += 1
                    print("\nYou value is correct, the card is yours\n")
                    print(f"Cards: {cardCount}/52")
                    print(f"fuckUpCount:{fuckUpCount}\n")
                    
    return fuckUpCount, cardCount
