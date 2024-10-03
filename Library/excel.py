from xlrd import open_workbook

def read_locators(sheetname):
    wb = open_workbook()
    ws = wb.sheet_by_name(sheetname)
