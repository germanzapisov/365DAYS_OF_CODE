from tqdm import tqdm
import time

dict_of_fruits = {
    "Apple": "10kg",
    "Orange": "6kg",
    "Pineapple": "15kg",
}


def check_fruits() -> None:
    for item, item_kg in tqdm(dict_of_fruits.items()):
        print(f"\nFruit: {item} | Kg: {item_kg}")
        time.sleep(0.5)
if __name__ == "__main__":
    check_fruits()