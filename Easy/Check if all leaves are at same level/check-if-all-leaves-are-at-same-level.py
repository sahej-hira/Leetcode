#User function Template for python3

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        #Code here
        if not root:
            return True  # Empty tree, so all leaf nodes are at the same level
        
        # Perform BFS traversal
        queue = deque([(root, 0)])  # Queue to store nodes along with their levels
        leaf_level = None  # Level of the first encountered leaf node
    
        while queue:
            node, level = queue.popleft()
    
            # If the current node is a leaf node
            if not node.left and not node.right:
                # If it's the first leaf node encountered, record its level
                if leaf_level is None:
                    leaf_level = level
                # If leaf node is not at the same level as previously encountered leaf nodes, return False
                elif level != leaf_level:
                    return False
            
            # Add left and right children to the queue along with their levels
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
    
        # If all leaf nodes are at the same level, return True
        return True

        # res = 1         # Assume all the leaf nodes are at the same level for starters
       
        # def dfs(node,depth, level):
          
        #     if not node:
        #         return
        #     if res == 0:
        #         return 
        #     if level == -1:
        #         level = depth
        #     elif level != depth:
        #         res = 0
                
        #     #print(ret)
        #     dfs(node.left, depth + 1,level)
        #     dfs(node.right, depth + 1,level)
            
            
        # dfs(root, 0, - 1)    
        # return res        
        
        
        # depth : is the depth/height of each node from root node
        # level: level stores the level of the first leaf node to be compared with all the other leaf nodes.



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        if Solution().check(root):
            print(1)
        else:
            print(0)



# } Driver Code Ends