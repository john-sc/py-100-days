q1=[8,4,1]
q2=[-4,7,4]
q3=[1,-4,8]
print("q1 size=",len(q1),"content=",q1)

for qi in q1:
	print(qi)
    
print("-----")  
thetuple = ('A','B','C','D','E')
print (thetuple[0])
print(q1[0],q1[1],q1[2])

print("-----")  
idx=0
while idx<len(q1):
    print(q1[idx])        
    idx=idx+1

print("-----")
Q=[q1,q2,q3]
print(len(Q))
print(Q)

print("-----")  
i=0
j=0
while i<len(Q):
    while j < len(q1):
        qi=Q[i]
        print(qi[j],Q[i][j])
        j=j+1
    i=i+1

print("-----tuple------")
tt=((8,4,1),(-4,7,4),(1,-4,8))
i=0
j=0
while i<len(tt):
    while j < 3:
        print(tt[i][j])
        j=j+1
    i=i+1
