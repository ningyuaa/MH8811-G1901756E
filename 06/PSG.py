import random as rd

def genPassword(n):
    Lletter = 'abcdefghijklmnopqrstuvwxyz'
    Uletter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Number = '0123456789'
    Symbols = '~!@#$%^&*()_+=-`?/\|;:'
    pw = []
    for i in range(0, n):
        if i % 4 == 0:
            pw.append(rd.choice(Lletter))
        if i % 4 == 1:
            pw.append(rd.choice(Uletter))
        if i % 4 == 2:
            pw.append(rd.choice(Number))
        if i % 4 == 3:
            pw.append(rd.choice(Symbols))
    rd.shuffle(pw)
    return (''.join(pw))

if '__name__' == '__main__':
    print(genPassword(12))





    
    
   

