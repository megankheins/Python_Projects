# GUI Epidemic Outbreak

import math
import random
import tkinter

class Simulation():
    """A class to control the outbreak simulation; spreads the pretend disease"""

    def __init__(self):
        """Initialize attributes"""

        # Days the simulation has been running
        self.day_number = 1

        # Get simulation conditions from the user
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.pop_size = int(input("---Enter the population size: "))

        # Convert the population to a perfect square for the visuals
        root = math.sqrt(self.pop_size)

        # User did not enter a perfect square
        if int(root + 0.5)**2 != self.pop_size:
            root = round(root, 0)
            self.grid_size = int(root)
            self.pop_size = self.grid_size**2
            print("Rounding population size to " + str(self.pop_size) + " for visual purposes.")

        # User did enter a perfect square
        else:
            self.grid_size = int(math.sqrt(self.pop_size))

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

        self.population = []    # List to hold all Person instances. A list of N lists: NxN objects (N is grid size)

        # Loop through the needed number of rows
        for i in range(simulation.grid_size):
            row = []
            # Loop through the needed number of Person instances per row
            for j in range(simulation.grid_size):
                person = Person()
                row.append(person)
            # Add the row to the population
            self.population.append(row)
        

    def initial_infection(self, simulation):
        """Infect the initial percentage of the population based on conditions"""

        # Multiply the pop size by the infect percentage to get the infected count for this simulation
        # Round and turn into an integer for using in a for loop
        infected_count = int(round(simulation.infect_percent*simulation.pop_size, 0))

        # Infect the correct amount of people
        infections = 0
        while infections < infected_count:
            # x is a random row in the population, y is a random person in the row
            x = random.randint(0, simulation.grid_size-1)
            y = random.randint(0, simulation.grid_size-1)
            
            # Check if the person is not infected
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1


    def spread_infection(self, simulation):
        """Simulate the infection spreading within the population. Infection can only spread to adjacent people in the 2D array."""

        # Loop through all of the rows in the population
        for i in range(simulation.grid_size):
            # Loop through all of the Person instances in the row
            for j in range(simulation.grid_size):
                # Check if the person is alive and able to be infected
                if self.population[i][j].is_dead == False:

                    # First row. Cannot look above
                    if i == 0:
                        # First column of first row. Cannot look left
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        # Last column of first row. Cannot look right
                        elif j == simulation.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        # All other columns in row can look left, right, and below
                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)

                    # Last row. Cannot look below
                    elif i == simulation.grid_size-1:
                        # First column of last row. Cannot look left
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        # Last column of last row. Cannot look right
                        elif j == simulation.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        # All other columns in row can look left, right, and above
                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)

                    # Middle rows
                    else:
                        # First column of middle rows. Cannot look left
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        # Last column of middle rows. Cannot look right
                        elif j == simulation.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        # All other columns in middle rows can look left, right, above, and below
                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
               
           
    def update(self, simulation):
        """Update the whole population by updating each individual Person instance"""

        # Update the simulation day number
        simulation.day_number += 1

        # Call update method for each Person instance
        for row in self.population:
            for person in row:
                person.update(simulation)


    def display_stats(self, simulation):
        """Display the population statistics"""

        # Initialize values for infected and dead count
        total_infected = 0
        total_dead = 0

        # Loop through population
        for row in self.population:
            for person in row:
                # Check if person is infected
                if person.is_infected:
                    total_infected += 1
                    # Check if person is dead
                    if person.is_dead:
                        total_dead += 1

        # Calculate infected percentage and death percent
        infected_percent = round((total_infected / simulation.pop_size)*100, 4)
        death_percent = round((total_dead / simulation.pop_size)*100, 4)

        # Summary
        print("\n-----Day #" + str(simulation.day_number) + "-----")
        print("Percentage of Population Infected: " + str(infected_percent) + "%")
        print("Percentage of Population Dead: " + str(death_percent) + "%")
        print("Total People Infected: " + str(total_infected) + " / " + str(simulation.pop_size))
        print("Total Deaths: " + str(total_dead) + " / " + str(simulation.pop_size))


# Helper function to create the graphics

def graphics(simulation, population, canvas):
    """Helper function to update the tkinter display"""

    # Get the dimensions of an individual square in the grid (representing 1 person)
    # GUI window is 600x600
    sq_dimension = 600//simulation.grid_size

    # Loop through population
    for i in range(simulation.grid_size):
        # y = starting index of where the square should be drawn
        y = i*sq_dimension
        for j in range(simulation.grid_size):
            # x = starting index of where the square should be drawn
            x = j*sq_dimension
            # Check if person is dead
            if population.population[i][j].is_dead:
                # Dead: Make the square red
                canvas.create_rectangle(x, y, x+sq_dimension, y+sq_dimension, fill='red')
            # Not dead, check if they are infected
            else:
                if population.population[i][j].is_infected:
                    # Infected: Make the square yellow
                    canvas.create_rectangle(x, y, x+sq_dimension, y+sq_dimension, fill='yellow')
                else:
                    # Healthy: Make the square green
                    canvas.create_rectangle(x, y, x+sq_dimension, y+sq_dimension, fill='green')


# The Main Code

# Create simulation object
simulation = Simulation()

# Set window size
window_width = 600
window_height = 600

# Create tkinter window and canvas
simulation_window = tkinter.Tk()
simulation_window.title('Epidemic Outbreak')
simulation_canvas = tkinter.Canvas(simulation_window, width=window_width, height=window_height, bg='lightblue')
simulation_canvas.pack(side=tkinter.LEFT)

# Create population object
population = Population(simulation)

# Set the initial infection
population.initial_infection(simulation)

# Display the statistics
population.display_stats(simulation)

input("Press (Enter) to begin the simulation. ")

# Run the simulation
for i in range(1, simulation.simulation_days):
    population.spread_infection(simulation)
    population.update(simulation)
    population.display_stats(simulation)
    graphics(simulation, population, simulation_canvas)

    # Update the tkinter window
    simulation_window.update()

    # Wipe the canvas clean after each day
    if i != simulation.simulation_days-1:
        simulation_canvas.delete('all')
        
