#TODO: PlayTest
#TODO: Multiplayer support
#TODO: Implement a bet feature
#TODO: Implement other features such as double down
###############################
#   Simple blackjack game    #
###############################

import art
import random
from os import system

def StartGame():
    GetPlayerACard()
    GetPlayerACard()
    GetDealerACard()
    GetDealerACard()
    PrintHands()


def GetACard():
    random_card_index = random.choice(cards)
    return cards[random_card_index]

def GetPlayerACard():
    score = GetScore(player_cards)
    if not score == 21:
        card = GetACard()
        player_cards.append(card)

def GetDealerACard():
    card = GetACard()
    dealer_cards.append(card)

def PrintHands():
    player_score = GetScore(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

def PrintFinalHands():
    player_score = GetScore(player_cards)
    dealer_score = GetScore(dealer_cards)
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

def GetScore(hand):
    sum = 0
    for card in hand:
        sum += card
    if sum > 21:
        sum = 0
        for card in hand:
            if card == 11:
                sum += 1
                continue
            sum += card
    return sum

def CheckScore(hand):
    score = GetScore(hand)
    if score > 21:
        return True
    if score == 21:
        print("Blackjack!")
    return False

def CheckWin(player_hand, dealer_hand):
    player_score = GetScore(player_hand)
    dealer_score = GetScore(dealer_hand)
    if dealer_score > 21:
        return True
    if player_score == 21:
        return True
    if player_score > dealer_score and player_score <= 21:
        return True
    if dealer_score > player_score and dealer_score <= 21:
        return False
    if dealer_score == player_score:
        return True

def PlayAgain():
    result = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if result == 'n':
        return False
    system('cls')
    Reset()
    print(art.logo)
    StartGame()
    return True

def Reset():
    player_cards.clear()
    dealer_cards.clear()
    
def HandleDealer():
    player_score = GetScore(player_cards)
    dealer_score = GetScore(dealer_cards)

    while player_score > dealer_score:
        GetDealerACard()
        dealer_score = GetScore(dealer_cards)
            


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

print(art.logo)

play = PlayAgain()

while play:
    player_wants_to_draw = True
    while player_wants_to_draw:
        current_player_score = GetScore(player_cards)
        if current_player_score < 21:
            answer = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer == 'n':
                player_wants_to_draw = False
                #AI GOES HERE
                HandleDealer()
            if answer == 'y':
                GetPlayerACard()
                PrintHands()
                game_end = CheckScore(player_cards)
                if game_end:
                    player_wants_to_draw = False
        if current_player_score >= 21:
            player_wants_to_draw = False
            HandleDealer()
    player_win = CheckWin(player_cards, dealer_cards)
    if not player_win:
        print("You Lost!")
        PrintFinalHands()
        
    if player_win:
        pl_score = GetScore(player_cards)
        dl_score = GetScore(dealer_cards)
        if pl_score == dl_score:
            print("Draw!")
            PrintFinalHands()
        else:
            print("You Win!")
            PrintFinalHands()
                
    play = PlayAgain()
        

