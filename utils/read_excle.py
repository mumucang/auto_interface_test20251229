import os.path

import openpyxl

from config import datas_path


class ReadExcel:

    @staticmethod
    def read_excel(file_path, sheet_name):
        """

        :param file_path:
        :param sheet_name:
        :return:
        """
        datas=[]
        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb[sheet_name]
            for row in sheet.iter_rows(min_row=2):
                data= tuple([i.value for i in row])
                datas.append(data)
        except Exception as e:
            print(e)

        return datas

if __name__ == '__main__':
    ReadExcel.read_excel(os.path.join(datas_path, "autointerface.xlsx"),"logindata")

