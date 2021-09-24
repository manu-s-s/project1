
n=int(input('enter no of elements: '))
array=[]
print("enter elements")
for e in range(n):
    array.append(int(input('>>')))
print(f'the result is new array={list(set(array))}')
  