from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum
from pokemon import Charizard, Blastoise, Venusaur, Haunter, Gengar

class PokemonBase:

    def __init__(self, hp: int, poke_type: str) -> None:
       self.current_hp = hp
       self.poke_type = poke_type
       self.status_effect = ""

    def is_fainted(self) -> bool:
        if self.current_hp <= 0:
            self.hp = hp
            self.poke_type = poke_type

    def get_poke_name(self) -> str:
        return self.poke_name

    def is_fainted(self) -> bool:
        if self.hp <= 0:
            return True
        else:
            return False

    def get_level(self) -> int:
        return self.level

    def get_hp(self) -> int:
        return self.current_hp

    def level_up(self) -> None:
        self.level = self.get_level() + 1

    def get_speed(self) -> int:
        return self.speed
    def get_hp(self):
        return self.hp
    
    def set_hp(self, new_level):
        if self.poke_name == "Charmander":
            self.hp = 8 + 1 * new_level
        elif self.poke_name == "Squirtle":
            self.hp = 9 + 2 * new_level
        elif self.poke_name == "Bulbasaur" or self.poke_name == "Charizard":
            self.hp = 12 + 1 * new_level
        elif self.poke_name == "Gastly":
            self.hp = 6 + (new_level // 2)
        elif self.poke_name == "Eevee":
            self.hp = 10
        elif self.poke_name == "Blastoise":
            self.hp = 15 + 2 * new_level
        elif self.poke_name == "Venusaur":
            self.hp = 20 + (new_level // 2)
        elif self.poke_name == "Haunter":
            self.hp = 9 + (new_level // 2)
        elif self.poke_name == "Gengar":
            self.hp = 12 + (new_level // 2)

    def get_level(self) -> int:
        return self.level

    def level_up(self) -> None:
        self.level = self.get_level() + 1
        self.set_hp(self.level)
        self.set_speed(self.level)

    def get_speed(self) -> int:
        return self.speed

    def set_speed(self, new_level):
        if self.poke_name == "Charmander":
            self.speed = 7 + 1 * new_level
        elif self.poke_name == "Squirtle":
            self.speed = 7
        elif self.poke_name == "Bulbasaur":
            self.speed = 7 + (new_level // 2)
        elif self.poke_name == "Gastly":
            self.speed = 9 + 1 * new_level
        elif self.poke_name == "Eevee":
            self.speed = 7 + new_level
        elif self.poke_name == "Charizard":
            self.speed = 9 + 1 * new_level
        elif self.poke_name == "Blastoise":
            self.speed = 10
        elif self.poke_name == "Venusaur":
            self.speed = 3 + (new_level // 2)
        elif self.poke_name == "Haunter":
            self.speed = 6
        elif self.poke_name == "Gengar":
            self.speed = 12

    def get_attack_damage(self) -> int:
        return self.attack_damage

    def get_defence(self) -> int:
        return self.defence

    def lose_hp(self, lost_hp: int) -> None:
        self.current_hp -= lost_hp
        self.hp -= lost_hp

    def defend(self, damage: int) -> None:
        pokemon_name = self.get_poke_name()
        if pokemon_name == "Charmander":
            if damage >= self.defence:
                self.current_hp -= damage
            else:
                self.current_hp -= damage // 2
        elif pokemon_name == "Squirtle" or pokemon_name == "Blastoise":
            if damage > 2 * self.defence:
                self.current_hp -= damage
            else:
                self.current_hp -= damage // 2
        elif pokemon_name == "Bulbasaur" or pokemon_name == "Venusaur":
            if damage > self.defence + 5:
                self.current_hp -= damage
            else:
                self.current_hp -= damage // 2
        elif pokemon_name == "Gastly" or pokemon_name == "Haunter" or pokemon_name == "Gengar":
            self.current_hp -= damage
        elif pokemon_name == "Eevee":
            if damage >= self.defence:
                self.current_hp -= damage
        elif pokemon_name == "Charizard":
            if damage > self.defence:
                self.current_hp -= 2 * damage
            else:
                self.current_hp -= damage

    def attack(self, other: PokemonBase):
        attack_multiplier = [[1, 2, 0.5, 1, 1],
                             [0.5, 1, 2, 1, 1],
                             [2, 0.5, 1, 1, 1],
                             [1.25, 1.25, 1.25, 2, 0],
                             [1.25, 1.25, 1.25, 0, 1]]
                self.hp -= damage
            else:
                self.hp -= damage // 2
        elif pokemon_name == "Squirtle" or pokemon_name == "Blastoise":
            if damage > 2 * self.defence:
                self.hp -= damage
            else:
                self.hp -= damage // 2
        elif pokemon_name == "Bulbasaur" or pokemon_name == "Venusaur":
            if damage > self.defence + 5:
                self.hp -= damage
            else:
                self.hp -= damage // 2
        elif pokemon_name == "Gastly" or pokemon_name == "Haunter" or pokemon_name == "Gengar":
            self.hp -= damage
        elif pokemon_name == "Eevee":
            if damage >= self.defence:
                self.hp -= damage
            else:
                self.hp = self.hp
        elif pokemon_name == "Charizard":
            if damage > self.defence:
                self.hp -= 2 * damage
            else:
                self.hp -= damage

    def attack(self, other: PokemonBase):
        pass
        #if other.get_defence() == 
        # Step 1: Status effects on attack damage / redirecting attacks
        # Step 2: Do the attack
        # Step 3: Losing hp to status effects
        # Step 4: Possibly applying status effects
        pass

    def get_poke_name(self) -> str:
        return self.poke_name

    def should_evolve(self) -> bool:
        return not self.isfainted()
    def should_evolve(self) -> bool:
        if self.is_fainted() == False:
            return True
        elif self.is_fainter() == True:
            return False
        
    def can_evolve(self) -> bool:
        if self.get_level() == 1 and self.get_poke_name == "Gastly":
            return True
        elif self.get_level() == 3 and (self.get_poke_name == "Charmander" or self.get_poke_name == "Squirtle" or self.get_poke_name == "Haunter"):
            return True
        elif self.get_level() == 2 and self.get_poke_name == "Bulbasaur":
            return True
        else:
            return False

    def heal(self) -> None:
        self.current_hp = self.hp
        self.status_effect = ""

    def get_evolved_version(self) -> PokemonBase:
        if self.poke_name == "Charmander":
            return Charizard()
        elif self.poke_name == "Squirtle":
            return Blastoise()
        elif self.poke_name == "Bulbasaur":
            return Venusaur()
        elif self.poke_name == "Gastly":
            return Haunter()
        elif self.poke_name == "Haunter":
            return Gengar()

    def __str__(self) -> str:
        pokemon_string = f"LV. {self.level}: {self.hp} HP"
        return pokemon_string

class PokeType(Enum):
    FIRE = "fire"
    GRASS = "grass"
    WATER = "water"
    GHOST = "ghost"
    NORMAL = "normal"
    def heal(self):
        if self.get_poke_name() == "Charmander":
            self.hp = 8 + 1 * self.get_level()
        elif self.get_poke_name() == "Squirtle":
            self.hp = 9 + 2 * self.get_level()
        elif self.get_poke_name() == "Bulbasaur" or self.get_poke_name == "Charizard":
            self.hp = 12 + 1 * self.get_level()
        elif self.get_poke_name() == "Gastly":
            self.hp = 6 + (self.get_level() // 2)
        elif self.get_poke_name() == "Eevee":
            self.hp = 10
        elif self.get_poke_name() == "Blastoise":
            self.hp = 15 + 2 * self.get_level()
        elif self.get_poke_name() == "Venusaur":
            self.hp = 20 + (self.get_level() // 2)
        elif self.get_poke_name() == "Haunter":
            self.hp = 9 + (self.get_level() // 2)
        elif self.get_poke_name() == "Gengar":
            self.hp = 12 + (self.get_level() // 2)

    def get_evolved_version(self) -> PokemonBase:
        if self.poke_name == "Charmander":
            return self.Charizard()
        elif self.poke_name == "Squirtle":
            return self.Blastoise()
        elif self.poke_name == "Bulbasaur":
            return self.Venusaur()
        elif self.poke_name == "Gastly":
            return self.Haunter()
        elif self.poke_name == "Haunter":
            return self.Gengar()

    def __str__(self) -> str:
        pokemon_string = f"LV. {self.level} {self.poke_name}: {self.hp} HP"
        return pokemon_string

class PokeType:
    def __init__(self):
        attack_multiplier = [[1, 2, 0.5, 1, 1],[0.5, 1, 2, 1, 1],[2, 0.5, 1, 1, 1],[1.25, 1.25, 1.25, 2, 0],[1.25, 1.25, 1.25, 0, 1]]
        FIRE = attack_multiplier[0]
        GRASS = attack_multiplier[1]
        WATER = attack_multiplier[2]
        GHOST = attack_multiplier[3]
        NORMAL = attack_multiplier[4]
