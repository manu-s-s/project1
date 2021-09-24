k=['eric idle','john cleese','graham chapman']
j=[42,76,9]
p=[]
i=0
for item in k:
    print(k[i][0].upper()+k[i].split(' ')[1][:2:].upper()+str(j[i]))
    i+=1
