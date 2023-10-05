# FOR EACH SECTION BELOW, YOU'LL NEED TO DELETE THE WORD "pass" TO BEGIN WORKING ON THAT SECTION OF THE CODE. "pass" IS ONLY THERE SO THAT BLOCK OF CODE DOESN'T PRODUCE AN ERROR WHILE YOU ARE WRITING THE CODE.
class Clone:
    def __init__(self, name, rank, planet):
        pass
        # TODO: Initialize the attributes for the Clone. There needs to be an attribute for: name, rank and planet.
        
    # TODO: Create a method to display the Clone's info in a readable format (this should output to the console.)


class Starship:
    def __init__(self, name, model, capacity):
        pass
        # TODO: Initialize the attributes for the Starship
    
    # TODO: Create a method to display the Starship's info in a readable format


class GalacticDatabase:
    def __init__(self):
        # TODO: Initialize empty lists to store Clone and Starship objects. I've done this one for you. You're safe to move on to the next #TODO. Remember [] is hour we create lists. In the next method down, you'll need to create a new object and add it to the list. 
        self.clones = []
        self.starships = []
        

    def add_clone(self, name, rank, planet):
        # TODO: Create a new Clone object and add it to the respective list (hint: use .append() method to add it to the list after you've created a new clone object)
        pass
    def add_starship(self, name, model, capacity):
        
        # TODO: Create a new Starship object and add it to the respective list (Hint: this should look very similar to the one above.)
        pass
    def view_clones(self):
        # TODO: Display information for all the clones stored in the database (Hint: Use a for loop here to print each item to the terminal. You should also use the method from the Clone class to disply the info.)
        pass
    def view_starships(self):
        # TODO: Display information for all the starships stored in the database
        pass
    # TODO: Additional methods to retrieve and display specific clone/starship details based on user input
    
# TODO: Implement user interaction to utilize the functionalities in the GalacticDatabase class