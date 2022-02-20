import xlwt

workbook = xlwt.Workbook(encoding='utf-8')  # Create workbook object
worksheet = workbook.add_sheet('link')  # Create work sheet
# worksheet.write(0, 0, 'helloWorld!')
# workbook.save('hello.xls')
# 添加一个乘法口诀表
for i in range(0, 9):
    for j in range(0, i):
        worksheet.write(i, j, "%d * %d = %d" % (i + 1, j + 1, (i + 1) * (j + 1)))
        workbook.save('hello.xls')
