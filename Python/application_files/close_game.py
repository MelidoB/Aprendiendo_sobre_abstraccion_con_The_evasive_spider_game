from pygame import event, QUIT
def close_game_function():
    """Close the game function when clicking exit"""
    for e in event.get():
        if e.type == QUIT:
            # if it is quit the game
            quit()
            exit(0)