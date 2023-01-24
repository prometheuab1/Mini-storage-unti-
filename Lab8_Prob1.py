#This program is written by Abdulbasit Adeniji on 12/5/2022 for CIS 105 Lab 8.
#The program will create an object of classes created and prompts user to enter the species, location, weight and
#endangered (true/false).

#create the Blueprint to our object
class Student:
    #constructor
    def __init__(self, species, location,weight, endangered):
        self.species = species
        self.location = location
        self.weight = weight
        self.endangered = endangered

    #define our method. / get
    def get_species(self):
        return self.species
    def get_location(self):
        return self.location
    def get_weight(self):
        return self.weight
    def get_endangered(self):
        return self.endangered


        #setters/mutators
    def set_species(self, species):
        self.species = species

    def set_location(self, location):
        self.location = location
            
    def set_weight(self, weight):
        self.weight = weight
            
    def set_endangered (self, endangered):
        self.endangered = endangered

    def __str__(self):
        return 'This specie is ' +str(self.species)+', the species location is '+ str(self.location)+ ' the specie weight '+str(self.weight)+' and the specie endanger status is ' +str(self.endangered) 


