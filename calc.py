
def IN():
    global firstNum
    global secondNum
    firstNum =float(input('enter first number'))
    secondNum=float(input('enter second number'))

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





