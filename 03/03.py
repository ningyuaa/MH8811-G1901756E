#---------------------------------Define 01 program----------------------------
def function_1():
    print("Hello,world!") 
#---------------------------------Define 02-1 program---------------------------
def function_2():
    nam = input('who are you?')
    print('Hello,',nam+'!')
#---------------------------------Define 03-1 program----------------------------
def function_3():
    C = input('Celsius Temperature')
    c = float(C)
    F = c*1.8+32
    print(F)

while True:
    answer=input('Please answer 1, 2 or 3 to choose one of these sub-programs as below\n1. "Hello,world!"program: enter 1 to receive a simple greeting\n2. Customized "Hello,world!" program: enter 2 to receive a customized greeting with your name\n3. "Temperature interchange"program: enter 3 to change Celsius Temperature into Fahrenheit Temperature\nOr key in any other word to exit')
    if answer == '1':
        function_1()
        continue
    if answer == '2':
        function_2()
        continue
    if answer == '3':
        function_3()
    else:
        print('Thank you!')
        break

#What else can make a function?
#For example, I can make a function of sum of 2 variables
#def sum(a,b):
#    return a + b
