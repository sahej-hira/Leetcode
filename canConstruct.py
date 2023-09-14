def canConstruct(target, wordset,memo):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    
    for word in wordset:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if (canConstruct(suffix,wordset,memo)) == True:
                memo[target] = True
                return True
    memo[target] = False
    return False



print(canConstruct("suzuki",["su","u","suz","uki","k"],{})) # True
print(canConstruct("dang",["aa","ang","da","d","na"],{})) # True
print(canConstruct("nokia",["nok","ono","n","a","ki"],{})) # False
    