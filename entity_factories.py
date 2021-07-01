from math import hypot
from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

import random


player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="Player", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)
# what I want to do is adjust so that at creation, each orc has a chance to be different from the other orcs. 
# I also want to change the attacks to become slightly randomized within each attack, so that each attack reps a dice roll.
# The difference between the races will be the sides of the dice and the number of dice.
# need to change orc code in some way to incorporate a random seed later such that each orc is unique.

orc = Actor(
    char="O", 
    color=(63, 127, 63), 
    name="Orc", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp = 10, defense = 0, power = 3),
)

troll = Actor(
    char="T", 
    color=(0, 127, 0), 
    name="Troll", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp = 16, defense = 1, power = 4),
)