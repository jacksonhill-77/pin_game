from pin_game import Ball



def testShatterRightBallX():
    ball = Ball("r", 5, 7)
    left, right = ball.shatter()
    assert right.x == 6


