def create_player(name, health):
    """
    Creates and returns a player dictionary
    """

    player = {
        "name": name,
        "health": health,
        "attack": 10,
        "inventory": []
    }

    return player


def is_alive(player):
    """
    Checks if the player is still alive
    """

    if player["health"] > 0:
        return True
    else:
        return False





#edit
def create_player(name, health):
    player = {
        "name": name,
        "health": health,
        "hp": health,
        "attack": 10,
        "inventory": [],
        "gold": 10,
        "companion": None,
        "flags": {}
    }
    return player

