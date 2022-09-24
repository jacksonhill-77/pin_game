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

def testPinsAreExpectedColour():
    game = GamePlayer(20, "RGBRG", 20)
    for row in game.grid.grid:
        for pin in row:
            if pin.x == 16 and pin.y == 7:
                assert pin.colour == 'g'
            if pin.x == 13 and pin.y == 17:
                assert pin.colour == 'white'





    
    





