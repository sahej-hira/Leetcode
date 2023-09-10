class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
# undirectional graph => cycles => recursion limit extended due to infinite loop!

        # simply apply dfs/bfs
        # if node is found: return True
        # else return False

        # creating adjacency list:
        graph = {}

        # create list for each node
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            # append adjacent node to the lists of each node
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        print(graph)


        visited = [False for i in range(n)]     # list
        # instead pf list hashset could be used would improve the time and space complexity!
        
        curr = source


        def dfs(edges,curr,destination):
            if curr == destination:
                return True

            # if curr is visited
            if visited[curr] == True:
                return False
            
            # If curr is not visited 
            visited[curr] = True

            # recursive function
            for neighbour in graph[curr]:
                if dfs(edges, neighbour,destination) == True:
                    return True
            return False

        return dfs(edges,curr,destination)
        