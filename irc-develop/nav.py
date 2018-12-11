#!usr/bin/env/python3
import random

class node(object):

    def __init__(self,id=0,x=0,y=0,ln=-1,rn=-1,fn=-1,bn=-1,vc=0):
        self.id = id
        self.x = y
        self.y = x
        self.left = ln
        self.right= rn
        self.front = fn
        self.back = bn
        self.visit_count = vc

    def display(self):
        print("id:",self.id,"x:",self.x,"y:",self.y,"left:",self.left,"right:",self.right,"front:"\
              ,self.front,"back:",self.back,"visit_count:",self.visit_count)

def goForward():
    if currentHeading == 0:
        pass
    elif currentHeading == 3 or currentHeading == 2:
        while currentHeading != 0:
            turnLeft()
    else:
        turnRight()
    moveStraight()
    print("Front")

def goLeft():
    if currentHeading == 1:
        pass
    elif currentHeading == 2 or currentHeading == 3:
        while currentHeading != 1:
            turnLeft()
    else:
        turnRight()
    moveStraight()
    print("Left")

def goRight():
    if currentHeading == 3:
        pass
    elif currentHeading == 2 or currentHeading == 1:
        while currentHeading != 3:
            turnLeft()
    elif currentHeading == 0:
        turnRight()
    moveStraight()
    print("Right")

def backTrace():
    for i in range(2):
        turnLeft()
    moveStraight()
    print("Backtrace")

def navigate(n):
    n.display()

    if(currentHeading == 0):
        right = n.right
        left = n.left
        front = n.front
        back = n.back
    elif (currentHeading == 1):
        right = n.front
        left = n.back
        front = n.left
        back = n.right
    elif (currentHeading == 2):
        right = n.left
        left = n.right
        front = n.back
        back = n.front
    else:
        right = n.back
        left = n.front
        front = n.right
        back = n.left


    if right > 0 and left > 0 and front > 0:
        vc = graph[right].visit_count
        if graph[left].visit_count < graph[front].visit_count:
            goLeft() if graph[left].visit_count < vc else goRight()
        else:
            goForward() if graph[front].visit_count < vc else goRight()

    elif right > 0 and left > 0:
        goLeft() if graph[left].visit_count < graph[right].visit_count else goRight()
    elif right > 0 and front > 0:
        goForward() if graph[front].visit_count < graph[right].visit_count else goRight()
    elif front > 0 and left > 0:
        goLeft() if graph[left].visit_count < graph[front].visit_count else goForward()

    if right > 0:
        goRight()
    elif front > 0:
        goForward()
    elif left > 0:
        goLeft()
    elif back > 0:
        backTrace()
    else:
        print("Dude you are grounded!")

    graph[n.id].visit_count += 1



if __name__ == "__main__":
    x,y = 0,0
    for i in range(10):
        lw = random.randint(-1,10)
        rw = random.randint(-1,10)
        fw = random.randint(-1,10)
        bw = random.randint(-1,10)
        n = node(i,x,y,lw,rw,fw,bw,0)
        navigate(n)