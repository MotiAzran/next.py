from file1 import GreetingCard
from file2 import BirthdayCard


def main():
    birth_card = BirthdayCard()
    greet_card = GreetingCard()

    birth_card.greeting_msg()
    print()
    greet_card.greeting_msg()


if __name__ == '__main__':
    main()
