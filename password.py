sym=str("!@#$%&")
cck=sck=nck=0
while cck<1 | sck<1 | nck<1:
    pa= str(input('enter a password'))
    strlen=len(pa)
    for a in range(0,strlen):
        if pa[a].isupper():#capital letter check
            cck=1
            print('d1')
        if(pa[a].isdigit()):
            nck=1
            print('d3')
        for b in range(0,len(sym)):
            if sym[b]==pa[a]: #sysbol check
                sck=1
                print('d2')


    if cck==1 and sck==1 and nck==1:
        print('password accepted')
        break
    else:
        print('print please enter a capital letter , number,symbol')
        continue


