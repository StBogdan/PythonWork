#!/bin/python3

import sys


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


t = int(input().strip())
for _ in range(t):
    # Read in graph
    n, m = map(int, (input().split()))

    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, (input().split()))
        graph[a][b] = 1;
        graph[b][a] = 1;
    s = int(input())

    # Check graph
    # for z in range(len(graph)):
    #    print(graph[z][1:])

    # Do bfs
    vis = [-1 for _ in range(n + 1)]
    ref = [0 for _ in range(n + 1)]
    q = Queue()

    for i in range(1, n + 1):
        if graph[s][i] == 1:
            q.enqueue(i)
            ref[i] = s
            vis[i] = 6

    vis[s] = 0
    cn = q.dequeue()
    while cn is not None:
        for k in range(1, n + 1):
            if graph[cn][k] == 1 and vis[k] < 0:
                q.enqueue(k)
                ref[k] = cn
                vis[k] = vis[ref[k]] + 6
        cn = q.dequeue()

    vis.pop(s)  # Pop self
    vis.pop(0)  # Pop extra elem
    print(" ".join(map(str, vis)))
