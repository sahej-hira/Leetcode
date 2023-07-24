class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[None]*(n)
        #print(answer)
        i=1
        
        while i<n+1:
            
            #print(i%3)
            if (i%3==0 and i%5==0):
                answer[i-1]="FizzBuzz"
            elif i%3==0:
                answer[i-1]="Fizz"
            elif i%5==0:
                answer[i-1]="Buzz"
            else:
                answer[i-1]=str(i)
            i+=1
            
        #print(answer)
        return answer












