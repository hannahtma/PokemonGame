from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by everyone"

from abc import abstractmethod
from enum import Enum, auto

class PokemonBase:

    def __init__(self, hp: int, poke_type: str) -> None:
        """
            PokemonBase class definition which initializes max hit points of the pokemon and pokemon type
            
            Parameters: the hit points in integer form and pokemon type in string form
        """
        if type(poke_type) != str:
            raise TypeError(poke_type + ' is invalid, only string values accepted')
        if type(hp) != int:
            raise TypeError(hp + " is invalid, only integer values accepted")
        self.base_hp = hp
        self.poke_type = poke_type

    def is_fainted(self) -> bool:
        """
            Determine if the pokemon fainted

            Parameters:
                self - refers to this instance of the class
        """
        if self.hp <= 0:
            return True
        else:
            return False

    def get_poke_name(self) -> str:
        return self.poke_name

    def get_level(self) -> int:
        return self.level

    def get_hp(self) -> int:
        return self.hp

    def get_speed(self) -> int:
        return self.speed

    def get_hp(self):
        return self.hp

    def get_level(self) -> int:
        return self.level

    def level_up(self) -> None:
        """
            Method for pokemon to level up

            Parameters:
                self - refers to this instance of the class
        """
        self.level += 1
        self.set_hp()
        self.set_attack()
        self.set_speed()
        self.set_defence()

    def get_speed(self) -> int:
        return self.speed

    def get_attack_damage(self) -> int:
        return self.attack_damage

    def get_defence(self) -> int:
        return self.defence

    def lose_hp(self, lost_hp: int) -> None:
        """
            Method for pokemon losing hit points

            Parameters:
                self - refers to this instance of the class
                lost_hp - the hit points lost due to the attack
        """
        self.hp -= lost_hp

    def get_poke_type(self) -> str:
        return self.poke_type

    def get_status_effect(self) -> str:
        return self.status_effect

    def get_effective_attack(self) -> int:
        return self.effective_attack

    @abstractmethod
    def get_evolved_version(self) -> PokemonBase:
        pass

    @abstractmethod
    def defend(self, damage: int) -> None:
        pass

    @abstractmethod
    def attack(self, other: PokemonBase):
        pass
        # Step 1: Status effects on attack damage / redirecting attacks
        # Step 2: Do the attack
        # Step 3: Losing hp to status effects
        # Step 4: Possibly applying status effects

    def should_evolve(self) -> bool:
        if self.is_fainted() == False and self.can_evolve() == True:
            return True
        else:
            return False
    
    def remove_status_effect(self):
        if self.status_effect == "Paralysis":
            self.speed = self.speed * 2
        self.status_effect = ""

    def health_cuts(self):
        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

    @abstractmethod
    def set_hp(self) -> None:
        pass

    @abstractmethod
    def set_attack(self) -> None:
        pass

    @abstractmethod
    def set_speed(self) -> None:
        pass

    @abstractmethod
    def set_defence(self) -> None:
        pass

    @abstractmethod
    def can_evolve(self) -> bool:
        pass

    def heal(self) -> None:
        self.hp = self.base_hp
        if self.status_effect == "Paralysis":
            self.speed = self.speed * 2
        self.status_effect = ""

    def __str__(self) -> str:
        pokemon_string = f"LV. {self.level} {self.poke_name}: {self.hp} HP"
        return pokemon_string

class PokeType(Enum):
    FIRE = auto()
    GRASS = auto()
    WATER = auto()
    GHOST = auto()
    NORMAL = auto()