def funct(j,i,n):

    while len(j)<n:
        j.append(j[i]+j[i+1])
        i+=1
    print(j)

a=[0,1]
n=int(input('enter no of elements:'))
funct(a,0,n)
