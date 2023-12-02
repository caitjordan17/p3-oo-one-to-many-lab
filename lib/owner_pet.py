class Pet:
    
    all = []
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner="None"):
        if pet_type in Pet.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            Pet.all.append(self)
            self._owner = owner
        else:
            raise TypeError("Pet not a valid type")
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if isinstance(value, Owner):
            self._owner = value


class Owner:
    def __init__(self, name):
        self.name = name
        print("name in owner:", name)

    def pets(self):
        return [pet for pet in Pet.all if pet.owner.name == self.name]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError("Pet not valid pet")

    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet: pet.name)


# owner = Owner("Ben")
# print("owner:", owner)
# print("owner.name:", owner.name)
# print("owner pets:", owner.pets())

# pet = Pet("Whiskers", "cat")
# print("pet.owner:", pet.owner)
# print("pet:", pet)
# print("ispet?", isinstance(pet, Pet))

# owner.add_pet(pet)
# print("pet after add:", pet)
# print("pet's owner after add:", pet.owner.name)

# owner = Owner("John")
# pet1 = Pet("Fido", "dog", owner)
# pet2 = Pet("Clifford", "dog", owner)
# pet3 = Pet("Whiskers", "cat", owner)
# pet4 = Pet("Jerry", "reptile", owner)
# print("owner's pets:", owner.pets)
# print("sorted:", owner.get_sorted_pets())