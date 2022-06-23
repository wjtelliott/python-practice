
class Car:
    def __init__(self, name, max_speed) -> None:
        self.name = name
        self.max_speed = max_speed
    
    def start(_) -> None: print('Vroom!')

    def talk(self, driver) -> None:
        print('Hello, {driver_name}, I am {self_name}!'
            .format(driver_name = driver, self_name = self.name))

class Driver:
    number_of_drivers = 0
    average_ranking = 0
    def __init__(self, name, age, ranking) -> None:
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1
        Driver.average_ranking = (Driver.average_ranking + self.ranking) / Driver.number_of_drivers


race_return_anno = {
    "add_driver": {
        "type": "int",
        "docstring": "Will return 1 if driver is succesfully added, and 0 if the driver was not added"
    },
    "get_average_ranking": {
        "type": "number",
        "docstring": "Will return average of all drivers within the race as int or double"
    },
    "add_driver_many": {
        "return": "int",
        "type": "int",
        "docstring": "Will return 0 if reached maximum driver limit. Will return 1 if at least one driver was added"
    }
}

class Race:
    def __init__(self, name, driver_limit, drivers = []) -> None:
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = drivers
    
    def add_driver(self, new_driver: Driver) -> race_return_anno['add_driver']:
        if Driver.number_of_drivers > self.driver_limit: return 0
        if new_driver.ranking > self.get_average_ranking() + 10: return 0
        self.drivers.append(new_driver)
        return 1

    def add_many_drivers(self, *drivers) -> race_return_anno['add_driver_many']:
        for driver in drivers:
            # if Driver.number_of_drivers > self.driver_limit: return 0
            if driver.ranking > self.get_average_ranking() + 10: continue
            self.drivers.append(driver)
        return 1

    def get_average_ranking(self) -> race_return_anno['get_average_ranking']:
        if len(self.drivers) <= 0: return 0
        result = 0
        for i in self.drivers:
            result += i.ranking
        return result / len(self.drivers)

    def show_drivers(self) -> None:
        print('Drivers:')
        for i in self.drivers: print('\t', i.name)
    
        
myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)

myCar.talk('asd')

jerry = Driver('Jerry', 24, 6)
john = Driver('John', 22, 14)
jacob = Driver('Jacob `Lightning`', 19, 1)

print('Averages: ', jacob.number_of_drivers)

slowy = Driver('Slowy', 91, 28)

print('Averages: ', slowy.average_ranking)

big_race = Race('Big one', 4)

# big_race.add_driver(jerry)
# big_race.add_driver(john)
# big_race.add_driver(jacob)
# big_race.add_driver(slowy)

big_race.add_many_drivers(jerry, john, jacob, slowy)
big_race.add_many_drivers()

big_race.show_drivers();

print('Average Race Ranking:', big_race.get_average_ranking())