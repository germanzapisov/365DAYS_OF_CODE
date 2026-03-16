from pedantic import pedantic_class, timer, pedantic
from pedantic.exceptions import PedanticTypeCheckException
from pedantic import pedantic_require_docstring



dict_heroes = {
    "Basic": {"level": 1, "hp": 80},
    "AntiMage": {"level": 1, "hp": 120, "ability": 35},
}

dict_colors = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "BLUE": "\033[33m",
    "RESET": "\033[0m"
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
        return f"character name: {self.name} | level: {self.level} | HP: {self.hp}"

    def __repr__(self) -> str:
        return f"name={self.name}, level={self.level}, hp={self.hp}"


@pedantic_class
class AntiMage(Hero):
    """
    class, inherited from Hero,
    displays information about the Anti-Mage character
    Attributes:
    name: character name
    level: character level
    hp: character hp
    ability: character ability
    Methods:
    info():
    returns information about a character
    """
    def __init__(self, name: str, level: int, hp: int, ability: int) -> None:
        super().__init__(name=name, level=level, hp=hp)
        self.__ability = ability

    @property
    def ability(self) -> int:
        return self.__ability

    def info(self) -> str:
        return super().info() + f" | Чары {self.ability}"

    def __repr__(self) -> str:
        return f"name={self.name}, level={self.level}, hp={self.hp}, char={self.ability}"

@pedantic_require_docstring
@timer
def menu() -> None:
    while True:
        select_action = int(
            input(
                f"""
{dict_colors.get("GREEN")} 1 - View character information {dict_colors.get("RESET")}
{dict_colors.get("RED")} 2 - Exit {dict_colors.get("RESET")}
>>""".strip()
            )
        )
        if select_action == 1:
            hero_asc = int(
                input(
                    """
1 - Basic
2 - AntiMage
>>""".strip()
                )
            )
            print(antimage_hero) if hero_asc == 2 else print(basic_hero)

        elif select_action == 2:
            print("Bye!")
            break


if __name__ == "__main__":
    basic = dict_heroes.get("Basic")
    antimag = dict_heroes.get("AntiMage")

    try:

        basic_hero = Hero(name="Basic",
                          level=basic["level"],
                          hp=basic["hp"])

        antimage_hero = AntiMage(
            name="AntiMage",
            level=antimag["level"],
            hp=antimag["hp"],
            ability=antimag["ability"],
        )

    except PedanticTypeCheckException:
        print("data types are specified incorrectly (pedantic)")

    menu()