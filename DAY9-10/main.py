from pedantic import pedantic
from pedantic import pedantic_class
from pedantic.exceptions import PedanticTypeCheckException


dict_heroes = {
    "Basic": {"level": 1, "hp": 80}
}

@pedantic_class
class Hero:
    def __init__(self, name: str, level: int, hp: int) -> None:
        self.__name = name
        self.__level = level
        self.__hp = hp

    @property
    def name(self) -> str:
        return self.__name

    @property
    def level(self) -> int:
        return self.__level

    @property
    def hp(self) -> int:
        return self.__hp

    def info(self) -> str:
        return f'character name: {self.name} | level: {self.level} | HP: {self.hp}'


# @pedantic_class
# class Antimag(Hero):
#     def __init__(self, name, level, hp, char: int):
#         super().__init__(name, level, hp)
#         self.__char = char

if __name__ == "__main__":
    basic = dict_heroes.get("Basic")

    try:
        basic_hero = Hero(name="Basic", level=basic["level"], hp=basic["hp"])
        print(basic_hero.info())

    except PedanticTypeCheckException:
        print("data types are specified incorrectly (pedantic)")