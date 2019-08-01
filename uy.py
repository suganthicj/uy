x11=int(input())
l=list(map(int,input().split()))
m=100000
for i in range(0,x11-1):
	for j in range(i+1,x11):
		z11=l[j]-l[i]
		if z11<0:
			z11=z11*-1
		if z11<m and z11!=0:
			m=z11
print(m)
