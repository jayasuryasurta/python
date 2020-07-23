z='temp'#var initilazation
while z!= 'exit':
    z=str(input('enter a string'))
    a=str(input('enter letter'))
    count=int(0)#counting varible
    for d in z:
        if d==a:
         count=count+1
    print(count)




