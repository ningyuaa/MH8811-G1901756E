import PSG
n = int(input('how many numbers do you want to have in your password?'))
while n<4:
    print('Please enter a number larger than 4')
    n = int(input('how many numbers do you want to have in your password?'))

PSG = PSG.genPassword(n)
print (PSG)
