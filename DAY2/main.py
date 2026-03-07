import time
from config import logger

YELLOW = "\033[33m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
BLUE = "\033[36m"
RESET = "\033[0m"


class Hero:
    """
    Parent class, initializes the character's health and damage.
    Attributes:
    health (int): Character's health
    damage (int): Character's damage
    Methods:
    info(): Returns character information
    attack(): Stores combat logic
    """

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def info(self):
        logger.debug("information about the character is displayed")
        return f" The hero has {self.health} HP and {self.damage} damage"

    def take_damage(self, dmg):
        self.health -= dmg

    def loading_battle(self):
        for _ in range(1, 13):
            print(f"{YELLOW}||{RESET}{GREEN}", end="")
            time.sleep(0.1)

    def attack(self, other):
        logger.debug("the battle has begun")
        count = 0
        time.sleep(0.1)
        turn_on = True
        for i in range(1, 100):
            if turn_on:
                self.loading_battle()
                print(f"\nround {i} {PURPLE}{self}{RESET} hits {BLUE}{other}{RESET}")
                time.sleep(1.3)
                other.take_damage(self.damage)
                print(
                    f"{self} hits {BLUE}{other}{RESET}, {BLUE}{other}{RESET} has {GREEN}{other.health}hp{RESET} left\n"
                )
                time.sleep(1.6)
                turn_on = False
                if other.health <= 0:
                    print(f"The enemy {other} is defeated!")
                    logger.debug("the fight is over")
                    break
            else:
                self.loading_battle()
                print(f"\nround {i} {BLUE}{other}{RESET} hits {PURPLE}{self}{RESET}")
                time.sleep(1.3)
                self.take_damage(other.damage)
                print(
                    f"{BLUE}{other}{RESET} hits {PURPLE}{self}{RESET}, {PURPLE}{self}{RESET} has {GREEN}{self.health}hp{RESET} left\n"
                )
                time.sleep(1.6)
                turn_on = True
                if self.health <= 0:
                    logger.debug("the fight is over")
                    print(f"Our character {self}  is defeated!")
                    break


class Doctor(Hero):
    """
        A class derived from the Hero, incorporating the Doctor's abilities: regeneration.
    Attributes:
    regeneration (int): Character regeneration
    Methods:
    regeneration_hp(): Character regeneration logic
    info(): Returns character information
    constructor __str__(): Returns the character type
    """

    def __init__(self, health, damage, regeneration):
        super().__init__(health, damage)
        self.regeneration = regeneration

    def take_damage(self, dmg):
        if self.health <= 115:
            self.health += self.regeneration
            print(f"{self} Received healing equal to {self.regeneration}HP!")
            self.health -= dmg
        else:
            self.health -= dmg

    def __str__(self):
        return "Doctor"

    def info(self):
        text = super().info()
        return f"{text} and {self.regeneration} Regeneration"


class Prince(Hero):
    """
    A class derived from the Hero, incorporating the Prince's abilities: shield.
    Attributes:
    defense (int): Character's shield
    Methods:
    defense(): Character defense logic
    info(): Returns character information
    constructor __str__(): Returns character type
    """

    def __init__(self, health, damage, shield, boolean_false=False):
        super().__init__(health, damage)
        self.shield = shield
        self.boolean_false = boolean_false

    def take_damage(self, dmg):
        if self.shield > 0:
            if dmg <= self.shield:
                self.shield -= dmg
                dmg = 0
                print(
                    f"The shield repelled the attack! Remaining shield strength: {self.shield}"
                )
            else:
                dmg -= self.shield
                self.shield = 0
        if self.shield <= 0:
            if not self.boolean_false:
                print("the shield is broken!")
                self.boolean_false = True
        self.health -= dmg

    def info(self):
        text = super().info()
        return f"{text} and {self.shield} shield"

    def __str__(self):
        return "Prince"


def initializing_characters():
    prince = Prince(160, 40, 40)
    doctor = Doctor(215, 25, 15)
    return prince, doctor


def menu():
    while True:
        prince, doctor = initializing_characters()
        try:
            menu_asc = int(
                input(
                    """          
                Select the desired action:
                1 - \033[35mPlay as the Mage against the Prince\033[0m
                2 - \033[35mPlay as the Prince against the Mage\033[0m
                3 - \033[33mDisplay information about a character\033[0m
                4 - \033[32mExit\033[0m
                >>
                        """.strip()
                )
            )
            if menu_asc == 1:
                logger.debug("the game for the magician was chosen")
                doctor.attack(prince)
                time.sleep(0.3)
            elif menu_asc == 2:
                logger.debug("the game for the prince was chosen")
                prince.attack(doctor)
                time.sleep(0.3)
            elif menu_asc == 3:
                logger.debug("character information selected")
                hero_choice = int(
                    input(
                        """
                Choose a character from the list below:
                1 - Doctor
                2 - Prince
                """.strip()
                    )
                )
                if hero_choice == 1:
                    logger.debug("information about the magician has been selected")
                    print(doctor.info())
                elif hero_choice == 2:
                    logger.debug("information about the prince has been selected")
                    print(prince.info())
            if menu_asc == 4:
                logger.debug("output selected")
                print("\ngoodbye!")
                break
        except ValueError:
            logger.error("a non-integer number was entered")
            print("enter the integer!")
        except KeyboardInterrupt:
            logger.info("the user stopped the code")
            print("\ngoodbye!")
            break


if __name__ == "__main__":
    menu()
