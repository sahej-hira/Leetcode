class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        # star graph meaning 1 node is common among all the pairs thus we only need to find that 1 pair doesn't matter which pairs we match

        if edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            return edges[0][1]
        elif edges[0][0] ==  edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        