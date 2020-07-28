pa= str(input('enter a password'))
sym=str("!@#$%&*()")
symLen=len(sym)
strlen=len(pa)
number="0123456789"
numLen=len(number)
cck=sck=nck=0
for a in range(0,strlen):
    if pa[a].isupper():#capital letter check

        cck=1


    for b in range(0,symLen):
        if sym[b]==pa[a]: #sysbol check

            sck=1

        if number[b] == pa[a]:#number check

            nck=1



while strlen>8:
    if cck==1 and sck==1 and nck==1:
        print('password accepted')
        break
    else:
        print('print please enter a capital letter , number,symbol')
        pa= str(input('enter a password'))

        for a in range(0,strlen):
              if pa[a].isupper():#capital letter check

                 cck=1


    for b in range(0,symLen):
        if sym[b]==pa[a]: #sysbol check

            sck=1
            if number[b] == pa[a]:#number check
              nck=1
              break

