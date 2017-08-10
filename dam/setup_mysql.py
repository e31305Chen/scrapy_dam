#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb
import MySQLdb.cursors

try:
    r_conn = MySQLdb.connect(host='localhost',
                            user='root',
                            passwd='root1234',
                            charset='utf8')
except:
    print("Can't Connect Database via root: ", sys.exc_info()[0])
    sys.exit()

# drop db and user if exist
r_cursor = r_conn.cursor()

# create user and db, and grant privileges
r_cursor.execute("CREATE USER IF NOT EXISTS 'demouser'@'localhost' IDENTIFIED BY 'demo1234'")
r_cursor.execute("CREATE DATABASE IF NOT EXISTS demo CHARACTER SET UTF8")
r_cursor.execute("GRANT ALL PRIVILEGES ON demo.* to 'demouser'@'localhost'")
r_cursor.execute("FLUSH PRIVILEGES")
r_cursor.close()
r_conn.close()

# connect demo db
try:
    conn = MySQLdb.connect(host='localhost',
                            user='demouser',
                            passwd='demo1234',
                            db='demo',
                            charset='utf8')
except:
    print("Can't Connect Database via demouser: ", sys.exc_info()[0])
    sys.exit()

# create schema
cursor = conn.cursor()
# cursor.execute("DROP TABLE if EXISTS a136")
# cursor.execute("USE demo")
cursor.execute("""CREATE TABLE IF NOT EXISTS ReservoirState (
                RS_ID INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                R_ID INT(10),
                Reservoir CHAR(8) NOT NULL,
                TimeStamp CHAR(25) NOT NULL,
                WaterLevel FLOAT(6,2) DEFAULT NULL,
                EffectiveWaterStorageCapacity FLOAT(6,2) DEFAULT NULL,
                PercentageUsedInReservoirCapacity FLOAT(3,2) DEFAULT NULL,
                MaximumCapacity FLOAT(6,2) DEFAULT NULL
                ) ENGINE=InnoDB""")
cursor.close()
conn.close()

