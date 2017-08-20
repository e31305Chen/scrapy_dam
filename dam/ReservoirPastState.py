#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors
import sys
import os
import time
import json
#path = os.path.abspath("dbhelper.py").replace("dbhelper.py","")
#sys.path.append(path)

# C9 has some problem with dbhelper.py path so later you can use codes above!
sys.path.append("/home/ubuntu/workspace/scrapy_dam/")
from dbhelper import dbuser_connect

#===========================================================================================================
#Setting
doublecheck = False  #It might take a great time and space the crawl the data. If not need it set to False!
keepfile = True  #See if you want to keep the original json file if yes we will rename it and keep it.
nameoffile = "Saving_data.json" #The name of the renamed file.
path = os.path.abspath("dir.txt").replace("dir.txt","") # To find the path.
openfilename = "ReservoirPastState_items1.json"
#===========================================================================================================
Run_scrapy = input("Do you want to run the scrapy?(or you already have the input file)[y/n]  ")  #No double check for "y"
if(Run_scrapy == "n"):
    openfilename = input("!!!!Make sure your input file is at the same dir as dir.txt!!!!\n("+path+")\nEnter your file name.( Default: ReservoirPastState_items1.json ):  ")
    doublecheck = False

def run_scrapy(dc):
    if(dc):
        delet()
        os.system("scrapy crawl ReservoirPastState")
        print("Please wait.....")
        for i in range(1,6,1):
            time.sleep(1)
            print(i)
        os.system("scrapy crawl ReservoirPastState")
    else:
        delet()
        os.system("scrapy crawl ReservoirPastState")

def delet():
    if(os.path.isfile('ReservoirPastState_items1.json')):
        os.remove('ReservoirPastState_items1.json')
        
    if(os.path.isfile('ReservoirPastState_items2.json')):
        os.remove('ReservoirPastState_items2.json')
        
    if(os.path.isfile('check_item1.txt')):
        os.remove('check_item1.txt')
        
    if(os.path.isfile('check_item1.txt')):
        os.remove('check_item2.txt')
    
#Compare two json file
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

def convert2list(string):
    try:
        s = open(string,"r")
    except:
        print("Cannot find and open the file under this directory:\n",string)
        sys.exit()
    s_list = s.read().splitlines()
    l = len(s_list)
    object_list = []
    for i in range(0,l,1):
        object_list.append(json.loads(s_list[i]))
    return(object_list)
    
#Link to DB by dbhelper.py
conn = dbuser_connect()
cursor = conn.cursor() 

#run crawl and compare the file then insert into DB
if(Run_scrapy == "y"):
    run_scrapy(doublecheck)

for t in range(1,5,1):
    dict_item1 = convert2list(path + openfilename)
    if(doublecheck):
        dict_item2 = convert2list(path+"ReservoirPastState_items2.json")
    
    if(doublecheck):
        if(ordered(dict_item1) == ordered(dict_item2)):
            l = len(dict_item1)
            for i in range(0,l,1):
                myDict = dict_item1[i]
                # Insert object to mysql 
                a =  list(myDict.values())
                values = '\"' + '\",\"'.join(map(str, a)) + '\"'
                column_name = ', '.join(myDict.keys())
                sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("ReservoirState", column_name, values)
                print(i+1,". ",values)
                print(sql)
                cursor.execute(sql)
                conn.commit()
            if(keepfile):
                os.rename(path+"ReservoirPastState_items1.json", path+nameoffile)
                print("The original json file is saving at: \n =>",path+nameoffile)
            delet()
            print("Comparison pass and file has been insert into DB table ReservoirState!")
            break
        else:
            print("comparison is fail. Try ",t," times")
            time.sleep(5)
            run_scrapy(doublecheck)
    else:
        l = len(dict_item1)
        for i in range(0,l,1):
            myDict = dict_item1[i]
            # Insert object to mysql 
            a =  list(myDict.values())
            values = '\"' + '\",\"'.join(map(str, a)) + '\"'
            column_name = ', '.join(myDict.keys())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("ReservoirState", column_name, values)
            print(i+1,". ",values)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        if(keepfile):
            a = path + openfilename
            b = path + "Saving_data/"+time.strftime("%Y%m%d")+"_"+nameoffile
            os.rename(a, b)
            print("The original json file is saving at: \n =>",b)
        delet()
        print("Comparison pass and file has been insert into DB table ReservoirState!")
        break
    
# Close DB link
cursor.close()
conn.close()





