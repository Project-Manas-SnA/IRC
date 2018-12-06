
#import matplotlib.pyplot as plt
import networkx as nx
import os
import math
import time
#import cv2
#from qr import *

#from qr import *
#from box import *
import RPi.GPIO as rpi
from Node import Node
import subprocess
import configuration


class IRC:
    def __init__(self):

        self.theta = 0
        self.tol = float(os.environ.get("tolerance"))
        self.junc = float(os.environ.get("junction"))
        self.leftw = float(os.environ.get("leftw"))
        self.rightw = float(os.environ.get("rightw"))
        self.frontw = float(os.environ.get("frontw"))

#        self.vidcap = cv2.VideoCapture(0)
        self.boxlb = [False, False]
        self.boxdb = [False, False]
        self.boxp = [False, False]
        self.boxqr3 = [False, False]
        self.boxqr5 = [False, False]

        self.map = nx.Graph()
        self.last_node = -1
        self.map.add_node(-1, node=Node(self.getRobotX(), self.getRobotY(), -1, -1, -1, -1, 1))

    def controlInput(self,control):
        proc.stdin.write(bytes(str(control) + "\n",'utf-8'))
        proc.stdin.flush()

        if control == 5:
            return int(proc.stdout.readline().decode('UTF-8').rstrip("\n"))

        elif control == 6:
            return int(proc.stdout.readline().decode('UTF-8').rstrip("\n"))

        elif control == 7:
            return int(proc.stdout.readline().decode('UTF-8').rstrip("\n"))

        elif control == 8:
            return int(proc.stdout.readline().decode('UTF-8').rstrip("\n"))

        elif control == 9:
            return int(proc.stdout.readline().decode('UTF-8').rstrip("\n"))

        elif control == 10:
            return int(proc.stdout.readline().decode('UTF-8').rstrip("\n"))


    def getRobotX(self):
        return self.controlInput(5)

    def getRobotY(self):
        return self.controlInput(6)

    def getTheta(self):
        return self.controlInput(7)

    def getFront(self):
        return self.controlInput(8)

    def getLeft(self):
        return self.controlInput(9)

    def getRight(self):
        return self.controlInput(10)

    def turnleft(self):
        self.theta = (self.theta + 1) % 4
#        while not self.getTheta() == self.getTheta():
        self.controlInput(1)
        time.sleep(5)
        rpi.cleanup()
    
    def goleft(self):
        self.theta = (self.theta + 1) % 4
#        while not self.theta == self.getTheta():
            # robotgoleft()
        self.controlInput(1)
        rpi.cleanup()
        time.sleep(5)
        self.forward()
        # self.forward()

    def forward(self):
        # robotMoveForward()
        self.controlInput(0)
        rpi.cleanup()
        time.sleep(5)
        #self.stop()        	

    def goright(self):
        self.theta = (self.theta - 1)
        if (self.theta < 0):
            self.theta = 3
        #while not self.theta == self.getTheta():
            # robotgoright()
        self.controlInput(3)
        rpi.cleanup()
        time.sleep(5)
        self.forward()
        # self.forward()

    def turnright(self):
        self.theta = (self.theta - 1)
        if self.theta < 0:
            self.theta = 3
        #while not self.theta == self.getTheta():
        self.controlInput(3)
        time.sleep(5)
        rpi.cleanup()   

    def stop(self):
        self.controlInput(4)
        rpi.cleanup()

    def backTrace(self):
        self.turnright()
        self.turnright()

    def move(self):
        node = self.isJunction()
        if (not node[0]):
            self.forward()
        else:
            if self.theta == 0:
                right = node[1]['node'].right
                left = node[1]['node'].left
                front = node[1]['node'].front
                back = node[1]['node'].back
            elif self.theta == 1:
                right = node[1]['node'].front
                left = node[1]['node'].back
                front = node[1]['node'].left
                back = node[1]['node'].right
            elif self.theta == 2:
                right = node[1]['node'].left
                left = node[1]['node'].right
                front = node[1]['node'].back
                back = node[1]['node'].front
            else:
                right = node[1]['node'].back
                left = node[1]['node'].front
                front = node[1]['node'].right
                back = node[1]['node'].left

            if right > 0:
                rightv = self.map.node[right]['node'].visit
            if left > 0:
                leftv = self.map.node[left]['node'].visit
            if front > 0:
                frontv = self.map.node[front]['node'].visit

            if right == 0 and left == 0 and front == 0:
                self.goright()
            elif right > 0 and left > 0  and front == 0:
                self.forward()
            elif right > 0 and left == 0 and front>0:
                self.goright()
            elif right == 0 and left > 0 and front > 0:
                self.goright()

            elif right > 0 and left > 0 and front > 0:
                vc = rightv
                if leftv < frontv:
                    if leftv < vc:
                        self.goleft()
                    else:
                        self.goright()
                else:
                    if frontv < vc:
                        self.forward()
                    else:
                        self.goright()

            elif right >= 0 and left >= 0:
                if left==0 and right==0:
                    self.goright()
                elif left==0:
                    self.goleft()
                elif right==0:
                    self.goright()
                elif leftv < rightv:
                    self.goleft()
                else:
                    self.goright()

            elif right >= 0 and front >= 0:
                if front==0 and right==0:
                    self.goright()
                elif front==0:
                    self.forward()
                elif right==0:
                    self.goright()
                elif frontv < rightv:
                    self.forward()
                else:
                    self.goright()

            elif front >= 0 and left >= 0:
                if front==0 and left==0:
                    self.forward()
                elif front==0:
                    self.forward()
                elif left==0:
                    self.goleft()
                elif leftv < frontv:
                    self.goleft()
                else:
                    self.forward()

            elif right >= 0:
                self.goright()
            elif front >= 0:
                self.forward()
            elif left >= 0:
                self.goleft()
            elif back >= 0:
                self.backTrace()
            else:
                print("Dude you are grounded!")

    def goal(self, x, y, theta):
        path = self.getPath(x, y)
        for node in path:
            x = self.map.node[node]['node'].x
            y = self.map.node[node]['node'].y
            posex = self.getRobotX()
            posey = self.getRobotY()
            if self.theta == 0:
                if x - posex > self.tol:
                    self.turnright()
                elif posex - x > self.tol:
                    self.turnleft()
                elif posey - y > self.tol:
                    self.turnright()
                    self.turnright()
            elif self.theta == 1:
                if posey - y > self.tol:
                    self.turnleft()
                elif y - posey > self.tol:
                    self.turnright()
                elif x - posex > self.tol:
                    self.turnright()
                    self.turnright()
            elif self.theta == 2:
                if x - posex > self.tol:
                    self.turnleft()
                elif posex - x > self.tol:
                    self.turnright()
                elif y - posey > self.tol:
                    self.turnright()
                    self.turnright()
            else:
                if y - posey > self.tol:
                    self.turnleft()
                elif posey - y > self.tol:
                    self.turnright()
                elif posex - x > self.tol:
                    self.turnright()
                    self.turnright()
            while math.fabs(x - self.getRobotX()) > self.tol or math.fabs(y - self.getRobotY()) > 0:
                self.forward()
            self.junction()
        while not self.theta == self.getTheta():
            self.turnright()
        self.junction()

    def getPath(self, x, y):
        start, end = self.getNode([self.getRobotX(), self.getRobotY()], [x, y])
        path = nx.dijkstra_path(self.map, start, end)
        del path[0]
        return path

    def getNode(self, start, end):
        begin, finish = -1, -1
        for node in self.map.nodes(data = True):
            x = node[1]['node'].x
            y = node[1]['node'].y
            if math.fabs(x - start[0]) <= self.tol and math.fabs(y - start[1]) <= self.tol:
                begin = node[0]
            if math.fabs(x - end[0]) <= self.tol and math.fabs(y - end[1]) <= self.tol:
                finish = node[0]
        return begin, finish

    def junction(self):
        flag = 0
        last = self.map.node[self.last_node]['node']
        leftw, rightw, frontw = -1, -1, -1
        if self.getLeft() >= self.leftw:
            leftw = 0
        if self.getRight() >= self.rightw:
            rightw = 0
        if self.getFront() >= self.frontw:
            frontw = 0
        if self.getTheta() == 0:
            for node in self.map.nodes(data = True):
                if math.fabs(node[1]['node'].x - self.getRobotX()) <= self.tol and math.fabs(node[1]['node'].y - self.getRobotY()) <= self.tol:
                    flag = 1
                    node[1]['node'].left = max(leftw, node[1]['node'].left)
                    node[1]['node'].right = max(rightw, node[1]['node'].right)
                    node[1]['node'].front = max(frontw, node[1]['node'].front)
                    if not node[0] == self.last_node:
                        last.front = node[0]
                        node[1]['node'].back = self.last_node
                        self.map.add_edge(node[0], self.last_node)
                        node[1]['node'].visit += 1
                        self.last_node = node[0]
                    break

            if not flag and math.fabs(last.y - self.getRobotY()) >= self.junc and (not leftw < 0 or not rightw < 0 or frontw < 0):
                self.map.add_node(self.map.number_of_nodes() + 1, node = Node(self.getRobotX(), self.getRobotY(), leftw, rightw, frontw, self.last_node, 1))
                self.map.node[self.last_node]['node'].front = self.map.number_of_nodes()
                self.map.add_edge(self.last_node, self.map.number_of_nodes())
                self.last_node = self.map.number_of_nodes()

        elif self.getTheta() == 1:
            for node in self.map.nodes(data = True):
                if math.fabs(node[1]['node'].x - self.getRobotX()) <= self.tol and math.fabs(node[1]['node'].y - self.getRobotY()) <= self.tol:
                    flag = 1
                    node[1]['node'].front = max(rightw, node[1]['node'].front)
                    node[1]['node'].left = max(frontw, node[1]['node'].left)
                    node[1]['node'].back = max(leftw, node[1]['node'].back)
                    if not node[0] == self.last_node:
                        last.left = node[0]
                        node[1]['node'].right = self.last_node
                        self.map.add_edge(node[0], self.last_node)
                        node[1]['node'].visit += 1
                        self.last_node = node[0]
                    break

            if not flag and math.fabs(last.x - self.getRobotX()) >= self.junc and (not leftw < 0 or not rightw < 0 or frontw < 0):
                self.map.add_node(self.map.number_of_nodes() + 1, node = Node(self.getRobotX(), self.getRobotY(), frontw, self.last_node, rightw, leftw, 1))
                last.left = self.map.number_of_nodes()
                self.map.add_edge(self.last_node, self.map.number_of_nodes())
                self.last_node = self.map.number_of_nodes()

        elif self.getTheta() == 2:
            for node in self.map.nodes(data = True):
                if math.fabs(node[1]['node'].x - self.getRobotX()) <= self.tol and math.fabs(node[1]['node'].y - self.getRobotY()) <= self.tol:
                    flag = 1
                    node[1]['node'].left = max(rightw, node[1]['node'].left)
                    node[1]['node'].right = max(leftw, node[1]['node'].right)
                    node[1]['node'].back = max(frontw, node[1]['node'].back)
                    if not node[0] == self.last_node:
                        last.back = node[0]
                        node[1]['node'].front = self.last_node
                        self.map.add_edge(node[0], self.last_node)
                        node[1]['node'].visit += 1
                        self.last_node = node[0]
                    break

            if not flag and math.fabs(last.y - self.getRobotY()) >= self.junc and (not leftw < 0 or not rightw < 0 or frontw < 0):
                self.map.add_node(self.map.number_of_nodes() + 1, node = Node(self.getRobotX(), self.getRobotY(), rightw, leftw, self.last_node, frontw, 1))
                last.back = self.map.number_of_nodes()
                self.map.add_edge(self.last_node, self.map.number_of_nodes())
                self.last_node = self.map.number_of_nodes()

        else:
            for node in self.map.nodes(data = True):
                if math.fabs(node[1]['node'].x - self.getRobotX()) <= self.tol and math.fabs(node[1]['node'].y - self.getRobotY()) <= self.tol:
                    flag = 1
                    node[1]['node'].front = max(leftw, node[1]['node'].front)
                    node[1]['node'].right = max(frontw, node[1]['node'].right)
                    node[1]['node'].back = max(rightw, node[1]['node'].back)
                    if not node == self.last_node:
                        last.right = node[0]
                        node[1]['node'].left = self.last_node
                        self.map.add_edge(node[0], self.last_node)
                        node[1]['node'].visit += 1
                        self.last_node = node[0]
                    break

            if not flag and math.fabs(last.x - self.getRobotX()) >= self.junc and (not leftw < 0 or not rightw < 0 or frontw < 0):
                    self.map.add_node(self.map.number_of_nodes() + 1, node = Node(self.getRobotX(), self.getRobotY(), self.last_node, frontw, leftw, rightw, 1))
                    last.right = self.map.number_of_nodes()
                    self.map.add_edge(self.last_node, self.map.number_of_nodes())
                    self.last_node = self.map.number_of_nodes()

    def draw_graph(self, graph):
#        plt.title('Trajectory Graph')
        pos = nx.get_node_attributes(graph, 'node')
        positions = {}
        lab = {}
        for key, value in pos.items():
            positions[key] = (value.x, value.y)
        for key, value in pos.items():
            lab[key] = (value.left, value.right, value.front, value.back)
        # for node in graph:
        #     print(graph.node[node]['node'].x, graph.node[node]['node'].y)
        edg = [(u, v) for (u, v, d) in graph.edges(data=True)]
        # pos = graphviz_layout(graph, prog='dot')
        nx.draw_networkx_nodes(graph, positions, label=True, node_size=700)
        nx.draw_networkx_labels(graph, positions, labels=lab, font_size=6)
        nx.draw_networkx_edges(graph, positions, edgelist=edg)
#        plt.axis('off')
#        plt.show()

    def isJunction(self):
        for node in self.map.nodes(data=True):
            if math.fabs(self.getRobotX() - node[1]['node'].x) <= self.tol and math.fabs(self.getRobotY() - node[1]['node'].y) <= self.tol:
                return [True, node[1]]
        return [False]

    def getColour(self, image):
        data = decode(image)
        if data!=None:
            print(data)
            return "qr"
        data = detectColour(image)
        if data!=None:
            print(data)
            return data
        return "white"

    def check(self):
        res, image = self.vidcap.read()
        colour = self.getColour(image)

        while colour == "pink":
            self.stop()
            self.boxp = [True, True, self.getRobotX(), self.getRobotY(), self.getTheta()]
            res, image = self.vidcap.read()
            colour = self.getColour(image)
        while colour == "lightblue":
            self.stop()
            self.boxlb = [True, True, self.getRobotX(), self.getRobotY(), self.getTheta()]
            res, image = self.vidcap.read()
            colour = self.getColour(image)
        while colour == "darkblue":
            self.stop()
            self.boxdb = [True, True, self.getRobotX(), self.getRobotY(), self.getTheta()]
            res, image = self.vidcap.read()
            colour = self.getColour(image)
        while colour == "qr":
            if self.boxqr3[1]:
                if self.boxdb[1]:
                    while colour == "qr":
                        self.stop()
                        self.boxqr5 = [True, True, self.getRobotX(), self.getRobotY(), self.getTheta()]
                        res, image = self.vidcap.read()
                        colour = self.getColour(image)
                else:
                    self.boxqr5 = [True, False, self.getRobotX(), self.getRobotY(), self.getTheta()]
                    break
            else:
                if self.boxp[1] and self.boxlb[1]:
                    while colour == "qr":
                        self.stop()
                        self.boxqr3 = [True, True, self.getRobotX(), self.getRobotY(), self.getTheta()]
                        res, image = self.vidcap.read()
                        colour = self.getColour(image)
                else:
                    self.boxqr3 = [True, False, self.getRobotX(), self.getRobotY(), self.getTheta()]
                    break
   
    def print(self):
        for node in self.map.node(data = True):
            print(node[1]['node'].x, node[1]['node'].y, node[1]['node'].left, node[1]['node'].front, node[1]['node'].right, node[1]['node'].back, node[1]['node'].visit)
        print()
if __name__ == "__main__":
   proc = subprocess.Popen('./maze_ipc.out', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
   # proc.stdin.write(bytes("helo\n", 'utf-8'))
   # proc.stdin.flush()
   # print(proc.stdout.readline().decode('UTF-8').rstrip('\n'))
   # print(proc.stdout.readline().decode('UTF-8').rstrip('\n'))
   #cmd = "maze_ipc.cpp"
   #subprocess.call(["g++","maze_ipc.cpp","-lwiringPi"])
   #a = subprocess.call("./maze_ipc") 
   #print(a)
   start = IRC()
   #print(start.getFront())
   #start.turnleft()
   #time.sleep(1)
   #start.stop()
   #start.forward()
   #start.stop()
   #time.sleep(5)
   #time.sleep(5)
   #start.controlInput(3)
   #time.sleep(1)
   #start.controlInput(0)
   #time.sleep(1)
   #start.controlInput(3)
   #time.sleep(1)
   #start.controlInput(0)
   #start.stop()
   try:
       while True:
          time.sleep(1)
          start.junction()
          print(start.getRobotX(), start.getRobotY())
          if start.boxqr3[0] and not start.boxqr3[1] and start.boxp[1] and start.boxlb[1]:
              start.goal(start.boxqr3[2], start.boxqr3[3], start.boxqr3[4])
          elif start.boxqr5[0] and not start.boxqr5[1] and start.boxdb[1]:
              start.goal(start.boxqr5[2], start.boxqr5[3], start.boxqr5[4])
          else:
              start.move()
          nx.write_gpickle(start.map, "test.gpickle")
#          start.draw_graph(start.map)
#          start.check()
#          print(start.getLeft(), start.getFront(), start.getRight(), start.getTheta(), start.getRobotX(), start.getRobotY())
          start.print()
   finally:
       proc.terminate()
