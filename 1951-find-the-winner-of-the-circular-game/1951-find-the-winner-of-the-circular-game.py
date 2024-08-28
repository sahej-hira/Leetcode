class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = []                              # queue
        # insertion of all the elements in a queue:
        for i in range(1,n + 1):
            #print("here",q)
            q.append(i)
        # the queue is filled with all the n elements
        #print(q)
        i = 0
        while n > 1:                   # until there is no more than 1 element in the queue
            #print("here2",q,n)
            i += 1
            popped_el= q.pop(0)
            if i == k:                       # if i == k do NOT add the element back into the queue
                i = 0
                n = n - 1
            else:                           # else add the popped element back into the queue
                q.append(popped_el)
        return q[0]                         # return the last element left in the queue
