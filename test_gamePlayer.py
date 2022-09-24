from pin_game import GamePlayer

def returnGamePinsAsList(size, colours, seed):
    game = GamePlayer(size, colours, seed)
    game.playGame()
    pins = []
    for row in game.grid.grid:
        for pin in row:
            colours = (pin.colour)
            pins.append(colours)
    return pins

def testDifferentSeedsGiveDifferentResults():
    size = 20
    colours = 'RGBBGR'
    game1Pins = returnGamePinsAsList(size, colours, 50)
    game2Pins = returnGamePinsAsList(size, colours, 100)
    assert game1Pins != game2Pins



    
    





