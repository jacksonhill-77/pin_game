from pin_game import Ball

def testMoveLeft():
    ball = Ball('R',5,6)
    ball.moveBallLeft()
    assert ball.x == 5
    assert ball.y == 7


