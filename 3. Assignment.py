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
    choose = input('Which class do you want to choose? (Enter a number) ').rstrip().lstrip()
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

while True:
    ass = input('Which type of assignment? (H/W) ').rstrip().lstrip().lower()
    if ass == 'h':
        ass = -4
        system('cls')
        break
    elif ass == 'w':
        ass = -3
        system('cls')
        break
    else:
        print('Please enter H (Homework) or W (Writing).')

names, iteration = '', 0
data = []
with open('Class Info\\' + choose + '.csv', 'r') as f:
    for line in f.readlines():
        line = line.rstrip().split(',')
        line[ass] = '0'
        data.append(line)
        iteration += 1
        names += str(iteration) + '. ' + ' '.join(line[:2]) + '\n'
flag = True
while True:
    if flag:
        print(names)
        print('-1 for exit')
    flag = True
    print('Please enter number of a person who has ', end='')
    who = input('Homework: ' if ass == -3 else 'Writing: ')
    if who == '-1':
        break
    if who.isdigit():
        who = int(who) - 1
        if not 0 <= who < len(data):
            print('Please enter correct number.')
            flag = False

        else:
            data[who][ass] = '1'
            system('cls')

    else:
        print('Please enter a number.')
        flag = False

with open('Class Info\\' + choose + '.csv', 'w') as f:
    for d in data:
        f.write(','.join(d) + '\n')
