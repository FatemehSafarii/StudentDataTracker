from os import remove
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
            class_name.remove(choose)
            break
    else:
        print('please enter a number.')

print(choose, class_name)
with open('Class Info\\Class Name.txt', 'w') as f:
    for line in class_name:
        f.write(line + '\n')
remove('Class Info\\' + choose + '.csv')