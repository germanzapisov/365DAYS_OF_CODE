import random

texts_fruits = {1: 'apple',
                2: 'orange',
                3: 'pineapple',
                4: 'qiwi',
                5: 'banana',
                6: 'melon'
}

texts_animals = {
    7: 'wolf',
    8: 'rabbit',
    9: 'parrot',
    10: "chicken",
    11: 'sheep',
    12: 'crocodile'
}

all_texts = texts_fruits | texts_animals

def generator(texts):
    for text, text_two in texts.items():
        if len(text_two) > 3:
            yield text_two
        else:
            continue


def gen_output(gen):
    while True:
        try:
            gens = next(gen)
            print(gens.replace(random.choice(gens),'-'))
            asc = input("enter answer:")
            if asc == gens: print("true")
            else: print("false")
        except StopIteration:
            print("the words are over")
            break


if __name__ == "__main__":
    gen = generator(all_texts)
    gen_output(gen)
