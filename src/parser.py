class InputParser:
    def __init__(self) -> None:
        pass

    def parse_file(self, path):
        print('opening', path)
        f = open(path, "r")
        print(f.read())


if __name__ == '__main__':
    parser = InputParser()
    parser.parse_file('input.txt')