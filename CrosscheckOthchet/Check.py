import os
import pandas as pd
url= r'C:/Users/STARLINECOMP.KZ/Downloads/Отчёт за 2 недели/'
files = os.listdir(url)

df_total = pd.DataFrame()
all_data = {

}
for file in files:
    if file.endswith('.xls'):
        excel_file = pd.ExcelFile(url + file)
        sheets = excel_file.sheet_names
        for sheet in sheets:
            frame = pd.DataFrame()
            df = excel_file.parse(sheet_name = sheet)

            frame = frame.append(df)
            all_data[sheet] = frame
            #frame.to_excel('combined_file.xls')




print(all_data)
# df_total.to_excel('combined_file.xls')

