

import pandas as pd

"""
读取excel文件
    参数：文件地址excelUrl
    返回类型：
"""
class ReadExccel:
    def __init__(self):
        pass
    def excelReadMethod(self):
        # 读取 Excel 文件
        df = pd.read_excel('ceshi01.xlsx', sheet_name='Sheet1')

        # 打印数据框的前几行
        print(df.head())

        # 获取某一列数据
        column_data = df['Column_Name']

        # 循环遍历每一行
        for index, row in df.iterrows():
            print(row['Column_Name'])

        # 关闭文件
        df.close()
readExcel = ReadExccel()
readExcel.excelReadMethod()