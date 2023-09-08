class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # hashmap with course and prerequisite info
        # visit set - to detect cyle


        prevmap = {i:[] for i in range(numCourses)} #hashmap
        for crs, pre in prerequisites:
            prevmap[crs].append(pre)

        visited = set()                             # set
        def dfs(crs):
            if crs in visited:
                return False
            if prevmap[crs] == []:
                return True
            
            # if crs not present in prevmap
            visited.add(crs)
            for pre in prevmap[crs]:    
                # using dfs on each node of course prerequisites to figure out if its valis
                if not dfs(pre):     # if dfs returns false => course can't be completed
                    return False
            visited.remove(crs)     # if dfs returns true =>all prerequisites can be completed
            prevmap[crs] = []       # clean those prereq from the prevmap since they can be completed so we don't need to recalculate each time
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        