
N=int(input())
lst=list(map(int,input().split()))
result= 0
temp=lst

for i in temp:
    if temp.count(i)!=i:
        if temp.count(i)<i:
            result+= temp.count(i)
            while i in temp:
                temp.remove(i)

        elif temp.count(i)>i:
            result+= temp.count(i)-i
            while i in temp:
                temp.remove(i)
print(result)