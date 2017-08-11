# -*- coding: utf-8 -*-
MYSQL_ROOT_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'root1234',
    'charset': 'utf8'
}

MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'demouser',
    'passwd': 'demo1234',
    'db': 'demo',
    'charset': 'utf8'
}

MYSQL_TABLE = {
    'ReservoirState': """CREATE TABLE IF NOT EXISTS ReservoirState (
                RS_ID INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                R_ID INT(10),
                Reservoir CHAR(8) NOT NULL,
                TimeStamp DATETIME NOT NULL,
                WaterLevel FLOAT(8,3) DEFAULT NULL,
                EffectiveWaterStorageCapacity FLOAT(8,3) DEFAULT NULL,
                PercentageUsedInReservoirCapacity FLOAT(8,3) DEFAULT NULL,
                MaximumCapacity FLOAT(8,3) DEFAULT NULL
                ) ENGINE=InnoDB""",
    'RegionalWaterRegime': """CREATE TABLE IF NOT EXISTS RegionalWaterRegime (
                RWR_ID INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                C_ID CHAR(8) NOT NULL,
                TimeStamp DATETIME NOT NULL,
                ReservoirLightsNow CHAR(1) DEFAULT NULL
                ) ENGINE=InnoDB"""
}