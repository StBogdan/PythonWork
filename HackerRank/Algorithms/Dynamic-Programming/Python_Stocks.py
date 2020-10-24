"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


leaf_of_bool = lambda x: Node(x, True, None, None, None, None)
subdiv_of_bool = lambda x: Node(x, False, leaf_of_bool(x), leaf_of_bool(x), leaf_of_bool(x), leaf_of_bool(x))


def udlr(quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
    tL = Solution.intersect(quadTree2.topLeft, quadTree1.topLeft)
    tR = Solution.intersect(quadTree2.topRight, quadTree1.topRight)
    bL = Solution.intersect(quadTree2.bottomLeft, quadTree1.bottomLeft)
    bR = Solution.intersect(quadTree2.bottomRight, quadTree1.bottomRight)
    return tL, tR, bL, bR


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)
        else:
            if quadTree1.isLeaf:
                tempNode = subdiv_of_bool(quadTree1.val)
                otherNode = quadTree2
            elif quadTree2.isLeaf:
                tempNode = subdiv_of_bool(quadTree2.val)
                otherNode = quadTree1
            else:
                tempNode = quadTree1
                otherNode = quadTree2

            topLeft, topRight, bottomLeft, bottomRight = udlr(tempNode, otherNode)

            if (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val and (
                    topLeft.val == True or topLeft.val == False)):
                return leaf_of_bool(topLeft.val)
            return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)
