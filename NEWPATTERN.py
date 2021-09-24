k=int(input('enter height:'))
k-=1
i=1
name=input('enter name:')
for letter in name:
    print(' '*k,end='')
    k-=1
    print(i*letter)
    i+=2
    if k==-1:
        break

