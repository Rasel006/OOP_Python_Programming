
S= input()
N=len(S)

Start =0
Total=0
list=[]

for i in range(0,N):
    left= S[Start:i+1]
    right= S[i+1:N-1]
    left_left=left.count('L')
    left_right=left.count('R')
    right_left=right.count('L')
    right_right=right.count('R')
    if left_left==left_right:
        Total+=1
        list.append(left)
        Start=i+1
print(Total)
for i in list:
    print(i)
    
    