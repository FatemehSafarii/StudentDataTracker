from os import system
with open('Class Info\\Class Name.txt', 'r') as f:

    class_name = []
    iteration = 1
    for line in f.readlines():
        line = line.rstrip()
        print(str(iteration) + '. ' + line)
        class_name.append(line)
        iteration += 1
while True:
    choose = input('Which class do you want to attendance? (Enter a number) ').rstrip().lstrip()
    if choose.isdigit():
        choose = int(choose) - 1
        if not 0 <= choose < len(class_name):
            print('Please enter correct number.')
        else:
            choose = class_name[choose]
            system('cls')
            break
    else:
        print('please enter a number.')

body = ''
with open('Class Info\\' + choose + '.csv', 'r') as f:
    for line in f.readlines():
        line = line.rstrip()
        body += line
        name = ' '.join(line.split(',')[:2])
        while True:

            att = input(name + ' (P/A) ').rstrip().lstrip().lower()
            if att == '0' or att == 'a':
                body += 'A,-,-,0,\n'
                system('cls')
                break
            elif att == '1' or att == 'p':
                body += 'P,-,-,0,\n'
                system('cls')
                break
            else:
                print('Please enter P (Present) or A (Absent).')
with open('Class Info\\' + choose + '.csv', 'w') as f:
    f.write(body)
