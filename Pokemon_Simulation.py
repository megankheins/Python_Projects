
import random

# Parent Class

class Pokemon():
    """A model for a generic Pokemon character"""

    def __init__(self, name, element, health, speed):
        """Initialize attributes"""

        self.name = name.title()
        self.element = element

        # Max health will be important for knowing what the character can heal to
        self.current_health = health
        self.max_health = health
        
        self.speed = speed
        self.is_alive = True


    def light_attack(self, enemy):
        """Simulates a light attack; will always do minimal damage at least"""
        # All pokemon will have a list moves = [light, heavy, restore, special]
        # All light attacks will appear at index 0 in the list

        damage = random.randint(15, 25)

        print("Pokemon " + self.name + " used " + self.moves[0] + ".")
        print("It dealt " + str(damage) + " damage.")

        # Deal damage
        enemy.current_health -= damage


    def heavy_attack(self, enemy):
        """Simulates a heavy attack; could do heavy damage or no damage at all"""
        # All pokemon will have a list moves = [light, heavy, restore, special]
        # All heavy attacks will appear at index 1 in the list
        
        damage = random.randint(0,50)

        print("Pokemon " + self.name + " used " + self.moves[1] + ".")

        # Dealt no damage
        if damage < 10:
            print("The attack missed!")
        else:       
            print("It dealt " + str(damage) + " damage.")
        
            # Deal damage
            enemy.current_health -= damage

        
    def restore(self):
        """Simulates a healing move to restore our current health"""
        # All pokemon will have a list moves = [light, heavy, restore, special]
        # All restore moves will appear at index 2 in the list
        
        # Generate the restore value
        heal = random.randint(15, 25)

        print("Pokemon " + self.name + " used " + self.moves[2] + ".")
        print("It healed " + str(heal) + " health points.")

        # Add health points
        self.current_health += heal

        # Check if over the max health
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        

    def faint(self):
        """Pokemon faints if you run out of health"""

        if self.current_health <= 0:
            self.is_alive = False
            print("Pokemon " + self.name + " has fainted!")
            input("Press 'Enter' to continue. ")


    def view_stats(self):
        """Show the pokemon's current stats"""
        print("\nName: " + self.name)
        print("Element Type: " + self.element)
        print("Health: " + str(self.current_health) + " / " + str(self.max_health))
        print("Speed: " + str(self.speed))
    

# Child Classes

class Fire(Pokemon):
    """A Fire type Pokemon; child of the Pokemon parent class"""

    def __init__(self, name, element, health, speed):
        "Inititalize attributes from the Pokemon class"""

        super().__init__(name, element, health, speed)

        # Fire type moves list
        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast']


    def special_attack(self, enemy):
        """FIRE BLAST: an elemental FIRE move"""
        # Massive damage to grass type, normal damage to fire type, minimal damage to water type

        print("Pokemon " + self.name + " used " + self.moves[3].upper() + "!")

        # Damage based on enemy pokemon type
        if enemy.element == 'GRASS':
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == 'WATER':
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10,30)

        # Deal the damage
        print("It dealt " + str(damage) + " damage.")
        enemy.current_health -= damage


    def move_info(self):
        "Show pokemon move information"""
        print("\n" + self.name + " Moves: ")

        # Light attack
        print("-- " + self.moves[0] + " --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # Restore move
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pokemon 15 to 25 damage points.")

        # Special attack
        print("-- " + self.moves[3] + " --")
        print("\tA powerful FIRE based attack...")
        print("\tGuaranteed to deal MASSIVE damage to GRASS type Pokemon.")


class Water(Pokemon):
    """A Water type Pokemon; child of the Pokemon parent class"""

    def __init__(self, name, element, health, speed):
        "Inititalize attributes from the Pokemon class"""

        super().__init__(name, element, health, speed)

        # Water type moves list
        self.moves = ['Bite', 'Splash', 'Dive', 'Water Cannon']


    def special_attack(self, enemy):
        """WATER CANNON: an elemental WATER move"""
        # Massive damage to fire type, normal damage to water type, minimal damage to grass type

        print("Pokemon " + self.name + " used " + self.moves[3].upper() + "!")

        # Damage based on enemy pokemon type
        if enemy.element == 'FIRE':
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == 'GRASS':
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10,30)

        # Deal the damage
        print("It dealt " + str(damage) + " damage.")
        enemy.current_health -= damage


    def move_info(self):
        "Show pokemon move information"""
        print("\n" + self.name + " Moves: ")

        # Light attack
        print("-- " + self.moves[0] + " --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # Restore move
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pokemon 15 to 25 damage points.")

        # Special attack
        print("-- " + self.moves[3] + " --")
        print("\tA powerful WATER based attack...")
        print("\tGuaranteed to deal MASSIVE damage to FIRE type Pokemon.")

        
class Grass(Pokemon):
    """A Grass type Pokemon; child of the Pokemon parent class"""

    def __init__(self, name, element, health, speed):
        "Inititalize attributes from the Pokemon class"""

        super().__init__(name, element, health, speed)

        # Grass type moves list
        self.moves = ['Vine Whip', 'Wrap', 'Grow', 'Leaf Blade']


    def special_attack(self, enemy):
        """LEAF BLADE: an elemental GRASS move"""
        # Massive damage to water type, normal damage to grass type, minimal damage to fire type

        print("Pokemon " + self.name + " used " + self.moves[3].upper() + "!")

        # Damage based on enemy pokemon type
        if enemy.element == 'WATER':
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == 'FIRE':
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10,30)

        # Deal the damage
        print("It dealt " + str(damage) + " damage.")
        enemy.current_health -= damage


    def move_info(self):
        "Show pokemon move information"""
        print("\n" + self.name + " Moves: ")

        # Light attack
        print("-- " + self.moves[0] + " --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # Restore move
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pokemon 15 to 25 damage points.")

        # Special attack
        print("-- " + self.moves[3] + " --")
        print("\tA powerful GRASS based attack...")
        print("\tGuaranteed to deal MASSIVE damage to WATER type Pokemon.")


# Game Class

class Game():
    """A game object to simulate the creation of pokemon and battles"""

    def __init__(self):
        """Intialize attributes"""

        self.pokemon_elements = ['FIRE', 'WATER', 'GRASS']
        # Names are not connect to the element type in this game
        self.pokemon_names = ['Charizard', 'Flareon', 'Arcanine', 'Cyndaquil',
                              'Squirtle', 'Gyarados', 'Vaporeon', 'Floatzel',
                              'Bulbasaur', 'Venusaur', 'Leafeon', 'Exeggutor']
        self.battles_won = 0


    def create_pokemon(self):
        """Randomly create a Pokemon"""

        # Randomly assign health and speed values
        health = random.randint(70,100)
        speed = random.randint(1,10)

        # Randomly assign an element and name
        name = self.pokemon_names[random.randint(0, len(self.pokemon_names)-1)]
        if name == 'Charizard' or name == 'Flareon' or name == 'Arcanine' or name == 'Cyndaquil':
            element = 'FIRE'
        elif name == 'Squirtle' or name == 'Gyarados' or name == 'Vaporeon' or name == 'Floatzel':
            element = 'WATER'
        else:
            element = 'GRASS'

        # Create the right elemental pokemon
        if element == 'FIRE':
            pokemon = Fire(name, element, health, speed)
        elif element == 'WATER':
            pokemon = Water(name, element, health, speed)
        else:
            pokemon = Grass(name, element, health, speed)

        return pokemon


    def choose_pokemon(self):
        """A method to simulate choosing your starting Pokemon"""

        # A list to hold 3 starter pokemon
        starters = []
        
        while len(starters) < 3:
            # Make a starter pokemon
            pokemon = self.create_pokemon()
            # Bool to see if the pokemon is unique
            valid_pokemon = True
            for starter in starters:
                # Check to see if there is a pokemon with that name or element in the list
                if starter.name == pokemon.name or starter.element == pokemon.element:
                    valid_pokemon = False
            # Add the unique pokemon to the list
            if valid_pokemon:
                starters.append(pokemon)

        # Show the starter pokemon
        for pokemon in starters:
            pokemon.view_stats()
            pokemon.move_info()

        # Present the user with the choice of their pokemon
        print("\nProfessor Eramo presents you with three Pokemon:")
        print("(1) - " + starters[0].name)
        print("(2) - " + starters[1].name)
        print("(3) - " + starters[2].name)
        choice = int(input("Which Pokemon would you like to choose: "))

        # Assign users selected pokemon
        pokemon = starters[choice-1]

        return pokemon


    def get_attack(self, pokemon):
        """User selects an attack"""

        # Print move options
        print("\nWhat would you like to do...")
        print("(1) - " + pokemon.moves[0])
        print("(2) - " + pokemon.moves[1])
        print("(3) - " + pokemon.moves[2])
        print("(4) - " + pokemon.moves[3])

        # Get user choice
        choice = int(input("Please enter your move choice: "))

        # Formatting
        print()
        print("---------------------------------------------------------")

        return choice


    def player_attack(self, move, player, enemy):
        """Attack the computer AI"""

        # Call the attack method based on the user's choice
        if move == 1:
            player.light_attack(enemy)
        elif move == 2:
            player.heavy_attack(enemy)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(enemy)

        # Check to see if the enemy fainted
        enemy.faint()


    def enemy_attack(self, player, enemy):
        """Randomly select a move for the enemy"""

        # Randomly assign a move
        move = random.randint(1,4)

        # Call the attack method based on the randomly assigned move
        if move == 1:
            enemy.light_attack(player)
        elif move == 2:
            enemy.heavy_attack(player)
        elif move == 3:
            enemy.restore()
        elif move == 4:
            enemy.special_attack(player)

        # Check to see if the player fainted
        player.faint()


    def battle(self, player, enemy):
        """Simulate a round of battle. Faster Pokemon go first"""

        # Get player's move
        move = self.get_attack(player)

        # Player goes first if their pokemon is faster
        if player.speed >= enemy.speed:
            self.player_attack(move, player, enemy)

            # Check if enemy is still alive
            if enemy.is_alive:
                self.enemy_attack(player, enemy)

        # Player goes second if their pokemon is slower
        else:
            self.enemy_attack(player, enemy)

            # Check if player is still alive
            if player.is_alive:
                self.player_attack(move, player, enemy)
        

# The Main Code

# Introduction
print("Welcome to Pokemon")
print("Can you become the world's greatest Pokemon Trainer?")
print("\nDon't worry! Professor Eramo is here to help you on your quest.")
print("He would like to gift you your first Pokemon!")
print("Here are three potential Pokemon partners.")
input("Press (Enter) to choose your Pokemon! ")

# The main game loop
playing_main = True
while playing_main:
    game = Game()

    # User chooses starter pokemon
    player = game.choose_pokemon()
    print("\nCongrats Trainer, you have chosen " + player.name + "!")
    input("\nYour journey with " + player.name + " begins now... Press (Enter). ")

    # Continue battling while user's pokemon is alive
    while player.is_alive:
        # Create the enemy pokemon
        enemy = game.create_pokemon()
        print("\nOh no! A wild " + enemy.name + " has approached!")
        enemy.view_stats()

        # Engage in battle while enemy and player pokemon are alive
        while enemy.is_alive and player.is_alive:
            game.battle(player, enemy)
            # Both players survived the round, show their current stats
            if enemy.is_alive and player.is_alive:
                player.view_stats()
                enemy.view_stats()
                # Formatting
                print("---------------------------------------------------------")

        # If player survived the battle against the enemy, increase the battles_won
        if player.is_alive:
            game.battles_won += 1

    # The player has fainted
    print("\nPoor " + player.name + " has fainted...")
    print("They defeated " + str(game.battles_won) + " Pokemon!")

    # Allow user to play again
    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        playing_main = False
        print("\nThank you for playing Pokemon!")

