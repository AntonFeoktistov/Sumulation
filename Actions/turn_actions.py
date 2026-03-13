from map.map import Map


def make_all_move(map: Map):
    creatures = map.get_all_creatures()
    for creature in creatures:
        creature.current_speed = creature.speed
        creature.make_move(map)


def find_winner(map: Map):
    entities = map.field.values()
    count_grass = 0
    count_herbivore = 0
    for entity in entities:
        if entity.type == "grass":
            count_grass += 1
        if entity.type == "herbivore":
            count_herbivore += 1
    if count_grass == 0:
        return "herbivore"
    if count_herbivore == 0:
        return "predator"
    return False
