from openpyxl import load_workbook
def excel_to_list(excelPath, sheetName):
    wb = load_workbook(excelPath)
    sheet = wb[sheetName]
    data_list = []
    title_list = []
    for cell1 in sheet['1']:
        title_list.append(cell1.value)
    for row in list(sheet.rows)[1:]:
        row_list = []
        for cell in row:
            row_list.append(cell.value)
            dict_data = dict(zip(title_list, row_list))
        data_list.append(dict_data)
        return data_list

def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data

if __name__== '__main__':
    data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")
    case_data = get_test_data(data_list, 'test_user_login_normal')
    print(data_list)

