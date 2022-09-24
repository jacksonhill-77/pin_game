from pin_game import Ball

def testShatterRightBallX():
    ball = Ball("r", 5, 7)
    right = ball.shatter(ball)
    assert right.x == 6

def testMoveBallLeft():
    ball = Ball('r',5,6)
    ball.moveBallLeft()
    print(ball.x, ball.y)
    assert ball.x == 5
    assert ball.y == 7

def testMoveBallRight():
    ball = Ball('r',6,7)
    ball.moveBallRight()
    print(ball.x, ball.y)
    assert ball.x == 7
    assert ball.y == 8

def testShatterLeftBall():
    ball = Ball('r', 2,2)
    ball.shatter(ball)
    assert ball.x == 2
    assert ball.y == 3

def testShatterRightBall():
    ball = Ball('r', 2,2)
    rightBall = ball.shatter(ball)
    assert rightBall.x == 3
    assert rightBall.y == 3


