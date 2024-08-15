from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0

        for i in bills:
            #print(i,fives,tens)
            if i == 5:
                fives += 1
            elif i == 10 and fives:
                fives -= 1
                tens += 1
            elif i == 20 and tens and fives:    # no need to add
                fives -= 1
                tens -= 1
            elif i == 20 and fives >= 3:       # no need to add
                fives -=3
            else:
                return False
        return True
            



        ''' drawback: creation of dictionary will take up more space
        # creation of a dict:
        dict = defaultdict(int)

        for i in range(len(bills)): # traverse over bills list
            # see if you have change for the amount user gives:
            to_return = bills[i] - 5    # amount to return to the customer
            while to_return > 0:    # to_return amount can be changed
                print(i,to_return,max(dict.keys()))
                to_return = to_return - max(dict.keys())    # update to_return amount


            if to_return < 0:
                return False    # false when we can't return change for a given amount.

            # add the received amount to dict: 
            if bills[i] in dict:
                dict[bills[i]] += 1
            else:
                dict[bills[i]] = 1

        return True
        '''
            

        