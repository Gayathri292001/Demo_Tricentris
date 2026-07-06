import openpyxl

def get_data():
    workbook = openpyxl.load_workbook("C://Users//Admin//PycharmProjects//Selenium_E26//Demo_Tricentis_Framework//test_data//login_data.xlsx")
    sheet = workbook['Sheet1']
    data=[]
    for i in sheet.iter_rows(min_row=2, values_only=True):
        data.append(i)
    return data


#Not required
# data = get_data()
# for i in data:
#     print(i)