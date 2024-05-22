class House:
    def __init__(self):
        self.numberOfFloors = 0

    def set_new_numbers_of_floors(self, floor = None):
        if floor is not None:
            self.numberOfFloors += floor
            print('Ваш этаж:', self.numberOfFloors)



my_house = House()
my_house.set_new_numbers_of_floors(5)