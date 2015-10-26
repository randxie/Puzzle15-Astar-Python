__author__ = 'randxie'

from SupportFun import NodeRepr, GetNeighbor, Manhatan, GenImage
import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
from heapdict.heapdict import *

class PuzzleSolver():
    def __init__(self, start, dest):
        self.start = start
        self.dest = dest

    def SolvePuzzle(self):
        start_time = time.time()
        print 'Start Solving Puzzle'
        # use string to represent states
        start = self.start
        dest = self.dest
        dest_repr = NodeRepr(dest)
        start_repr = NodeRepr(start)

        # set up initial lists
        dist_list = {}
        color_list = {}
        est_list = {}
        array_list = {}
        search_parent = {}

        # initial start states
        color_list[start_repr] = 1                  # stores node color
        dist_list[start_repr] = 0                   # stores distance to start node
        est_list[start_repr] = Manhatan(start)      # stores estimation to destination node
        array_list[start_repr] = start              # stores np.array of states
        search_parent[start_repr] = 0               # store search parent for finding final path

        # use heapdict (supports decrease key), from website https://github.com/DanielStutzbach/heapdict
        heap_q = heapdict()
        heap_q[start_repr] =  (dist_list[start_repr] + est_list[start_repr])

        # follow the handwritten note from Dr.Dimitrov Ned, ut austin
        while heap_q:
            u = heap_q.popitem()
            if (u[0]==dest_repr):
                break
            next_node = GetNeighbor(array_list[u[0]])
            for v in next_node:
                tmp = NodeRepr(v)
                if tmp not in color_list:
                    color_list[tmp] = 1
                    search_parent[tmp] = u[0]
                    dist_list[tmp] = dist_list[u[0]] + 1
                    est_list[tmp] = Manhatan(v)
                    array_list[tmp] = v
                    heap_q[tmp] = (dist_list[tmp] + est_list[tmp])

                elif color_list[tmp] == 1:
                    if dist_list[tmp] > (dist_list[u[0]]+1):
                        search_parent[tmp] = u[0]
                        dist_list[tmp] = dist_list[u[0]] + 1
                        heap_q[tmp] = dist_list[tmp] + est_list[tmp]

                elif color_list[tmp] == 2:
                    if dist_list[tmp] > (dist_list[u[0]]+1):
                        search_parent[tmp] = u[0]
                        dist_list[tmp] = dist_list[u[0]] + 1
                        heap_q[tmp] = dist_list[tmp] + est_list[tmp]
                        color_list[tmp]=1
            color_list[u[0]]=2

        # find out movement from start to destination
        position = dest_repr
        self.movement = []
        self.movement.append(array_list[dest_repr])
        count = 0
        while search_parent[position]!=0:
            tmp = search_parent[position]
            self.movement.append(array_list[tmp])
            position = NodeRepr(tmp)
            count = count + 1
        print 'total step: %d' %(count)
        print("Takes %s seconds to solve the puzzle" % (time.time() - start_time))
        self.movement.append(array_list[start_repr])
        self.movement =  self.movement[::-1]

    def AnimateMove(self):
        fig = plt.figure()
        animate_plot = []
        for mtx_i in self.movement:
            im = plt.imshow(np.array(GenImage(mtx_i)))
            animate_plot.append([im])
        ani = animation.ArtistAnimation(fig, animate_plot, interval=500, blit=True, repeat=False)
        plt.axis('off')
        ani.save('puzzle_solution.gif', writer='imagemagick', fps=1.5)
        plt.show()
