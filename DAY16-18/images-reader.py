from pathlib import Path

signatures = {
    "JPG": b'\xff\xd8\xff',
    "PNG": b'\x89PNG',
    "AVIF": b'typavif'

}
folder = Path.home() / 'downloads'
print(folder)

def reader():
    cleaner()
    for file in folder.iterdir():
        if file.is_file():
            with open(file,'rb') as f:
                main = f.read(64)
                if main.startswith(signatures['JPG']):
                    JPG.append(f)
                if main.startswith(signatures['\x89PNG']):
                    PNG.append(f)
                if signatures['AVIF'] in main:
                    AVIF.append(f)


def gen_of_files():
    choice = input("Enter the file extension without the period")
    if choice.upper().startswith('PNG'):
        for file in PNG:
            yield file
    elif choice.upper().startswith('JPG'):
        for file in JPG:
            yield file
    elif choice.upper().startswith('AVIF'):
        for file in AVIF:
            yield file

def output_gen():
    gen = gen_of_files()
    for file in gen:
        print(file)

def counter():
    print(f'PNG:{len(PNG)}\nAVIF:{len(AVIF)}\nJPG:{len(JPG)}')


def cleaner():
    PNG.clear()
    AVIF.clear()
    JPG.clear()

def main():
    asc = int(input("""
    1 - file count counter
    2 - read all files of the format
    """))
    if asc == 1:
        reader()
        counter()
    if asc == 2:
        reader()
        output_gen()

if __name__ == "__main__":
    PNG, AVIF, JPG = [], [], []
    main()
