import xlwt

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('result', cell_overwrite_ok=True)
sheet.write(0, 0, 'abc')
a = '去'
sheet.write(1, 1, a)
book.save(r'f:/result.xls')