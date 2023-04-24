import random
import xlrd
import xlsxwriter
import os

filePath="C:\\Users\\mecaj\\Documents\\Future\\PYTHON\\consulta.xls"
openFile=xlrd.open_workbook(filePath);
sheet=openFile.sheet_by_name("InformacionDTE-FEL")
workbook = xlsxwriter.Workbook('Nuevo.xls')
worksheet = workbook.add_worksheet()