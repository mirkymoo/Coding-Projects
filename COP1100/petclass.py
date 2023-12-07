class Pet:
    def __init__(self, name, pet_type, age):
        self.name = name
        self.pet_type = pet_type
        self.age = age

    def setPetName(self,name):
        self.name = name

    def setPetType(self, pet_type):
        self.pet_type = pet_type

    def setPetAge(self, age):
        self.age = age

    def getPetName(self):
        return self.name

    def getPetAge(self):
        return self.age

    def getPetType(self):
        return self.pet_type


def main():
    pet_name = input('Please enter your pet\'s name: \n')
    pet_type = input('What animal is your pet? \n')
    pet_age = input('What is the age of your pet? \n')

    my_pet = Pet(pet_name,pet_type,pet_age)

    print('\nYou have a', my_pet.getPetAge(), 'year old pet', my_pet.getPetType(), 'named', my_pet.getPetName())
    
main()