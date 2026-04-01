import random
from tqdm import tqdm


class Colors:
    """
    colors for text
    """

    red = "\033[31m"
    green = "\033[32m"
    purple = "\033[35m"
    reset = "\033[0m"


def generator(texts):
    """
    creates a generator
    """
    for id, text in texts.items():
        if len(text) > 3:
            yield text


def gen_output(gen, total):
    """
    displays a dictionary
    and asks for a response
    """
    bar = tqdm(total=total)
    while True:
        try:
            my_gen = next(gen)
            print(next(gen_id), my_gen.replace(random.choice(my_gen), "-"))
            asc = input(f"{Colors.purple}enter answer:{Colors.reset}")
            if asc == my_gen:
                print(f"{Colors.green}true{Colors.reset}")
                bar.update(1)
            else:
                print(f"{Colors.red}false{Colors.reset}")
                bar.update(1)
        except StopIteration:
            print("the words are over")
            bar.close()
            break


if __name__ == "__main__":
    texts_fruits = {
        2: "apple",
        1: "orange",
        3: "pineapple",
        4: "qiwi",
        5: "banana",
        6: "melon",
    }

    texts_animals = {
        7: "wolf",
        8: "rabbit",
        9: "parrot",
        10: "chicken",
        11: "sheep",
        12: "crocodile",
    }

    all_texts = texts_fruits | texts_animals
    gen_id = (i + 1 for i in range(0, 10000000))
    gen = generator(all_texts)
    gen_output(gen, total=len(all_texts))
