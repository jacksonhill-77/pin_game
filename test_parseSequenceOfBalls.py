from pin_game import GamePlayer

def testParseSequenceOfBalls():
    player = GamePlayer(5, "RGBRBG")
    player.parseSequenceOfBalls()
    ballColours = []
    for ball in player.ballsToSimulate:
        ballColours.append(ball.colour)
    assert ballColours == ["R","G","B","R","B","G"]


