#poker app
import random
from cards import deck
from player import Player
from game import Game



def main():

    deck.shuffle()
    print(len(deck))
    deck.dealCards()
    print(len(deck))


    #for card in deck:
    #    print(card)

if __name__ == "__main__":
    main()
