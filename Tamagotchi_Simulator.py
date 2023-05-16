
import random


class Tamagotchi():
    """Simulates the game of Tamagotchi"""


    def __init__(self, name):
        """Initialize attributes"""
        
        self.name = name.title()

        # Track creature score throughout the game
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        # Food inventory, if creature is awake, if creature is alive
        self.food = 2
        self.awake = True
        self.alive = True


    def eat(self):
        """Simulates the creature eating"""

        # Take one food piece away each time the creature eats
        if self.food > 0:
            self.food -= 1
        
            # Take a random hunger value away
            pieces = random.randint(1,4)
            self.hunger -= pieces
            if self.hunger < 0:
                self.hunger = 0
            print("Yum! " + self.name + " ate a great meal!")

        else:
            print(self.name + " doesn't have any food left. You need to forage!")
        
    def play(self):
        """Play a game to lower the creatures boredom level"""
        
        print("\n" + self.name + " wants to play a game.")
        print(self.name + " is thinking of a number 0, 1, or 2.")
        number = random.randint(0,2)
        guess = int(input("What is your guess: "))

        # If they guess correct, lower the boredom level more
        if guess == number:
            print("You guessed correct!")
            self.boredom -= 3

        else:
            print("WRONG. The number " + self.name + " was thinking of is " + str(number) + ".")
            self.boredom -= 1

        # Make sure boredom is not less than 0    
        if self.boredom < 0:
            self.boredom = 0


    def sleep(self):
        """Simulate creature sleeping"""

        # Player can only try to wake creature up when they are sleeping; no other actions can be completed
        self.awake = False

        # Tiredness and boredom decrease each round the creature sleeps
        self.tiredness -= 3
        self.boredom -= 2
        print("Zzzz....Zzzz....Zzzz....")

        # Make sure boredom and tiredness are not less than 0
        if self.boredom < 0:
            self.boredom = 0
        if self.tiredness < 0:
            self.tiredness = 0


    def wake_up(self):
        """Simulate randomly waking the creature up"""

        # Random selection; 0 means they wake up
        wakes_up = random.randint(0,2)

        # Creature wakes up
        if wakes_up == 0:    
            self.awake = True
            print(self.name + " just woke up.")
            self.tiredness = 0

        # Creature still sleeping
        else:
            print(self.name + " won't wake up right now ... still sleepy.")
            self.sleep()
            

    def clean(self):
        """Simulate the creature bathing"""

        self.dirtiness = 0
        print(self.name + " has taken a bath. YAY")


    def forage(self):
        """Simulate the creature foraging for food"""

        # Creature finds a random amount of food
        pieces = random.randint(0,4)
        self.food += pieces
        print(self.name + " found " + str(pieces) + " pieces of food.")

        # Creature gets dirty looking for food
        self.dirtiness += 2

    def display_values(self):
        """Show the creature's current values and information"""

        print("\nCreature Name: " + self.name)
        print("Hunger (0-10): " + str(self.hunger))
        print("Boredom (0-10): " + str(self.boredom))
        print("Tiredness (0-10): " + str(self.tiredness))
        print("Dirtiness (0-10): " + str(self.dirtiness))

        print("\nFood Inventory: " + str(self.food) + " pieces")

        if self.awake:
            print("Current Status: Awake")
        else:
            print("Current Status: Sleeping")


    def increase_values(self, difficulty):
        """Update the creature values based on the chosen difficulty"""

        # Increase boredom and tiredness only if creature is awake
        if self.awake == True:
            self.boredom += random.randint(0,difficulty)
            self.tiredness += random.randint(0,difficulty)

        # Increase hunder and dirtiness even if they are sleeping
        self.hunger += random.randint(0,difficulty)
        self.dirtiness += random.randint(0,difficulty)
        

    def kill(self):
        """Check if any values are out of range and kill the creature if necessary"""

        # Creature can die of hunger or dirtiness
        if self.hunger >= 10:
            print("\n" + self.name + " has starved to death...")
            self.alive = False
        elif self.dirtiness >= 10:
            print("\n" + self.name + " has suffered an infection and died.")
            self.alive = False

        # Creature does not die of boredom or tiredness, just falls asleep
        elif self.boredom >= 10:
            self.boredom = 10
            print("\n" + self.name + " is bored and falling asleep...")
            self.awake = False
        elif self.tiredness >= 10:
            self.tiredness = 10
            print("\n" + self.name + " is sleepy and falling asleep...")
            self.awake = False


# Helper function: outside of the Creature Class

def menu(creature):
    """Show the game menu options"""

    # If the creature is sleeping, the user can only try to wake them up
    if creature.awake == False:
        choice = input("\nEnter (6) to try to wake up: ")
        # Make sure the choice is hard coded to 6 in case they try to select something else
        choice = '6'

    # If the creature is awake, the user can select from all options
    else:
        print("\nEnter (1) to eat.")
        print("Enter (2) to play.")
        print("Enter (3) to sleep.")
        print("Enter (4) to take a bath.")
        print("Enter (5) to forage for food.")
        choice = input("What is your choice: ")

    return choice
    

def action(creature, choice):
    """Call the correct action based on the user's choice"""
    
    if choice == '1':
        creature.eat()
    elif choice == '2':
        creature.play()
    elif choice == '3':
        creature.sleep()
    elif choice == '4':
        creature.clean()
    elif choice == '5':
        creature.forage()
    elif choice == '6':
        creature.wake_up()
    else:
        print("That is not a valid option.")


# The main code

print("Welcome to the Tamagotchi Simulator")

# User input for difficulty level
my_difficulty = int(input("Please choose your difficulty level (1-5): "))
if my_difficulty > 5:
    my_difficulty = 5
elif my_difficulty < 1:
    my_difficulty = 1

# Main game loop
playing = True
while playing:

    # Get user input for name
    pet_name = input("\nWhat name would you like to give your pet Tamagotchi: ").strip()
    my_pet = Tamagotchi(pet_name)

    # Keep track of the game round
    game_round = 1

    # Game loop simulating a single round
    while my_pet.alive:

        print("\n----------------------------------------------------------------------------------")
        print("Round #" + str(game_round))

        # Display values, allow user to select move, and call the correct action
        my_pet.display_values()
        select_choice = menu(my_pet)
        action(my_pet, select_choice)

        # Show the round summary
        print("\nRound #" + str(game_round) + " Summary:")
        my_pet.display_values()
        input("\nPress (enter) to continue...")

        # Increase creature's values
        my_pet.increase_values(my_difficulty)

        # Check if the creature should die
        my_pet.kill()

        # Next game round
        game_round += 1

    print("\nR.I.P.")
    print(my_pet.name + " survived a total of " + str(game_round - 1) + " rounds.")

    # Ask the user if they want to play again
    play_again = input("\nWould you like to play again (y/n): ").lower().strip()
    if play_again != 'y':
        playing = False
        print("\nThank you for playing!")


