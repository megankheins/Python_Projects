# Epidemic Outbreak Simulation

import random

class Simulation():
    """A class to control the outbreak simulation; spreads the pretend disease"""

    def __init__(self):
        """Initialize attributes"""

        # Days the simulation has been running
        self.day_number = 1

        # Get simulation conditions from the user
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.pop_size = int(input("---Enter the population size: "))

        print("\nWe must first start by infecting a portion of the population.")
        self.infect_percent = float(input("---Enter the percentage (0-100) of the population to initially infect: "))
        self.infect_percent /= 100

        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infect_prob = float(input("---Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        
        print("\nWe must know how long the infection will last when exposed.")
        self.infect_duration = int(input("---Enter the duration (in days) of the infection: "))

        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = float(input("---Enter the mortality rate (0-100) of the infection: "))

        print("\nWe must know how long to run the simulation.")
        self.simulation_days = int(input("---Enter the number of days to simulate: "))
        

class Person():
    """A class to simulate an individual person in the population"""

    def __init__(self):
        """Initialize attributes"""

        # Person starts uninfected
        self.is_infected = False

        # Person starts alive
        self.is_dead = False

        # Keeps track of how many days a person is infected
        self.days_infected = 0


    def infect(self, simulation):
        """Simulate infected a person based on the simulation conditions"""

        # Randomly decide if they are infected based on the infection probability
        if random.randint(0,100) < simulation.infect_prob:
            self.is_infected = True


    def heal(self):
        """Simulate healing a person from infection"""
        self.is_infected = False
        self.days_infected = 0


    def die(self):
        """Simulate the person dying"""
        self.is_dead = True


    def update(self, simulation):
        """Update the individual person if they are not dead"""

        # Check if person is alive
        if not self.is_dead:
            # Check if person is infected
            if self.is_infected:
                self.days_infected += 1
                # Check if person will die
                if random.randint(0,100) < simulation.mortality_rate:
                    self.die()
                # Check how long the person has been infected
                elif self.days_infected == simulation.infect_duration:
                    self.heal()
                    
        
class Population():
    """A class to simulate a whole population of Person objects"""

    def __init__(self, simulation):
        """Initialize attributes"""

        # List to hold all Person instances
        self.population = []

        # Create the amount of Person instances based on the simulation conditions
        for i in range(simulation.pop_size):
            person = Person()
            self.population.append(person)


    def initial_infection(self, simulation):
        """Infect the initial percentage of the population based on conditions"""

        # Multiply the pop size by the infect percentage to get the infected count for this simulation
        # Round and turn into an integer for using in a for loop
        infected_count = int(round(simulation.infect_percent*simulation.pop_size, 0))

        # Infect the corrent amount of people
        for i in range(infected_count):
            # Infect the ith person in the population
            self.population[i].is_infected = True
            self.population[i].days_infected = 1

        # Shuffle the population list to spread the infection randomly
        random.shuffle(self.population)


    def spread_infection(self, simulation):
        """Simulate the infection spreading within the population.
        Infection can only spread to adjacent people in the list"""
        
        for i in range(len(self.population)):
            # Check if the ith person is alive and are able to be infected
            if self.population[i].is_dead == False:
                
                # First person in the list can only check to the right [i+1]
                if i == 0:
                    if self.population[i+1].is_infected:
                        self.population[i].infect(simulation)

                # Middle of the list can check to the left [i-1] and right [i+1]
                elif i < len(self.population)-1:
                    if self.population[i-1].is_infected or self.population[i+1].is_infected:
                        self.population[i].infect(simulation)

                # Last person in the list can only check to the left [i-1]
                elif i == len(self.population)-1:
                    if self.population[i-1].is_infected:
                        self.population[i].infect(simulation)


    def update(self, simulation):
        """Update the whole population by updating each individual Person instance"""

        # Update the simulation day number
        simulation.day_number += 1

        # Call update method for each Person instance
        for person in self.population:
            person.update(simulation)


    def display_stats(self, simulation):
        """Display the population statistics"""

        # Initialize values for infected and dead count
        total_infected = 0
        total_dead = 0

        # Loop through population
        for person in self.population:
            # Check if person is infected
            if person.is_infected:
                total_infected +=1
                # Check if person is dead
                if person.is_dead:
                    total_dead +=1

        # Calculate infected percentage and death percent
        infected_percent = round((total_infected / simulation.pop_size)*100, 4)
        death_percent = round((total_dead / simulation.pop_size)*100, 4)

        # Summary
        print("\n-----Day #" + str(simulation.day_number) + "-----")
        print("Percentage of Population Infected: " + str(infected_percent) + "%")
        print("Percentage of Population Dead: " + str(death_percent) + "%")
        print("Total People Infected: " + str(total_infected) + " / " + str(simulation.pop_size))
        print("Total Deaths: " + str(total_dead) + " / " + str(simulation.pop_size))


    def graphics(self):
        """Graphical representation of the population. X dead, O healthy, I infected."""

        # List to hold characters to represent each person in the population
        status = []

        for person in self.population:
            # Person is dead
            if person.is_dead:
                character = 'X'
            # Person is alive
            else:
                # Person is infected
                if person.is_infected:
                    character = 'I'
                # Person is healthy
                else:
                    character = 'O'
            status.append(character)

        # Print out status for each person
        for character in status:
            print(character, end= '-')


# The Main Code

# Create simulation and population objects
simulation = Simulation()
population = Population(simulation)

# Set the initial infection
population.initial_infection(simulation)

# Display the statistics
population.display_stats(simulation)

# Display graphics
population.graphics()

# User starts simulation
input("\nPress (Enter) to begin the simulation. ")

# Run simulation
for i in range(1, simulation.simulation_days):
    population.spread_infection(simulation)
    population.update(simulation)
    population.display_stats(simulation)
    population.graphics()

    # Pause after each day
    if i != simulation.simulation_days-1:
        input("\nPress (Enter) to advance to the next day.")


    
