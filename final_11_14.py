""" Malcolm Grossman and Dylan Murphy
    CS 111 final
    Euchre game
"""

import random 


class Cards:
    """ This Class creates Card objects with two instance variables: suit and number. 
    
    parameters
    suit-  an int betweeen 0-4. Spades = 0, Clubs = 1, Hearts = 2, Diamonds = 3, Jokers = 4 and 5
    
    number - an integer value for the card values higher than ten retain their int value but are given a name object coresponding to traditional face cards in a deck.  
    """
    # this class creates cards. Each card has a number associated to its number and suit.
    def __init__(self, suit, number):
        
        self.suit = suit 
        self.number = number
        

        if self.suit == 0:
            self.suit_name = "spades"
        elif self.suit == 1:
            self.suit_name = "clubs"
        elif self.suit == 2:
            self.suit_name = "hearts"
        elif self.suit == 3:
            self.suit_name = "diamonds"
        elif self.suit == 4:
            self.suit_name = "white"
        elif self.suit == 5:
            self.suit_name = "red"
     

        if self.number == 11 or self.number == 31:
            self.number_name = "Jack"
        elif self.number == 12 or self.number == 32:
            self.number_name = "Queen"
        elif self.number == 13 or self.number == 33:
            self.number_name = "King"
        elif self.number == 14 or self.number == 34:
            self.number_name = "Ace"
        elif self.number == 15 or self.number == 35:
            self.number_name = "Joker"
        elif self.number == 16 or self.number == 36:
            self.number_name = "Joker"
        elif self.number > 21 and self.number < 31:
            self.number_name = (self.number - 20)
        else:
            self.number_name = self.number
            
        
       
    def get_suit(self):
        return self.suit

    def get_number(self):
        return self.number 

    def show_card(self):
        print(self.suit_name, self.number_name)
    
  
       
def declare_trump(hand, trump):
    """This function runs once trump is declared and changes all the cards in play that are of the trump
     class to a higher valued version of itself.
     Parameters:
     hand - a list of Card items representing the players hand
     trump - the suit that has been defined as trump
    """

    place= 0
    for card in hand:
        # if the suit name of the card is trump OR if the card is a White Joker (suit number 4) and the trump is of a black suit OR if the card is a Red Joker (suit number 5)
        # and the trump is of a red suit then the number value of the card is increased.
        if card.suit_name == trump or card.suit == 4  or card.suit == 5:
            new_card = Cards(card.suit, card.number + 20)
            hand[place] = new_card
        place += 1

     
       
    
class Deck:
    """ this class creates a deck containing cards. uses the Card class to create 54 cards with 4 sets of 13 cards in each suit and two jokers. 
    parameters 
    game_type - a user inputted value that chooses the number of cards to be played with. 
    """
    def __init__(self, game_type):
        self.game_type = game_type
        deck = []
        for i in range(4):
            for j in range(13):
                card = Cards(i, j+2)
                deck.append(card)
                
        for joker in range(2):
            card = Cards(joker+4, 15+joker)
            deck.append(card)
        self.deck = deck
        
    def get_deck(self):
        return self.deck
    
    def choose_cards(self):
        """
        this method determines how many cards will be played with in this game. redefines self.deck so that it reflects the deck that will be used in the game.
        """
        self.game_deck = []
        if self.game_type == 34:
            for k in self.deck:
                if k.get_number() >= 7:
                    self.game_deck.append(k)
            self.deck = self.game_deck
        
        elif self.game_type == 30:
            for k in self.deck:
                if k.get_number() >= 8:
                    self.game_deck.append(k)
            self.deck = self.game_deck
        
        elif self.game_type == 26:
            for k in self.deck:
                if k.get_number() >= 9:
                    self.game_deck.append(k)
            self.deck = self.game_deck
        return self.deck
        
    def shuffle(self):
        # this method shuffles the deck.
        self.shuffled_deck= []
        for card in self.game_deck:
            n = random.randrange(len(self.game_deck))
            self.shuffled_deck.insert(n, card)
        self.deck = self.shuffled_deck
        return self.deck

        
class Turn:
    # this class will be used to play each turn of Eucher.
    def __init__(self, deck, game_type, player0, player1, player2, player3):
        self.game_type = game_type
        self.deck = deck
        self.player0 = player0
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
#        self.trump = random.randrange(4)
        # use self.deck.deck to access the list of cards
        
    def getGameType(self):
        return self.game_type
    
    def getDeck(self):
        return self.deck
    
    def deal(self):
        for i in range(5):
            self.player0.hand.append(self.deck.deck.pop())
            self.player1.hand.append(self.deck.deck.pop())
            self.player2.hand.append(self.deck.deck.pop())
            self.player3.hand.append(self.deck.deck.pop())
        
    def decide_trump(self, turn):
        """this methods decides who's turn it is to choose trump. This is based on how many
        rounds have been played. Trump rotates from player0 to player1 to player2 to player3 
        and back to player0 again
        """
        valid_list = ["spades", "clubs", "hearts", "diamonds" ]
        if turn == 0:
            trump = input("What suit do you want to be trump? Spades, Clubs, Hearts, Diamonds ")
            trump.lower()
            while trump not in valid_list:
                trump = input("What suit do you want to be trump? Spades, Clubs, Hearts, Diamonds ")
                trump.lower()      
        elif turn == 1:
            trump = self.player1.pick_trump()
        elif turn == 2:
            trump = self.player2.pick_trump()
        elif turn == 3:
            trump = self.player3.pick_trump()

        if trump == 0:
            trump = "spades"
        elif trump == 1:
            trump = "clubs"
        elif trump == 2:
            trump = "hearts"
        elif trump == 3:
            trump = "diamonds"
        return trump

    def showCards(self, cards_played):
        # shows which cards have been played
        print("The cards now in play are :")
        for card in cards_played:
            card.show_card()

    def trick(self, cards_played, trump, turn, winner):
        """This method determines what order the players go in. If it's the very first turn the user will
        always go first however after that the winner will go.
        Parameters:
        cards_played - a list of the cards that have already been played
        trump - the suit that is trump
        turn - what turn it is
        winner - who won the last trick
        """
        player_list = []
        print("TURN: ", turn)
    
        if turn == 1 or winner.getName() == "You":  
            self.showCards(cards_played)
            player_trick(self.player0, cards_played, turn, trump)
            AI_trick(self.player1, cards_played, trump, False)
            AI_trick(self.player2, cards_played, trump, False)
            AI_trick(self.player3, cards_played, trump, False)
            player_list = [self.player0, self.player1, self.player2, self.player3]
        elif winner.getName() == "AI1":
            AI_trick(self.player1, cards_played, trump, True)
            AI_trick(self.player2, cards_played, trump, False)
            AI_trick(self.player3, cards_played, trump, False)
            self.showCards(cards_played)
            player_trick(self.player0, cards_played, turn, trump)
            player_list = [self.player1, self.player2, self.player3, self.player0]
        elif winner.getName() == "AI2":
            AI_trick(self.player2, cards_played, trump, True)
            AI_trick(self.player3, cards_played, trump, False)
            self.showCards(cards_played)
            player_trick(self.player0, cards_played, turn, trump)
            AI_trick(self.player1, cards_played, trump, False)
            player_list = [self.player2, self.player3, self.player0, self.player1]
        elif winner.getName() == "AI3":
            AI_trick(self.player3, cards_played, trump, True)
            self.showCards(cards_played)
            player_trick(self.player0, cards_played, turn, trump)
            AI_trick(self.player1, cards_played, trump, False)
            AI_trick(self.player2, cards_played, trump, False)
            player_list = [self.player3, self.player0, self.player1, self.player2]

        self.cards_played = cards_played
        self.player_list = player_list

    def decide_winner(self):
        # decides who won the trick
        high_card = self.cards_played[0]
        for card in self.cards_played:
            if card.number > high_card.number:
                high_card = card
        idx_card = self.cards_played.index(high_card)
        winner = self.player_list[idx_card]
        winner.score += 1
        print(winner.getName(), " won the hand!")
        return winner


                
class Player:
    # creates a player that can either be controlled by the player or the AI.
    def __init__(self, score, name):
        self.score = score
        self.hand = []
        self.name = name
   
    def getHand(self):
        return self.hand
    
    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def showHand(self):
        place = 0
        print("your cards are: ")
        for i in self.hand:
            place += 1
            print(place, end = "\t")
            i.show_card()

class AI:
    def __init__(self, score, name):
        self.score = score
        self.hand = []
        self.name = name

    def getHand(self):
        return self.hand

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def pick_trump(self):
        # decides what the AI should pick as trump
        spades = 0
        clubs = 0
        hearts = 0
        diamonds = 0
        for card in self.hand:
            if card.get_suit() == 0:
                spades += 1
            elif card.get_suit() == 1:
                clubs += 1
            elif card.get_suit() == 2:
                hearts += 1
            elif card.get_suit() == 3:
                diamonds += 1
            trump_list = [spades, clubs, hearts, diamonds]
            trump_list.sort()
            trump = trump_list[3]
        return trump

def Rules():
    """This function tell the player the rules of the game
    """
    rules_file = open("Rules.txt", "r")
    for aline in rules_file:
        print(aline)
    cont = input("Press ENTER to continue. ")
    while cont != "":
        cont = input("Press Enter to continue")



def AI_trick(player, cards_played, trump, go):
    """ This function determines what card the AI plays based on the cards in play, the cards in it's hand, and what trump is.
        Parameters:
        Player - the player(AI) that will be playing the cards
        cards_played - a list of Card items that show what cards have been played by other players
        trump - what suit trump is
    """
    #the play card is always by default the leading card
    hand_list = []
    idx_hand = 0
    if go:
        for j in player.hand:
            hand_list.append([idx_hand, j.get_number()])
            idx_hand += 1
        sort_cards(hand_list)
        

        for i in hand_list:
            if i[1] == 14:
                card_place = i[0]
            else:
                card_place = hand_list[len(hand_list)-1][0]

        
        
        
        
    else:
        suit = cards_played[0].get_suit()
        number = cards_played[0].get_number()
        play_card = cards_played[0]
        for i in cards_played:
            """
            determines what the play card is based on its suit and number
            """
            if i.get_suit() == suit and i.get_number() >= number:
                """if the suit is the same as the original suit and the number is greater then the high number and play card
                are updated to the new play card (play_card)
                """
                number = i.get_number()
                play_card = i
            elif i.suit_name == trump:
                """ if the suit name is not the same os the original but is trump then the suit is updated to trump, the number
                is updated to the first trump card played, and so is the card
                """
                suit = i.suit_name
                number = i.get_number()
                play_card = i
            elif suit == trump and i.get_number() >= number:
                """ if the suit is already trump and the number of the played card of the trump suit is greater than that of 
                the play card of the trump suit then the number and play card are updated
                """
                number = i.get_number()
                play_card = i

            elif i.get_suit() == 4 or i.get_suit() == 5:
                suit = trump
                number = i.get_number()
                play_card = i

    # these lists will be filled with cards basd on their position relative to the play card
        high_list = []
        low_list = []
        trump_high_list = []
        trump_low_list = []
        idx_hand = -1



        for card in player.hand:
            # moves through the cards in the players hand comparing them to the current play card
            idx_hand+= 1
            hand_list.append([idx_hand, card.get_number()])
            if card.get_suit() == suit:
                if card.get_number() > number:
                    high_list.append([idx_hand, card.get_number()])
                elif card.get_number() < number:
                    low_list.append([idx_hand, card.get_number()])
            elif card.get_suit() == trump:
                if card.get_number() > number:
                    trump_high_list.append([idx_hand, card.get_number()])
                elif card.get_number() < number:
                    trump_low_list.append([idx_hand, card.get_number()])
            elif card.get_suit() == 4:
                if card.get_number() > number:
                    trump_high_list.append([idx_hand, card.get_number()])
                elif card.get_number() < number:
                    trump_low_list.append([idx_hand, card.get_number()])
            elif card.get_suit() == 5:
                if card.get_number() > number:
                    trump_high_list.append([idx_hand, card.get_number()])
                elif card.get_number() < number:
                    trump_low_list.append([idx_hand, card.get_number()])
      
       
        sort_cards(high_list)
        sort_cards(low_list)
        sort_cards(trump_high_list)
        sort_cards(trump_low_list)

        if high_list == [] and low_list != []:
            card_place = low_list[0][0]
        elif low_list == [] and high_list != []:
            card_place = high_list[0][0]
        elif low_list != [] and high_list != []:
            if (len(low_list) + len(high_list)) > 3:
                try: 
                    card_place = high_list[1][0]
                except:
                    card_place = high_list[0][0]
            else:
                card_place = high_list[0][0]
        elif high_list == [] and low_list == [] and trump_high_list != []:
            card_place = trump_high_list[0][0]
        elif high_list == [] and low_list == [] and trump_low_list != [] and trump_high_list == []:
            card_place = trump_low_list[0][0]
            

        else:
            # if the AI doesn't have trump or a card of the leading suit it chooses the lowest card in its hand
            
            sort_cards(hand_list)
            card_place = hand_list[0][0]    
        

    print(player.getName() , "played")
    player.hand[card_place].show_card()
    cards_played.append(player.hand.pop(card_place))

   
def sort_cards(alist):
    """ this function sorts a list of cards based on their number
    parameters- 
    alist: a list of card objects
    """
    n = len(alist)
    for i in range(1,n):
        cur_index = i - 1 
        cur_item= alist[i]
        while cur_index >= 0 and alist[cur_index][1] > cur_item[1]:
            alist[cur_index + 1]= alist[cur_index]
            cur_index = cur_index-1
        alist[cur_index+1]= cur_item



def player_trick(player, cards_played, turn, trump):
    valid_list = [1,2,3,4,5]
    play_card = input("What card would you like to play? (integer 1-5)")
    if cards_played == []:
        # if the player goes first there should be no issues with entering the wrong card
        while play_card == "":
            play_card = input("What card would you like to play? (integer 1-5)")
        play_card = int(play_card)
        while play_card not in valid_list and (play_card > (len(valid_list)-turn+1) or play_card <= 0):
            play_card = int(input("What card would you like to play? (integer 1-5)"))
    else:
        while play_card == "":
            play_card = input("What card would you like to play? (integer 1-5)")
        play_card = int(play_card)
        while play_card not in valid_list and (play_card > (len(valid_list)-turn+1) or play_card <= 0):
            play_card = int(input("What card would you like to play? (integer 1-5)"))
        # if the player does not go first then they must follow suit if possible or play trump if they cannot follow suit
        # if they can't do either of those then they can play whatever they want
        check_follow = False
        check_trump = False
        if cards_played[0].suit == 4 or cards_played[0].suit == 5:
            check_follow = True
            high_suit = None

        else:
            high_suit = cards_played[0].suit

        if player.hand[play_card-1].suit == high_suit:
             check_follow = True
             check_trump = True

    
        elif player.hand[play_card-1].suit != high_suit:
            check = 0
            for card in player.hand:
                if card.suit == high_suit:
                    check += 1
            if check == 0:
                check_follow = False

        elif player.hand[play_card-1].suit == trump:
            check_trump = True

        elif player.hand[play_card-1].suit != trump or player.hand[play_card - 1].suit != 4 or player.hand[play_card - 1].suit != 5:
            check = 0 
            for card in player.hand:
                if card.suit == trump or card.suit == 4  or card.suit == 5:
                    check += 1
            if check == 0:
                check_follow = False

        while check_follow == False and play_card not in valid_list and (play_card > (len(valid_list)-turn+1) or play_card <= 0):
            play_card = int(input("You must follow suit, play a card of the same suit as the first card played. (integer 1-5)"))
            if player.hand[play_card - 1].suit == cards_played[0].suit:
                check_follow = True
                check_trump = True

        while check_trump == False and play_card not in valid_list and (play_card > (len(valid_list)-turn+1) or play_card <= 0):
            play_card = int(input("You cannot follow suit but you have a trump card in your hand. You must play a trump card. (integer 1-5)"))
            if player.hand[play_card - 1].suit == trump or player.hand[play_card - 1].suit == 4 or player.hand[play_card - 1].suit == 5:
                check_trump = True

    cards_played.append(player.hand.pop(play_card-1))


def play_game():
    # plays the game
    Rules()
    valid_list = ["34","30","26"]
    cardChoice= input("How many cards do you want to play with? 34, 30, 26 ")
    while cardChoice not in valid_list:
        cardChoice= input("How many cards do you want to play with? 34, 30, 26 ")
    cardChoice= int(cardChoice)
    # I think we should figure the game out with four players and then allow the option to choose after we've figured that out.
    """
    """
    winner = None
    score0 = 0
    score1 = 0
    score2 = 0
    score3 = 0
    game_score1 = 0
    game_score2 = 0
    player0 = Player(score0, "You")
    player1 = AI(score1, "AI1")
    player2 = AI(score2, "AI2")
    player3 = AI(score3, "AI3")
    turn = 0
    play_trump = 0
    while game_score1 < 10 and game_score2 < 10:
        deck = Deck(cardChoice)
        deck.choose_cards()
        deck.shuffle()
        t = Turn(deck, cardChoice, player0, player1, player2, player3)
        t.deal()
        player0.showHand()
        if play_trump == 4:
            play_trump = 0
        trump = t.decide_trump(play_trump)
        declare_trump(player0.hand, trump)
        declare_trump(player1.hand, trump)
        declare_trump(player2.hand, trump)
        declare_trump(player3.hand, trump)
        print("Trump this turn is: ", trump)
        play_trump += 1
        
        while player0.hand != []:
            turn += 1
            if turn == 5:
                turn = 0
            cards_played = []
            t.trick(cards_played, trump, turn, winner)
            winner = t.decide_winner()
            print("SCORES:")
            print(player0.getName(),    player0.getScore())
            print(player1.getName(),    player1.getScore())
            print(player2.getName(),   player2.getScore())
            print(player3.getName(),    player3.getScore())
            player0.showHand()
        comp_score1 = player0.getScore() + player2.getScore()
        comp_score2 = player1.getScore() + player3.getScore()

        if comp_score1 == 3:
            game_score1 += (comp_score1 + 2)
            game_score2 -= 1
        elif comp_score1 == 5:
            game_score1 += (comp_score1 + 3)
            game_score2 -= 2

        elif comp_score2 == 3:
            game_score2 += (comp_score2 + 2)
            game_score1 -= 1

        elif comp_score2 == 5:
            game_score2 += (comp_score2 + 3)
            game_score1 -= 2

        print("The score of Team 1 is ", game_score1)
        print("The score of Team 2 is ", game_score2)

        player0.score = 0
        player1.score = 0
        player2.score = 0
        player3.score = 0

    if game_score1 >= 10 and game_score2 >= 10:
        print("IT'S A TIE!")
    elif game_score1 >= 10:
        print("YOU WON THE GAME!") 

    elif game_score2 >= 10:

        print("YOU LOST THE GAME!")
    
        
def main():
    play_game()
    
    
if __name__ == "__main__":
    main()
