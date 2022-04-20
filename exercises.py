#random module importing
import random

#Ask for number of problems
kol = int(input('How many problems do you want to solve: '))

#List for the number of correct answers
right=[]

#List for the number of wrong answers
wrong=[]
for i in range(kol):
    a = random.randint(0, 6)   #random number
    b = random.randint(0, 6)   #random number
    try:
        c = int(input(str(a) + ' * ' + str(b) + ' = '))
        if a * b == c:
            print('Right.')
            right.append(c)   #If correct, include in the list of correct answers
        else:
            print('Wrong.')
            wrong.append(c)   #If incorrect, include in the list of incorrect answers
    except ValueError:   #ValueError exception - if the wrong data type was entered
        print('Wrong data type.')
        wrong.append(1)   #The ValueError exception is also an error, we include it in the list of incorrect answers
print('')
print('Number of correct answers: ' + (str(len(right))))
print('Number of wrong answers: ' + (str(len(wrong))))
print('')


#Grading system on a five-point scale, rounds the grade to an integer
if round(len(right) / kol * 5) == 5:
    print('Your mark: 5')
elif round(len(right) / kol * 5) == 4:
    print('Your mark: 4')
elif round(len(right) / kol * 5) == 3:
    print('Your mark: 3')
elif round(len(right) / kol * 5) <=2:
    print('Your mark: 2')
