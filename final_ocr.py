answerList=[]
answer_key=open('answerkey.txt','r')
key_contents=answer_key.read().splitlines()
y=0
while y<20:
    key=key_contents[y].split('.')
    y+=1
    answerList.append(key[1].strip())
n=int(input('enter number of students '))
variable=1
while variable<=n:
    correctAns = 0
    wrongAns = 0
    userAns = []
    count=0 
    file = open(f'exam{variable}.txt', 'r')
    contents = file.read().splitlines()
    i=0
    while i < 20:
        answer = contents[i].split(".")
        i += 1
        userAns.append(answer[1].strip())
    for i in answerList:
        if i == userAns[count]:
            correctAns += 1
        else:
            wrongAns += 1
        count+=1
    with open('marklist of students.txt','a') as f:
        f.write(f'{variable}.{correctAns}/20')
        f.write('\n')
    f.close()
    variable+=1
    