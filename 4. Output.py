import xlwt
from os import mkdir
from os.path import isdir
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
            break
    else:
        print('please enter a number.')

data = []
with open('Class Info\\' + choose + '.csv', 'r') as f:
    for line in f.readlines():
        line = line.rstrip().split(',')[:-1]
        temp = line[:2]
        del line[:2]
        for i in range(len(line) // 4):
            temp.append(line[:4])
            del line[:4]
        data.append(temp)

style_session = xlwt.easyxf('font: name Times New Roman, bold on; align: vert centre, horiz centre;'
                            ' borders: left thin, right thin, top thin, bottom thin;'
                            ' pattern: pattern solid, fore_colour light_green;')
style_name = xlwt.easyxf('font: name Times New Roman, bold on; align: vert centre, horiz centre;'
                         ' borders: left thin, right thin, top thin, bottom thin;'
                         ' pattern: pattern solid, fore_colour ivory;')
style_normal = xlwt.easyxf('font: name Times New Roman; align: vert centre, horiz centre;'
                           ' borders: left thin, right thin, top thin, bottom thin')
style_gray = xlwt.easyxf('font: name Times New Roman, bold on; align: vert centre, horiz centre;'
                         ' borders: left thin, right thin, top thin, bottom thin;'
                         ' pattern: pattern solid, fore_colour gray25;')

wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet 1')

ws.write_merge(0, 1, 0, 0, 'Name', style_name)
ws.write_merge(0, 1, 1, 1, 'Family Name', style_name)
for j in range(len(data[0]) - 2):
    z = j
    j = j * 4 + 2
    ws.write_merge(0, 0, j, j + 3, 'Session %s' % (z + 1), style_session)
    ws.write(1, j, 'Att.', style_gray)
    ws.write(1, j + 1, 'Ho.', style_gray)
    ws.write(1, j + 2, 'Wr.', style_gray)
    ws.write(1, j + 3, 'Pos.', style_gray)
for j in range(len(data)):
    ws.write(j + 2, 0, data[j][0], style_normal)
    ws.write(j + 2, 1, data[j][1], style_normal)
    for k in range(len(data[j]) - 2):
        z = k
        k = k * 4 + 2
        ws.write(j + 2, k, '✔' if data[j][z + 2][0] == 'P' else '✖', style_normal)
        if data[j][z + 2][1] != '-':
            ws.write(j + 2, k + 1, '✔' if data[j][z + 2][1] == '1' else '✖', style_normal)
        else:
            ws.write(j + 2, k + 1, '-', style_normal)
        if data[j][z + 2][2] != '-':
            ws.write(j + 2, k + 2, '✔' if data[j][z + 2][2] == '1' else '✖', style_normal)
        else:
            ws.write(j + 2, k + 2, '-', style_normal)
        ws.write(j + 2, k + 3, '' if data[j][z + 2][3] == '0' else int(data[j][z + 2][3]), style_normal)

ws.col(0).width, ws.col(1).width = 6000, 6000
if not isdir('Outputs'):
    mkdir('Outputs')
wb.save('Outputs\\' + choose + '.xls')
