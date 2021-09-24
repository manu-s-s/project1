lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
K=input('enter string: ')
string=''
for alphabet in K:
    if alphabet in lower:
        string+=alphabet
    elif alphabet in upper:
        string+=lower[upper.index(alphabet)]
    else:string+=alphabet
print(string)