def raise_stop_iteration():
    raise StopIteration()


def raise_zero_division_error():
    x = 5 / 0


def raise_assertion_error():
    assert False


def raise_import_error():
    import unreal_module


def raise_key_error():
    x = {'a': 1}['b']


def raise_syntax_error():
    raise SyntaxError()


def raise_indentation_error():
    raise IndentationError()


def raise_type_error():
    x = 5 + '5'


def main():
    try:
        raise_stop_iteration()
    except StopIteration:
        print("Got StopIteration")

    try:
        raise_zero_division_error()
    except ZeroDivisionError:
        print("Got ZeroDivisionError")

    try:
        raise_assertion_error()
    except AssertionError:
        print("Got AssertionError")

    try:
        raise_import_error()
    except ImportError:
        print("Got ImportError")

    try:
        raise_key_error()
    except KeyError:
        print("Got KeyError")

    try:
        raise_syntax_error()
    except SyntaxError:
        print("Got SyntaxError")

    try:
        raise_indentation_error()
    except IndentationError:
        print("Got IndentationError")

    try:
        raise_type_error()
    except TypeError:
        print("Got TypeError")


if __name__ == '__main__':
    main()