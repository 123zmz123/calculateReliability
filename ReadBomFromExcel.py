import xlrd
import re

from xlrd import *

class MyBom:
    __BomType = "xls"
    __BomPath = ""
    __Type_Map_Of_Capacitor = {}
    __Type_Map_Of_Resistor = {}

    def __init__(self,Input_Type,Input_Path):
        self.__BomType = Input_Type
        self.__BomPath = Input_Path

    def read_message_in_bom(self):
        Excel = xlrd.open_workbook(self.__BomPath)
        # print(Excel.sheet_names()[0])
        Bom = Excel.sheet_by_name(Excel.sheet_names()[0])
        print(Bom.nrows)
        print(Bom.ncols)
        for i in range(11,84):
            if "电容" in Bom.col_values(1)[i]:
                print(Bom.col_values(3)[i], Bom.col_values(8)[i],"类别为电容")
                print("电容值为",self.__Extract_Capacitor_Value(Bom.col_values(3)[i]))
                print(Bom.col_values(1)[i])
            elif "电阻" in Bom.col_values(1)[i]:
                print(Bom.col_values(3)[i], Bom.col_values(8)[i],"类别为电阻")
                print("电阻值为",self.__Extract_Resister_Value(Bom.col_values(3)[i]))
            else:
                print(Bom.col_values(3)[i], Bom.col_values(8)[i])

    def __Extract_Capacitor_Value(self,Capacitor_Message):
        return re.findall("/(.*[u,n,p,mF])",str(Capacitor_Message))
    def __Extract_Resister_Value(self,Resister_Message):
        return re.findall(".*[R,K,M,r,k,m]",str(Resister_Message))










if __name__ == "__main__":
    TheExcel = MyBom("xls","C:\\Users\\lenovo\\Desktop\\SH001T初版BOM.xls")
    TheExcel.read_message_in_bom()


