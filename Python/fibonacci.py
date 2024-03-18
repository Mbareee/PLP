phi = (1 + (5)**0.5) / 2
n = int(input("How many terms of the Fibonacci sequence would you like to see? "))
result = []
def fibonaci(n):
    for term in range(n):
        ans1 = (((phi)**term) - ((1-phi)**term)) / (5)**0.5
        result.append(int(ans1))
    print(result)    

        
    

fibonaci(n)