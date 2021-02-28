import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_place):
        super().__init__()
        self.__illegal_place = illegal_place

    def __str__(self):
        return "The username contains an illegal character at {}".format(self.__illegal_place)


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __init__(self, char_type):
        self.__char_type = char_type

    def __str__(self):
        return "The password is missing a character ({})".format(self.__char_type)


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


def check_username(username):
    if len(username) < 3:
        raise UsernameTooShort()

    if len(username) > 16:
        raise UsernameTooLong()

    allowed_chars = string.ascii_letters + string.digits + '_'
    for i, c in enumerate(username):
        if c not in allowed_chars:
            raise UsernameContainsIllegalCharacter(i)

    return True


def check_password(password):
    if len(password) < 8:
        raise PasswordTooShort()

    if len(password) > 40:
        raise PasswordTooLong()

    if len([c for c in password if c in string.ascii_uppercase]) == 0:
        raise PasswordMissingCharacter('Uppercase')
    if len([c for c in password if c in string.ascii_lowercase]) == 0:
        raise PasswordMissingCharacter('Lowercase')
    if len([c for c in password if c in string.digits]) == 0:
        raise PasswordMissingCharacter('Digit')
    if len([c for c in password if c in string.punctuation]) == 0:
        raise PasswordMissingCharacter('Special')

    return True


def check_input(username, password):
    if check_username(username) and check_password(password):
        print("OK")


def main():
    try:
        check_input("1", "2")
    except UsernameTooShort as e:
        print(e)

    try:
        check_input("0123456789ABCDEFG", "2")
    except UsernameTooLong as e:
        print(e)

    try:
        check_input("A_a1.", "12345678")
    except UsernameContainsIllegalCharacter as e:
        print(e)

    try:
        check_input("A_1", "2")
    except PasswordTooShort as e:
        print(e)

    try:
        check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    except PasswordTooLong as e:
        print(e)

    try:
        check_input("A_1", "abcdefghijklmnop")
    except PasswordMissingCharacter as e:
        print(e)

    try:
        check_input("A_1", "ABCDEFGHIJLKMNOP")
    except PasswordMissingCharacter as e:
        print(e)

    try:
        check_input("A_1", "ABCDEFGhijklmnop")
    except PasswordMissingCharacter as e:
        print(e)

    try:
        check_input("A_1", "4BCD3F6h1jk1mn0p")
    except PasswordMissingCharacter as e:
        print(e)

    check_input("A_1", "4BCD3F6.1jk1mn0p")


if __name__ == '__main__':
    main()