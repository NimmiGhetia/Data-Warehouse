import pyodbc
import platform 

platform.architecture()
#conn=pyodbc.connect(r'Driver={Microsoft Access Driver(*.accdb)};DBQ=/home/FDUSER/Data-Warehouse/lab7/Books2010.accdb;')
#cursor=conn.cursor()
#cursor.execute('Select * from books')
#for row in cursor.fetchall():
#    print(row)