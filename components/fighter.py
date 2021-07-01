from __future__ import annotations

from typing import TYPE_CHECKING
import random

from components.base_component import BaseComponent
from input_handlers import GameOverEventHandler
from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor


class Fighter(BaseComponent):
    entity: Actor

    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    @property
    def hp(self) -> int:
        return self._hp 
    
    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.entity.ai:
            self.die()

    def die(self) -> None:
        if self.engine.player is self.entity:
            death_message = "You died, bro!"
            self.engine.event_handler = GameOverEventHandler(self.engine)
        else:
            death_message = f"{self.entity.name} is dead, bro!"

        self.entity.char = "%"
        self.entity.color = (191, 0, 0)
        self.entity.blocks_movement = False
        self.entity.ai = None
        self.entity.name = f"{self.entity.name} remains"
        self.entity.render_order = RenderOrder.CORPSE

        print(death_message)


class MonsterFighter(Fighter):
    def __init__(self, min_hp: int, max_hp: int, min_power: int, max_power: int, min_defense: int, max_defense: int):
        super().__init__(
            base_hp = random.randint(min_hp, max_hp),
            base_attack = random.randint(min_power, max_power),
            base_defense = random.randint(min_defense, max_defense),
        )

