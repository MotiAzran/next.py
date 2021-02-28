class Animal(object):
    ZOO_NAME = "Hayathon"

    def __init__(self, name, hunger=0):
        self.__name = name
        self.__hunger = hunger

    def get_name(self):
        return self.__name

    def is_hungry(self):
        return self.__hunger > 0

    def feed(self):
        self.__hunger -= 1

    def talk(self):
        raise NotImplementedError()


class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Woof Woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self.__stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self.__color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky", 0),
               Unicorn("Keith", 7), Dragon("Lizzy", 1450),
               Dog("Doggo", 80), Cat("Kitty", 80), Skunk("Stinky Jr."), Unicorn("Clair", 80), Dragon("McFly", 80)]
    special_func = {Dog: "fetch_stick", Cat: "chase_laser", Skunk: "stink", Unicorn: "sing", Dragon: "breath_fire"}

    for animal in zoo_lst:
        if animal.is_hungry():
            print('{} {}'.format(type(animal).__name__, animal.get_name()))
            while animal.is_hungry():
                animal.feed()

        animal.talk()
        getattr(animal, special_func[type(animal)])()

    print(Animal.ZOO_NAME)


if __name__ == '__main__':
    main()
