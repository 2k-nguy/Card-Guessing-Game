# My attempt to make a card guessing game
# 1. Guess the color
# 2. Guess the suit
# 3. Guess the value
# 4. Repeat until the deck is done 

from random import randrange
import random

### Visually pleasing suit stream
def streamSuit():

    spade = "\u2660"
    club = "\u2663"
    diamond = "\u2666"
    heart = "\u2665"

    suitLst = [spade, club, diamond, heart]
    suitLine = []
    for i in range(60):
        suitLine.append(suitLst[randrange(len(suitLst))])
        
    suitStream = " ".join(suitLine)
    return suitStream
    
print(streamSuit())
print(streamSuit())
print(streamSuit())

streamSuit()

### Define necessary functions
def createDeck():
    class card:
        def __init__(self, color, suit, value):
            self.color = color
            self.suit = suit
            self.value = value
            
        def __repr__(self):
            return f"{self.color}, {self.suit}, {self.value}"
    
    deck = []

    for i in range(1, 14):
        if i == 1:
            i = "Ace"
        elif i == 10:
            i = "Jack"
        elif i == 11:
            i = "Queen"
        elif i == 13:
            i = "King"
            
        i = str(i)

        deck.append(card("Red", "Heart", i))
        deck.append(card("Red", "Diamond", i))
        deck.append(card("Black", "Spade", i))
        deck.append(card("Black", "Club", i))
        
    return deck

def guessColor(currCard, userColor):
    return bool(currCard.color == userColor)

def guessSuit(currCard, userSuit):
    return bool(currCard.suit == userSuit)

def guessValue(currCard, userValue):
    return bool(currCard.value == userValue)
  
def getCardFromDeck():
    return gameDeck[randrange(deckSize)]

### Define necessary variables
gameDeck = createDeck()
deckSize = len(gameDeck)
cardCount = 0
fuckUpCount = 0
tries = 0

### Where the game begins
while cardCount != 52:
    tries += 1
    currCard = getCardFromDeck()

    ### Guess card color
    guess = input("\nWhat is the card color? (Type Red or Black, SPELLING MUST BE EXACT)\n")
    
    if guessColor(currCard, guess):
        print("\nYou guessed the color correctly!")

        ### Guess the card suit
        guess = input("What is the card suit? (Type Spade, Club, Diamond, or Heart, SPELLING MUST BE EXACT)\n")

        if guessSuit(currCard, guess):
            print("\nYou guessed the suit correctly!")

            ### Guess the card value
            guess = input("What is the card value? (Type 2-10, Jack, Queen, King or Ace, SPELLING MUST BE EXACT)\n")

            if guessValue(currCard, guess):
                print("\nYou guessed the card correctly:", currCard)
                del currCard
                cardCount += 1


            ### When the color guess is wrong
            elif not(guessValue(currCard, guess)):
             fuckUpCount += 1
             print("\nYou lost the card:", currCard, end = "\n")
             print(f"Cards: {cardCount}/52")
             print(f"fuckUpCount:{fuckUpCount}", end = "\n")
             del currCard

        ### When the suit guess is wrong
        elif not(guessSuit(currCard, guess)):
         fuckUpCount += 1
         print("\nYou lost the card:", currCard, end = "\n")
         print(f"Cards: {cardCount}/52")
         print(f"fuckUpCount:{fuckUpCount}", end = "\n")
         del currCard
            

    ### When the value guess is wrong    
    elif not(guessValue(currCard, guess)):
         fuckUpCount += 1
         print("\nYou lost the card:", currCard, end = "\n")
         print(f"Cards: {cardCount}/52")
         print(f"fuckUpCount:{fuckUpCount}", end = "\n")
         del currCard

### Final Message
print(f"You guessed the deck! Only took you {tries} tries!")
print("Thanks for playing!")
