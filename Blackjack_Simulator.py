
import random
import time


class Card():
    """Class to simulate a single card"""

    def __init__(self, rank, value, suit):
        """Initialize attributes"""
        self.rank = rank
        self.value = value
        self.suit = suit

    
    def display_card(self):
        """Show the card's rank and suit"""
        print(self .rank + " of " + self.suit)
        

class Deck():
    """Class to simulate building a deck of 52 cards"""

    def __init__(self):
        """Initialize attributes"""

        # List to hold all 52 cards
        self.cards = []


    def create_deck(self):
        """Create the deck made up of 52 cards"""

        # Card information
        suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                 '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

        # Creating the deck
        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)

    def shuffle(self):
        """Simulate shuffling the deck of cards"""
        random.shuffle(self.cards)


    def deal(self):
        """Simulate dealing a card; remove that card for that round"""

        # Return the last card in the deck
        card = self.cards.pop()
        return card


class Player():
    """Class to simulate the user playing Black Jack"""

    def __init__(self):
        """Initialize player attributes"""

        self.hand = []          # List to hold the player's hand
        self.hand_value = []    # Value of the player's hand
        self.playing = True     # Boolean to show if the player is still playing hand


    def draw(self, deck):
        """Simulate dealing the user a starting hand"""

        # Deal the player 2 cards
        for card in range(2):
            card = deck.deal()
            self.hand.append(card)


    def show_hand(self):
        """Display the player's current hand"""
        print("\nPlayer's Hand:")
        for card in self.hand:
            card.display_card()
        

    def hit(self, deck):
        """Deal the player a new card; simulating hitting in Black Jack"""
        card = deck.deal()
        self.hand.append(card)


    def set_hand_value(self):
        """Calculate the value of the player's hand"""
        self.hand_value = 0

        # Track if you have an ace in your hand
        have_ace = False

        for card in self.hand:
            self.hand_value += card.value
            # Check for Ace
            if card.rank == 'A':
                have_ace = True

        # User is allowed to use the ace as 11 or as 1
        if self.hand_value > 21 and have_ace:
            self.hand_value -= 10

        print("\nTotal value: " + str(self.hand_value)) 


    def update(self, deck):
        """Allow the user to continue hitting if below 21"""

        # Player can hit if the value is less than 21
        if self.hand_value < 21:
            choice = input("\nWould you like to hit (y/n): ").lower().strip()
            if choice == 'y':
                self.hit(deck)

            # Player chose not to hit even those they weren't at 21
            else:
                self.playing = False
                
        # Value is more than 21
        else:
            self.playing = False
        

class Dealer():
    """Class to simulate the dealer in the Black Jack game"""

    def __init__(self):
        """Initialize dealer attributes"""
        self.hand = []          # List to hold the dealers's hand
        self.hand_value = []    # Value of the dealers's hand
        self.playing = True     # Boolean to show if the dealer is still playing hand


    def draw(self, deck):
        """Simulate dealing the dealer a starting hand"""

        # Deal the dealer 2 cards
        for card in range(2):
            card = deck.deal()
            self.hand.append(card)


    def show_hand(self):
        """Display the dealer's hand one at a time"""

        input("\nPress (enter) to reveal the dealer's hand. ")

        # Show each card one at a time
        for card in self.hand:
            card.display_card()
            # Pauses the program for 1 second. Builds suspense for the user
            time.sleep(1)
            

    def hit(self, deck):
        """Simulate the dealer hitting. They must hit until they have reached a value of 17"""
        self.set_hand_value()

        # Dealer must keep hitting if the value is less than 17
        while self.hand_value < 17:
            card = deck.deal()
            self.hand.append(card)
            self.set_hand_value()

        print("\nDealer is set with a total of " + str(len(self.hand)) + " cards.")
            

    def set_hand_value(self):
        """Calculate the value of the dealer's hand"""
        self.hand_value = 0

        # Track if you have an ace in your hand
        have_ace = False

        for card in self.hand:
            self.hand_value += card.value
            # Check for Ace
            if card.rank == 'A':
                have_ace = True

        # User is allowed to use the ace as 11 or as 1
        if self.hand_value > 21 and have_ace:
            self.hand_value -= 10

    
class Game():
    """Class to simulate holding the game bets and payouts"""
    
    def __init__(self, money):
        """Initialize attributes"""

        self.money = int(money) # Amount of money the player has
        self.bet = 20           # Min bet must be 20
        self.winner = ""        # Start the game with no winner


    def get_bet(self):
        """Simulate a user's bet"""

        # Keep betting until the user makes an acceptable bet
        betting = True
        while betting:
            
            # Get user input for their bet
            bet = int(input("What would you like to bet (min bet of $20): "))

            # Min bet must be 20
            if bet < 20:
                bet = 20

            # The user does not have the amount of money they are trying to bet
            if bet > self.money:
                print("\nSorry, you cannot afford that bet.")
                
            # Bet is within range; stop betting
            else:
                self.bet = bet
                betting = False
                

    def score(self, player_score, dealer_score):
        """Score the round of Black Jack"""

        # User got Black Jack
        if player_score == 21:
            print("\nYou win! You got Blackjack!!!")
            self.winner = 'player'

        # Dealer got Black Jack
        elif dealer_score == 21:
            print("\nYou lose...the dealer got Blackjack.")
            self.winner = 'dealer'

        # User went over 21
        elif player_score > 21:
            print("\nYou lose...you went over 21.")
            self.winner = 'dealer'

        # Dealer went over 21
        elif dealer_score > 21:
            print("\nYou win! The dealer went over 21.")
            self.winner = 'player'

        else:
            # Player scores more
            if player_score > dealer_score:
                print("\nYou win! The dealer scored " + str(dealer_score) + ".")
                self.winner = 'player'
                
            # Dealer scores more
            elif dealer_score > player_score:
                print("\nYou lose...the dealer scored " + str(dealer_score) + ".")
                self.winner = 'dealer'

            # Tied score
            else:
                print("\nIt's a push...the dealer scored " + str(dealer_score) + ".")
                self.winner = 'tie'


    def payout(self):
        """Update the money based on who won the round"""

        # User won
        if self.winner == 'player':
            self.money += self.bet

        # User lost
        elif self.winner == 'dealer':
            self.money -= self.bet


    def show_money(self):
        """Display the current amount of money the user has in the game"""

        print("\nCurrent Money: $" + str(self.money))


    def show_money_and_bet(self):
        """Display the current bet and current money for the round"""

        print("\nCurrent Money: $" + str(self.money) + "\t\tCurrent Bet: $" + str(self.bet))

        

# The main code

# Welcome message for user
print("Welcome to the Blackjack Simulator.")
print("The minimum bet at this table is $20.")

# Create a game object. This keeps track of money, bets, winners, and payouts
money = int(input("\nHow much money are you willing to play with today: "))
game = Game(money)

# Main game loop
playing_game = True
while playing_game:

    # Build the deck and shuffle it
    game_deck = Deck()
    game_deck.create_deck()
    game_deck.shuffle()

    # Create the player and dealer objects
    player = Player()
    dealer = Dealer()

    # Display the amount of money the player has and allow them to bet
    game.show_money()
    game.get_bet()
    
    # Create the player and dealer hands
    player.draw(game_deck)
    dealer.draw(game_deck)

    # Show the money and the bet for the user
    game.show_money_and_bet()

    # Show the dealer's first card
    print("The dealer is showing a " + str(dealer.hand[0].rank) + " of " + str(dealer.hand[0].suit) + ".")

    # Simulate a single round for the player
    while player.playing:
        player.show_hand()
        player.set_hand_value()
        player.update(game_deck)

    # Simulate a single round for the dealer
    dealer.hit(game_deck)
    dealer.show_hand()

    # Figure out who won and what the payout is
    game.score(player.hand_value, dealer.hand_value)
    game.payout()

    # User ran out of money
    if game.money < 20:
        playing_game = False
        game.show_money()
        print("\nSorry, you are out of money. Come back later.")
        
    

