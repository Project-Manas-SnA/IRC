import matplotlib.pyplot as plt
import networkx as nx
import os
import math
import cv2
from qr import *
from box import *

from Node import Node
import configuration


class IRC:
    def __init__(self):
        self.limitx = 30
        self.limity = 36
        self.posex = 2
        self.posey = 2
        self.theta = 0
        self.count = 0
        self.tol = float(os.environ.get("tolerance"))
        self.junc = float(os.environ.get("junction"))

        self.vidcap = cv2.VideoCapture(0)
        self.boxlb = [False, False]
        self.boxdb = [False, False]
        self.boxp = [False, False]
        self.boxqr3 = [False, False]
        self.boxqr5 = [False, False]

        self.map = nx.Graph()
        self.last_node = -1
        self.map.add_node(-1, node=Node(self.posex, self.posey, -1, -1, -1, -1, 1))

    def create_map(self):
        self.count = self.count + 1
        self.maze = np.zeros((self.limitx, self.limity))
        self.maze[self.posex][self.posey] = 1
        for x in range(0, self.limitx):
            self.maze[x][0] = 2
            self.maze[x][self.limity - 1] = 2
        for x in range(0, self.limity):
            self.maze[self.limitx - 1][x] = 2
            self.maze[0][x] = 2
        for x in range(0, 4):
            self.maze[4][x] = 2
        for x in range(7, 12):
            self.maze[4][x] = 2
        for x in range(0, 5):
            self.maze[x][12] = 2
        for x in range(4, 13):
            self.maze[8][x] = 2
        for x in range(9, 13):
            self.maze[x][8] = 2
        for x in range(0, self.limity):
            self.maze[16][x] = 2
        for x in range(12, 16):
            self.maze[x][4] = 2
        for x in range(12, 16):
            self.maze[x][12] = 2

        for x in range(4, 13):
            self.maze[x][16] = 2
        for x in range(16, 20):
            self.maze[8][x] = 2
        for x in range(4, 9):
            self.maze[x][20] = 2

        for x in range(12, 16):
            self.maze[x][23] = 2
        for x in range(20, 24):
            self.maze[12][x] = 2

        for x in range(24, 27):
            self.maze[8][x] = 2
        for x in range(8, 12):
            self.maze[x][27] = 2
        for x in range(27, 32):
            self.maze[12][x] = 2

        for x in range(24, 31):
            self.maze[4][x] = 2
        for x in range(4, 9):
            self.maze[x][31] = 2

        if self.count % 1 == 0:
            plt.title("Maze")
            plt.imshow(self.maze)
            plt.grid()
            plt.show()

    def goleft(self):
        self.theta = (self.theta + 1) % 4
        self.forward()

    def turnleft(self):
        self.theta = (self.theta + 1) % 4

    def forward(self):
        if (self.theta == 0):
            front = [self.posex, self.posey + 1]
            front2 = [self.posex, self.posey + 2]

        elif (self.theta == 1):
            front = [self.posex - 1, self.posey]
            front2 = [self.posex - 2, self.posey]

        elif (self.theta == 2):
            front = [self.posex, self.posey - 1]
            front2 = [self.posex, self.posey - 2]
        else:
            front = [self.posex + 1, self.posey]
            front2 = [self.posex + 2, self.posey]

        # if (not self.maze[front2[0]][front2[1]] == 2):
        self.posex = front[0]
        self.posey = front[1]

    def backward(self):
        if (self.theta == 0):
            back = [self.posex, self.posey - 1]
        elif (self.theta == 1):
            back = [self.posex + 1, self.posey]
        elif (self.theta == 2):
            back = [self.posex, self.posey + 1]
        else:
            back = [self.posex - 1, self.posey]

        self.posex = back[0]
        self.posey = back[1]

    def goright(self):
        self.theta = (self.theta - 1)
        if (self.theta < 0):
            self.theta = 3
        self.forward()

    def turnright(self):
        self.theta -= 1
        if self.theta < 0:
            self.theta = 3

    def stop(self):
        pass

    def backTrace(self):
        self.turnleft()
        self.turnright()
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
            elif right > 0 and left > 0 and front == 0:
                self.forward()
            elif right > 0 and left == 0 and front > 0:
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
                if left == 0 and right == 0:
                    self.goright()
                elif left == 0:
                    self.goleft()
                elif right == 0:
                    self.goright()
                elif leftv < rightv:
                    self.goleft()
                else:
                    self.goright()

            elif right >= 0 and front >= 0:
                if front == 0 and right == 0:
                    self.goright()
                elif front == 0:
                    self.forward()
                elif right == 0:
                    self.goright()
                elif frontv < rightv:
                    self.forward()
                else:
                    self.goright()

            elif front >= 0 and left >= 0:
                if front == 0 and left == 0:
                    self.forward()
                elif front == 0:
                    self.forward()
                elif left == 0:
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
            posex = self.posex
            posey = self.posey
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
            while math.fabs(x - self.posex) > self.tol or math.fabs(y - self.posey) > 0:
                self.forward()
            self.create_map()
            self.junction()
        while not theta == self.theta:
            self.turnright()

    def getPath(self, x, y):
        start, end = self.getNode([self.posex, self.posey], [x, y])
        path = nx.dijkstra_path(self.map, start, end)
        del path[0]
        return path

    def getNode(self, start, end):
        begin, finish = -1, -1
        for node in self.map.nodes(data=True):
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
        if self.theta == 0:
            left = [self.posex - 2, self.posey]
            left2 = [self.posex - 2, self.posey - 1]
            left3 = [self.posex - 2, self.posey + 1]
            right = [self.posex + 2, self.posey]
            right2 = [self.posex + 2, self.posey - 1]
            right3 = [self.posex + 2, self.posey + 1]
            front = [self.posex, self.posey + 2]

            leftw, rightw, frontw = -1, -1, -1
            if not self.maze[left[0]][left[1]] == 2 and not self.maze[left2[0]][left2[1]] == 2 and not \
            self.maze[left3[0]][left3[1]] == 2:
                leftw = 0
            if not self.maze[right[0]][right[1]] == 2 and not self.maze[right2[0]][right2[1]] == 2 and not \
            self.maze[right3[0]][right3[1]] == 2:
                rightw = 0
            if not self.maze[front[0]][front[1]] == 2:
                frontw = 0

            for node in self.map.nodes(data=True):
                if math.fabs(node[1]['node'].x - self.posex) <= self.tol and math.fabs(
                        node[1]['node'].y - self.posey) <= self.tol:
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

            if not flag and math.fabs(last.y - self.posey) >= self.junc and (
                    not leftw < 0 or not rightw < 0 or frontw < 0):
                self.map.add_node(self.map.number_of_nodes() + 1,
                                  node=Node(self.posex, self.posey, leftw, rightw, frontw, self.last_node, 1))
                self.map.node[self.last_node]['node'].front = self.map.number_of_nodes()
                self.map.add_edge(self.last_node, self.map.number_of_nodes())
                self.last_node = self.map.number_of_nodes()

        elif self.theta == 1:
            left = [self.posex, self.posey - 2]
            left2 = [self.posex + 1, self.posey - 2]
            left3 = [self.posex - 1, self.posey - 2]
            right = [self.posex, self.posey + 2]
            right2 = [self.posex + 1, self.posey + 2]
            right3 = [self.posex - 1, self.posey + 2]
            front = [self.posex - 2, self.posey]

            leftw, rightw, frontw = -1, -1, -1
            if not self.maze[left[0]][left[1]] == 2 and not self.maze[left2[0]][left2[1]] == 2 and not \
            self.maze[left3[0]][left3[1]] == 2:
                leftw = 0
            if not self.maze[right[0]][right[1]] == 2 and not self.maze[right2[0]][right2[1]] == 2 and not \
            self.maze[right3[0]][right3[1]] == 2:
                rightw = 0
            if not self.maze[front[0]][front[1]] == 2:
                frontw = 0

            for node in self.map.nodes(data=True):
                if math.fabs(node[1]['node'].x - self.posex) <= self.tol and math.fabs(
                        node[1]['node'].y - self.posey) <= self.tol:
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

            if not flag and math.fabs(last.x - self.posex) >= self.junc and (
                    not leftw < 0 or not rightw < 0 or frontw < 0):
                self.map.add_node(self.map.number_of_nodes() + 1,
                                  node=Node(self.posex, self.posey, frontw, self.last_node, rightw, leftw, 1))
                last.left = self.map.number_of_nodes()
                self.map.add_edge(self.last_node, self.map.number_of_nodes())
                self.last_node = self.map.number_of_nodes()

        elif self.theta == 2:
            left = [self.posex + 2, self.posey]
            left2 = [self.posex + 2, self.posey + 1]
            left3 = [self.posex + 2, self.posey - 1]
            right = [self.posex - 2, self.posey]
            right2 = [self.posex - 2, self.posey - 1]
            right3 = [self.posex - 2, self.posey + 1]
            front = [self.posex, self.posey - 2]

            leftw, rightw, frontw = -1, -1, -1
            if not self.maze[left[0]][left[1]] == 2 and not self.maze[left2[0]][left2[1]] == 2 and not \
            self.maze[left3[0]][left3[1]] == 2:
                leftw = 0
            if not self.maze[right[0]][right[1]] == 2 and not self.maze[right2[0]][right2[1]] == 2 and not \
            self.maze[right3[0]][right3[1]] == 2:
                rightw = 0
            if not self.maze[front[0]][front[1]] == 2:
                frontw = 0

            for node in self.map.nodes(data=True):
                if math.fabs(node[1]['node'].x - self.posex) <= self.tol and math.fabs(
                        node[1]['node'].y - self.posey) <= self.tol:
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

            if not flag and math.fabs(last.y - self.posey) >= self.junc and (
                    not leftw < 0 or not rightw < 0 or frontw < 0):
                self.map.add_node(self.map.number_of_nodes() + 1,
                                  node=Node(self.posex, self.posey, rightw, leftw, self.last_node, frontw, 1))
                last.back = self.map.number_of_nodes()
                self.map.add_edge(self.last_node, self.map.number_of_nodes())
                self.last_node = self.map.number_of_nodes()

        else:
            left = [self.posex, self.posey + 2]
            left2 = [self.posex - 1, self.posey + 2]
            left3 = [self.posex + 1, self.posey + 2]
            right = [self.posex, self.posey - 2]
            right2 = [self.posex - 1, self.posey - 2]
            right3 = [self.posex + 1, self.posey - 2]
            front = [self.posex + 2, self.posey]

            leftw, rightw, frontw = -1, -1, -1
            if not self.maze[left[0]][left[1]] == 2 and not self.maze[left2[0]][left2[1]] == 2 and not \
            self.maze[left3[0]][left3[1]]:
                leftw = 0
            if not self.maze[right[0]][right[1]] == 2 and not self.maze[right2[0]][right2[1]] == 2 and not \
            self.maze[right3[0]][right3[1]]:
                rightw = 0
            if not self.maze[front[0]][front[1]] == 2:
                frontw = 0

            for node in self.map.nodes(data=True):
                if math.fabs(node[1]['node'].x - self.posex) <= self.tol and math.fabs(
                        node[1]['node'].y - self.posey) <= self.tol:
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

            if not flag and math.fabs(last.x - self.posex) >= self.junc and (
                    not leftw < 0 or not rightw < 0 or frontw < 0):
                self.map.add_node(self.map.number_of_nodes() + 1,
                                  node=Node(self.posex, self.posey, self.last_node, frontw, leftw, rightw, 1))
                last.right = self.map.number_of_nodes()
                self.map.add_edge(self.last_node, self.map.number_of_nodes())
                self.last_node = self.map.number_of_nodes()

    def draw_graph(self, graph):
        plt.title('Trajectory Graph')
        pos = nx.get_node_attributes(graph, 'node')
        positions = {}
        lab = {}
        for key, value in pos.items():
            positions[key] = (value.x, value.y)
        for key, value in pos.items():
            lab[key] = (value.x, value.y)
        # for node in graph:
        #     print(graph.node[node]['node'].x, graph.node[node]['node'].y)
        edg = [(u, v) for (u, v, d) in graph.edges(data=True)]
        # pos = graphviz_layout(graph, prog='dot')
        nx.draw_networkx_nodes(graph, positions, label=True, node_size=700)
        nx.draw_networkx_labels(graph, positions, labels=lab, font_size=6)
        nx.draw_networkx_edges(graph, positions, edgelist=edg)
        plt.axis('off')
        plt.show()

    def isJunction(self):
        for node in self.map.nodes(data=True):
            if math.fabs(self.posex - node[1]['node'].x) <= self.tol and math.fabs(
                    self.posey - node[1]['node'].y) <= self.tol:
                return [True, node[1]]
        return [False]

    def getColour(self, image):

        data = decode(image)
        if data != None:
            print(data)
            return "qr"

        data = detectColour(image)
        if data != None:
            print(data)
            return data

        return "white"

    def check(self):
        res, image = self.vidcap.read()
        colour = self.getColour(image)

        while colour == "pink":
            self.stop()
            self.boxp = [True, True, self.posex, self.posey, self.theta]
            res, image = self.vidcap.read()
            colour = self.getColour(image)
        while colour == "lightblue":
            self.stop()
            self.boxlb = [True, True, self.posex, self.posey, self.theta]
            res, image = self.vidcap.read()
            colour = self.getColour(image)
        while colour == "darkblue":
            self.stop()
            self.boxdb = [True, True, self.posex, self.posey, self.theta]
            res, image = self.vidcap.read()
            colour = self.getColour(image)
        while colour == "qr":
            if self.boxqr3[1]:
                if self.boxdb[1]:
                    while colour == "qr":
                        self.stop()
                        self.boxqr5 = [True, True, self.posex, self.posey, self.theta]
                        res, image = self.vidcap.read()
                        colour = self.getColour(image)
                else:
                    self.boxqr5 = [True, False, self.posex, self.posey, self.theta]
                    break
            else:
                if self.boxp[1] and self.boxlb[1]:
                    while colour == "qr":
                        self.stop()
                        self.boxqr3 = [True, True, self.posex, self.posey, self.theta]
                        res, image = self.vidcap.read()
                        colour = self.getColour(image)
                else:
                    self.boxqr3 = [True, False, self.posex, self.posey, self.theta]
                    break


if __name__ == "__main__":
    start = IRC()
    start.create_map()
    while True:
        start.create_map()
        start.junction()
        if start.boxqr3[0] and not start.boxqr3[1] and start.boxp[1] and start.boxlb[1]:
            start.goal(start.boxqr3[2], start.boxqr3[3], start.boxqr3[4])
        elif start.boxqr5[0] and not start.boxqr5[1] and start.boxdb[1]:
            start.goal(start.boxqr5[2], start.boxqr5[3], start.boxqr5[4])
        else:
            start.move()
        start.draw_graph(start.map)
        start.check()
