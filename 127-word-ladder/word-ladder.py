class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # formatlities:

        # check if endword exists in wordlist, if not => there exists no path from the begining word to the end word.
        if endWord not in wordList:
            return 0

        # nei: list of neighbours
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        # creation of key for the adjacency list and creation of an adjacency list
        for word in wordList:
            for j in range( len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)   # add neighbours of all the words belonging to the same pattern, using patterns as keys.
        # adjacency list creation: DONE

        # traversing throught the adjacency list: using BFS
        visit = set([beginWord])           # visit set to keep track of all the visited nodes
        q = deque([beginWord])
        res = 1                 # output, no. of layers until we reach the endword

        # we're gonna go layer-by-layer until we reach the endword (that is surely present in the list if we've come this far) - conditional statement at the beginning

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):   # finding neighbours:
                    # transorming the word to its patter.
                    pattern = word[:j] + "*" + word[j+ 1:]

                    # finding all the words that are present with the similar pattern, as the word (we just found the pattern for)
                    for neighbour in nei[pattern]:
                        # so as to not take the same "word" multiple times, we make sure the neighbour words are not present in the visit set.
                        if neighbour not in visit:
                            visit.add(neighbour)
                            q.append(neighbour)


            res += 1
        print(res)
        # if still a pattern is not found:
        return 0


    
        
        