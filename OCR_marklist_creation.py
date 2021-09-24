answerList = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
with open('answerkey.txt','a') as f:
    k=1
    for item in answerList:
        f.write(f'{k}.{item}\n')
        k+=1

