
L,S=map(int,input().split())
#S=eval(input('起始S = '))

n=S
t=0

while  n!=L:
    if n>L:
        n=n-2
        t=t+1
        #print('n＝',n)
        #print('次數＝',t)

    elif n<L:
        n=n+5
        t=t+1
        #print('n＝',n)
        #print('次數＝',t)

print(t)





