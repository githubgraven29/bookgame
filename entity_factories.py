from components.ai import HostileEnemy
from components.consumable import HealingConsumable
from components.fighter import Fighter, MonsterFighter
from entity import Actor, Item




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
    fighter=MonsterFighter(low_hp = 8, high_hp = 12, min_power = 2, max_power = 3, min_defense = -1, max_defense = 1),
)

troll = Actor(
    char="T", 
    color=(0, 127, 0), 
    name="Troll", 
    ai_cls=HostileEnemy,
    fighter=MonsterFighter(low_hp = 13, high_hp = 19, min_power = 2, max_power = 6, min_defense = 0, max_defense = 2),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
)
