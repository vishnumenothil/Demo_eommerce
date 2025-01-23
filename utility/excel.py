from xlrd import open_workbook
# xlrd is a Python library used to read data from Excel files 
# (specifically .xls files, which are in the older Excel binary format). It was widely used before

def read_locator(sheetname): 
    wb=open_workbook("test_data/objects.xls")
    ws=wb.sheet_by_name(sheetname)
    used_rows=ws.nrows
    data={}
    for i in range(1,used_rows):
        rows=ws.row_values(i)
        print(rows)
        data[rows[0]]=(rows[1],rows[2])
    
    return data  

def read_headers(testcases,sheetname):
    wb=open_workbook("test_data/testdata.xls")
    wc=wb.sheet_by_name(sheetname)
    used_row=wc.nrows
    for i in range(0,used_row):
         rows=wc.row_values(i)
        #  print(rows)
         if rows[0]==testcases:
             _headers=wc.row_values(i-1)
             _headers=[_header for _header in _headers if _header.strip() ]
            #  print(_headers)
                
             break
    return ",".join(_headers[2:])


def read_data(test_case_name,sheetname):
    data=[]
    wb=open_workbook("test_data/testdata.xls") 
    wc=wb.sheet_by_name(sheetname)
    used_rows=wc.nrows
    for i in range(0,used_rows):
        rows=wc.row_values(i)
        if rows[0]== test_case_name:
            temp_data=[item for item in rows if str(item).strip()]
            if temp_data[1].upper()== 'YES' :
                data.append(tuple(temp_data[2:]))
    return data




    # _locator=read_locator('paymentpage')

# print(read_headers('test_login_positive',"smoke"))
# print(read_data('test_login_positive',"smoke"))
print(read_headers("test_payment","shopping1"))

# p=read_locator("paymentpage")
# print(p)
print("*"*50)
print(read_data("test_payment","shopping1"))
# print(p['txt_quat'])
# for i,j in p.items():
#     print(i,j)