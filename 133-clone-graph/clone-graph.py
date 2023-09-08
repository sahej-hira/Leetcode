"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # input - adjacency list

        hashmap = {}                # mapping of old and new nodes to see if a node clone already exists
        def clone(node):            # using dfs
            if node in hashmap:     # if node present in the hashmap
                return hashmap[node]

            # if clone is not present in the hashmap
            copy = Node(node.val)          # calling node constructor that constructs a node
            hashmap[node] = copy            # mapping the old node to its copy

            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy
        return clone(node) if node else None

            

        