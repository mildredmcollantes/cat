import sys


def main():
    args = sys.argv[1:]
    for x in args:
        # print(x)
        file_contents = ""
        if x == ">":
            output = args[x+1]
            _write_file(output, file_contents)
            break
        with open(x) as file:
            file_contents = file.read()
            print(file_contents)


def _write_file(output, file_contents):
    with open(output) as file:
        file.write(file_contents)


if __name__ == "__main__":
    main()