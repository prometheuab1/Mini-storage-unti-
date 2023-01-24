import Lab8_Prob1

#main method
def main():
    #display program reason to user.
    print('-------------------------------------------------------------------')
    print('This program is going to ask the user to enter animal species, location,weight, endangered and then display back to user')
    print('--------------------------------------------------------------------')

    species = input('Animal species: ')
    location = input('Animal location: ')
    weight = int(input(f'The weight of {species}: '))
    endangered = input('Is this specie endangered? Yes or No: ')


    print('---------------------------------------------')
    Student1 = Lab8_Prob1.Student(species, location,weight, endangered)
    
    print(f'This specie is a {Student1.get_species()}')
    print(f'Specie location is {Student1.get_location()}')
    print(f'Specie weight is {Student1.get_weight()}')
    print(f'Is {species} ? {Student1.get_endangered()}')
    print('-------------------')
    print(Student1)

    
    
#call main
main()
