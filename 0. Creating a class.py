from os.path import isfile
from os import system
from os import mkdir
from os.path import isdir
if not isdir('Class Info'):
    mkdir('Class Info')
while True:
    class_name = input('Name of the class: ').rstrip().lstrip()
    if isfile('Class Info\\' + class_name + '.csv'):
        print('You have a class with this name.\n')
    else:
        break
if not isfile('Class Info\\Class Name.txt'):
    with open('Class Info\\Class Name.txt', 'w'):
        pass
with open('Class Info\\Class Name.txt', 'a') as f:
    f.write(class_name + '\n')
with open('Class Info\\' + class_name + '.csv', 'w') as f:

    while True:
        system('cls')
        print('Put -1 instead of name when you\'re done.')
        name = input('Name: ').lower().rstrip().lstrip().title()
        if name == '-1':
            break
        surname = input('Family name: ').lower().rstrip().lstrip().title()
        while True:
            agree = input('"' + name + ' ' + surname + '" do you agree? (Y/N) ').rstrip().lstrip().lower()
            if agree == 'y' or agree == 'yes':
                f.write(name + ',' + surname + ',\n')
                print()
                break
            elif agree == 'n' or agree == 'no':
                print()
                break
            else:
                print('Please enter Y or N.')
