##########################
#####   CALCULATOR   #####
##########################
'''Program by Piotr Gołdyś'''


# Imports:
import re
import time
########

run = True
ans = 0
equation = ''
safe = 0
history = ''

#Welcome message / instructions
print('##########################')
print('#####   CALCULATOR   #####')
print('##########################')
print()
print('Hello, human. \nType some calculations!')
print()
print("(HISTORY - type 'h'")
print("(RESTART - type 'r'")
print("( EXIT   - type 'e'")
print("For 'sqrt' use '**(1/2)'")
print('--------------------------------------------------------------------')



def check():    #Checks for special/wrong input
    global ans, run, equation, safe, history

    equation = input()
    if equation == 'e':     #Exit
        print('Goodbye')
        run = False
    elif equation == 'r':   #Restart
        ans = 0
        safe = 0
        history = ''
        equation = ''
    elif equation == 'h':   #History
        print('History: ', history)

    else:   #Checks for wrong inputs and protects from using eval()'s function safe loop
        notsafe = 0
        for x in equation:
            if set('[,.;:{}[&%$@!~]').intersection(equation) or x.isalpha():
                equation = re.sub('[a-zA-Z,.;:{}[&%$@!~]', ' ', equation) #Deletes special/dangerous characters
                safe = 0
                notsafe = 1
            else:
                safe = 1
        if notsafe == 1:
            print('Wrong input!')
            time.sleep(2)


def perform():      #Do maths
    global history, run, ans, equation, safe

    if safe == 1:
        equation = re.sub('[a-zA-Z,.;:{}[&%$@!~]', ' ', equation)
        if ans == 0:    #For the first equation
             if equation[0] == '*' or equation[0] == '/':
                 ans = str(eval('0' + equation))
             else:
                ans = str(eval(equation))
                history += equation + ' '

        else:   #For next equations
             if equation[0].isdigit():
                 print('Wrong input!')
                 time.sleep(2)
             else:
                 ans = str(eval(ans + equation))
                 history += equation + ' '

    if run == True:
        print(ans, end='') #Printing stuff

def program():
    check()
    perform()

while run:
    program()


