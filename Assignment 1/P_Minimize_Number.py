N= int(input())

lt= list(map(int,input().split()))

def solve(lst):
    opt=0
    while 1:
        for i in lst:
            if i%2!=0:
                return opt
        opt+=1
        lst=list(map(lambda v:v/2,lst))

print(solve(lt))

 