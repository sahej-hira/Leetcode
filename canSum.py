def cansum(target,nums,memo): 
    if target in memo: 
        return memo[target]
    if target == 0: 
        return True
    if target < 0: 
        return False
    
    for num in nums:
        reminder = target - num
        if cansum(reminder,nums,memo) == True:
            memo[target] = True
            return True
    memo[target] = False
    return False

print(cansum(7,[2,3],{}))# True
print(cansum(8,[2,3,5],{})) # True
print(cansum(300,[7,14],{})) # False