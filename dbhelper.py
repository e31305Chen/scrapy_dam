#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import csv
import MySQLdb
from config import *
from collections import OrderedDict

def help():
    print('  USAGE: valid command list as followed')
    print('  create_demodb_and_demouser ')
    print('  create_table ')
    print('  drop_table ')
    print('  setup')

def root_connect():
    try: 
        r_conn = MySQLdb.connect(host = MYSQL_ROOT_CONFIG['host'],
                                user = MYSQL_ROOT_CONFIG['user'],
                                passwd = MYSQL_ROOT_CONFIG['passwd'],
                                charset = MYSQL_ROOT_CONFIG['charset'])
    except:
        print("Can't Connect Database via root: ", sys.exc_info()[0])
        sys.exit()
    else:
        return r_conn

def create_demodb_and_demouser():
    r_conn = root_connect()
    r_cursor = r_conn.cursor()
    sql = 'CREATE USER IF NOT EXISTS \"' + MYSQL_CONFIG['user'] + '\"@\"' + MYSQL_CONFIG['host'] + '\" IDENTIFIED BY \"' + MYSQL_CONFIG['passwd'] + '\"'
    r_cursor.execute(sql)
    sql = 'CREATE DATABASE IF NOT EXISTS ' + MYSQL_CONFIG['db'] + ' CHARACTER SET ' + MYSQL_CONFIG['charset']
    r_cursor.execute(sql)
    sql = "GRANT ALL PRIVILEGES ON " + MYSQL_CONFIG['db'] + ".* to '" + MYSQL_CONFIG['user'] + "'@'" + MYSQL_CONFIG['host'] + "'"
    r_cursor.execute(sql)
    r_cursor.execute('FLUSH PRIVILEGES')
    r_cursor.close()
    r_conn.close()
    
def dbuser_connect():
    try:
        conn = MySQLdb.connect(host=MYSQL_CONFIG['host'],
                                user=MYSQL_CONFIG['user'],
                                passwd=MYSQL_CONFIG['passwd'],
                                db=MYSQL_CONFIG['db'],
                                charset=MYSQL_CONFIG['charset'])
    except:
        print("Can't Connect Database via " + MYSQL_CONFIG['user'], sys.exc_info()[0])
        sys.exit()
    else:
        return conn

def show_table():  #Don't know why is not working
    conn = dbuser_connect()
    cursor = conn.cursor()
    sql = "USE " + MYSQL_CONFIG['db'] + ";"
    print(sql)
    cursor.execute(sql)
    sql = "SHOW TABLES;"
    print(sql)
    cursor.execute(sql)
    cursor.close()
    conn.close()

def create_table(table):
    conn = dbuser_connect()
    cursor = conn.cursor()
    table_ex = MYSQL_TABLE[table]
    try:
        cursor.execute(table_ex)
    except:
        t = "WARNING: You might haven't created the FK table."
        print(t)
        cursor.close()
        conn.close()
        sys.exit()
    cursor.close()
    conn.close()
    t = "Table "+table+" has been created..."
    print(t)
    
def drop_all_tables():
    conn = dbuser_connect()
    cursor = conn.cursor()
    for i in reversed(range(len(MYSQL_TABLE_LIST))):
        table=MYSQL_TABLE_LIST[i]
        sql = "DROP TABLE " + table + ";"
        cursor.execute(sql)
        t = "Table "+table+" has been dropped..."
        print(t)
    cursor.close()
    conn.close()
    
    
def create_all_tables():
    conn = dbuser_connect()
    cursor = conn.cursor()
    for i in range(len(MYSQL_TABLE_LIST)):
        table=MYSQL_TABLE_LIST[i]
        table_ex = MYSQL_TABLE[table]
        try:
            cursor.execute(table_ex)
            print(table) 
        except:
            t = "WARNING: You might haven't created the FK table."
            print(t)
            cursor.close()
            conn.close()
            sys.exit()
    cursor.close()
    conn.close()
    t = "All tables have been created...Good!"
    print(t)

def drop_table(table):
    conn = dbuser_connect()
    cursor = conn.cursor()
    sql = "DROP TABLE " + table + ";"
    cursor.execute(sql)
    cursor.close()
    conn.close()
    t = "Table "+table+" has been dropped..."
    print(t)

def seidm():
    print("SEIDM ROCKS!!")

def setup():
    create_demodb_and_demouser()
    print("Setup Complete")

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in ["create_demodb_and_demouser",
                                            "setup",
                                            "show_table",
                                            "seidm",
                                            "drop_all_tables",
                                            "create_all_tables"]:
        f = globals()[sys.argv[1]]
        f()
    elif len(sys.argv) == 2 and sys.argv[1] in ["create_table", 
                                                "drop_table"]:
        print('Enter the table name.')
        for i in range(len(MYSQL_TABLE_LIST)):
            print(MYSQL_TABLE_LIST[i])

    elif len(sys.argv) == 3 and sys.argv[1] in ["create_table", 
                                                "drop_table"]:
        f = globals()[sys.argv[1]]
        f(sys.argv[2])
    else:
        help()
        sys.exit()