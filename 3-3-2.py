class UnderAge(Exception):
    def __init__(self, age):
        super().__init__()
        self.__age = age

    def __str__(self):
        return "Your age is under 18. Now you are {} years old in {} year{} you will be 18".format(
            self.__age, 18 - self.__age, '' if (18 - self.__age) == 1 else 's')


def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print("You should send an invite to " + name)


def main():
    send_invitation("A", 20)

    try:
        send_invitation("B", 17)
    except UnderAge as e:
        print(e)


if __name__ == '__main__':
    main()