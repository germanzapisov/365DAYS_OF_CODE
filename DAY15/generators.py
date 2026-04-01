from pathlib import Path

file = Path.cwd().parent / "DAY12" / "main.py"
info_txt = Path(__file__).parent / "texts" / "info.txt"


def write() -> None:
    """
    overwrites information from a file to another
    """
    with open(file, "r") as f:
        text = f.read()
    with open(info_txt, "a") as w:
        w.write(text)


def read():
    """
    creates a generator
    """
    with open(info_txt, "r") as r:
        for line in r:
            if not "import" in line:
                yield line
            else:
                print("imports")


def output() -> None:
    """
    requests the number of rows and outputs a generator
    """
    gen = read()
    try:
        n = int(input("enter number of lines: "))
        for i in range(n):
            print(next(gen), end="")
    except StopIteration:
        print("final")


def main() -> None:
    """
    Main function, launch the rest
    """
    write()
    output()


if __name__ == "__main__":
    main()
