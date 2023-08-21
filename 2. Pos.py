from os import system


def show(name, space):
    string = ''
    for k in range(len(name)):
        string += str(k + 1) + '. ' + name[k][0] + ' ' * (space - len(name[k][0]) + 2) + '+' * name[k][1] + '\n'
    return string


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

data, names, maximum = [], [], 0
with open('Class Info\\' + choose + '.csv', 'r') as f:
    for line in f.readlines():
        line = line.rstrip().split(',')
        data.append(line)
        temp = ' '.join(line[:2])
        if len(temp) > maximum:
            maximum = len(temp)
        names += [[temp, int(line[-2])]]

flag = True
while True:
    if flag:
        print(show(names, maximum))
        print('-1 for exit')
    flag = True
    who = input('Please enter number of that person who is gonna get positive: ')
    if who == '-1':
        break
    if who.isdigit():
        who = int(who) - 1
        if not 0 <= who < len(data):
            print('Please enter correct number.')
            flag = False
        else:
            data[who][-2] = str(int(data[who][-2]) + 1)
            names[who][-1] += 1
            system('cls')
    else:
        print('Please enter a number.')
        flag = False

with open('Class Info\\' + choose + '.csv', 'w') as f:
    for d in data:
        f.write(','.join(d) + '\n')
