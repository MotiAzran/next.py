def read_file(file_name):
    data = ''
    f = None

    try:
        f = open(file_name, 'r')
    except IOError:
        data = "__NO_SUCH_FILE__"
    else:
        data = f.read()
    finally:
        return '\n'.join(["__CONTENT_START__", data, "__CONTENT_END__"])


def main():
    print(read_file('file_not_exists.txt'))
    print(read_file('names.txt'))


if __name__ == '__main__':
    main()
