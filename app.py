import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)
import sqlite3
import json
import random

Product_List =["Apple","Käse","Brot", "Eier","Eis" ]


con=sqlite3.connect("Product.db")
cursor=con.cursor()

def table1():
    cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCT(Id INT ,Product TEXT,Preis FLOAT) ")
    con.commit()
    



def rand_funk():
    Preis=random.randrange(1,10)
    Id=random.randrange(100,1000)
   
    cursor.execute("INSERT INTO PRODUCT (Id,Preis) VALUES(?,?)",(Id,Preis))
    con.commit()
    con.close()
   

table1()

i=0
while (i<6):
    rand_funk()
    i+=1
con.close()

