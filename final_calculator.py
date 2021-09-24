from calculator.calc import *
def my_calc(expression):
    i=1
    while True:
        i+=1
        j=0
        if ('(' not in expression) and (')' not in expression):
            print('=',calculate(expression))
            break
        while  j+i<len(expression):
            if expression[j]=='(' and expression[j+i]==')':
                calculated=str(calculate(expression[j+1:j+i]))
                l,_,r=expression.partition(expression[j:j+i+1])
                expression=l+calculated+r
            j+=1
while True: 
    text=input('type:')
    if text=='off':
        print('calculator is turning off')
        break    
    my_calc(text)
    