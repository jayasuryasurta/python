
def IN():
    global firstNum
    global secondNum
    firstNum =input('\033[1;32;47m enter first number\n')
    if(firstNum.isnumeric()):
        float(firstNum)
        secondNum=input('\033[1;32;47m enter second number\n')
        if(firstNum.isnumeric() and secondNum.isnumeric()):
           float(secondNum)
        else:
            print('\033[1;32;41m  pleae enter a valid Integer \n')
            IN()
    else:
        print('\033[1;32;41m  pleae enter a valid Integer \n')
        IN()

def calc(operation):
    if operation == 'a'   :
        print('addtion')
        IN()
        z= format(firstNum+secondNum)
        print (z)
    elif operation == 's' :
        print('subtraction')
        IN()
        z= format(firstNum-secondNum)
        print (z)
    elif operation== 'm':
        print('multipcation')
        IN()
        z= format(firstNum*secondNum)
        print (z)
    elif operation== 'd':
        print('division')
        IN()
        z= format(firstNum/secondNum)
        print (z)
    elif operation== 'e':
        print('bye')
    else :
        print('please enter a valid option')


print('welcome')
operation=input("enter a,s,m,d or e to exit")
temp=0
while operation != "e":
    if temp==1:
        operation=input("enter a,s,m,d or e to exit")
    calc(operation)
    temp=1





