answerList = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
correctAns = 0
wrongAns = 0
userAns = []
incorrectAns = [] 

user_input = input("Put your answer script: ")
count = 0

if user_input.endswith(".txt"):
    file = open(user_input, 'r')
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
    count += 1
print('number of correct answers=',correctAns)
print('number of wrong answers=',wrongAns)
if correctAns<15:
    print('you lost')
else:
    print('you won')

