
testcase = int(input())
for num in range(testcase):
    N=input().strip()
    
    digits = list(N)
    digits.reverse()
    
    print(" ".join(digits))