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

MYSQL_TABLE_LIST=['Location','City','Reservoir','WaterSupply',
                    'FlowObservatory','Forecast','IrrigationArea',
                    'ReservoirState','RegionalWaterRegime','Q90','Q95',
                    'NextReservoirLights','NextWeekP','RuleCurve','SimReservoirFlow',
                    'WaterIntakeStructures','ForecastingTime','Light','PreWaterLevel',
                    'PreWaterStorageCapacity','PeoplesLivelihoodWater','IrrigationWaterDemand']


MYSQL_TABLE = {
    'Location':"""CREATE TABLE IF NOT EXISTS Location (
               L_ID                 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
               LocationName         varchar(3) NOT NULL
               )ENGINE=InnoDB""",

    'City':"""CREATE TABLE IF NOT EXISTS City(
                C_ID                 int not null auto_increment,
                CityName             varchar(10) NOT NULL,
                L_ID                 int,
                primary key (C_ID),
                FOREIGN KEY (L_ID) REFERENCES Location (L_ID)
                )ENGINE=InnoDB""",
    
    'Reservoir':"""CREATE TABLE IF NOT EXISTS Reservoir (
                R_ID                 int not null auto_increment,
                ReservoirIdentifier  varchar(8) not null,
                ReservoirName         varchar(10),
                primary key (R_ID)
                )ENGINE=InnoDB""",
    
    'WaterSupply':"""CREATE TABLE IF NOT EXISTS WaterSupply (
                WS_ID                int not null auto_increment,
                R_ID                 int,
                C_ID                 int,
                primary key (WS_ID),
                foreign key (C_ID) references City (C_ID),
                foreign key (R_ID) references Reservoir (R_ID)
                )ENGINE=InnoDB""",
        
    'FlowObservatory':"""CREATE TABLE IF NOT EXISTS FlowObservatory(
                FO_ID                int not null auto_increment,
                C_ID                 int,
                BasinIdentifier      varchar(10),
                ObservatoryName      varchar(10),
                primary key (FO_ID),
                FOREIGN KEY (C_ID) REFERENCES City (C_ID)
                )ENGINE=InnoDB""",

    'Forecast':"""CREATE TABLE IF NOT EXISTS Forecast(
                F_ID                 int not null auto_increment,
                L_ID                 int,
                TimeStamp            datetime,
                ElementValue         varchar(10),
                ForecastP            float,
                ForecastT            float,
                primary key (F_ID),
                FOREIGN KEY (L_ID) REFERENCES Location (L_ID)
                )ENGINE=InnoDB""",

    'IrrigationArea':"""CREATE TABLE IF NOT EXISTS IrrigationArea (
                IRR_ID               int not null auto_increment,
                IrrigationName       varchar(10),
                IrrigationArea       float,
                Fallow               int,
                primary key (IRR_ID)
                )ENGINE=InnoDB""",
   
    'ReservoirState': """CREATE TABLE IF NOT EXISTS ReservoirState (
                RS_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                R_ID INT,
                TimeStamp DATETIME NOT NULL,
                WaterLevel FLOAT(8,3) DEFAULT NULL,
                EffectiveWaterStorageCapacity FLOAT(8,3) DEFAULT NULL,
                PercentageUsedInReservoirCapacity FLOAT(8,3) DEFAULT NULL,
                MaximumCapacity FLOAT(8,3) DEFAULT NULL,
                FOREIGN KEY (R_ID) REFERENCES Reservoir (R_ID)
                ) ENGINE=InnoDB""",
    'RegionalWaterRegime': """CREATE TABLE IF NOT EXISTS RegionalWaterRegime (
                RWR_ID INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                C_ID int,
                TimeStamp DATETIME NOT NULL,
                ReservoirLightsNow CHAR(1) DEFAULT NULL,
                FOREIGN KEY (C_ID) REFERENCES City (C_ID)
                ) ENGINE=InnoDB""",
    
    'Q90':"""CREATE TABLE IF NOT EXISTS Q90 (
                Q90_ID               int not null auto_increment,
                FO_ID                int,
                Ten_1                float,
                Ten_2                float,
                Ten_3                float,
                Ten_4                float,
                Ten_5                float,
                Ten_6                float,
                Ten_7                float,
                Ten_8                float,
                Ten_9                float,
                Ten_10               float,
                Ten_11               float,
                Ten_12               float,
                Ten_13               float,
                Ten_14               float,
                Ten_15               float,
                Ten_16               float,
                Ten_17               float,
                Ten_18               float,
                Ten_19               float,
                Ten_20               float,
                Ten_21               float,
                Ten_22               float,
                Ten_23               float,
                Ten_24               float,
                Ten_25               float,
                Ten_26               float,
                Ten_27               float,
                Ten_28               float,
                Ten_29               float,
                Ten_30               float,
                Ten_31               float,
                Ten_32               float,
                Ten_33               float,
                Ten_34               float,
                Ten_35               float,
                Ten_36               float,
                primary key (Q90_ID),
                FOREIGN KEY (FO_ID) REFERENCES FlowObservatory (FO_ID)
                )ENGINE=InnoDB""",
    
    'Q95':"""CREATE TABLE IF NOT EXISTS Q95 (
                Q95_ID               int not null auto_increment,
                FO_ID                int,
                Ten_1                float,
                Ten_2                float,
                Ten_3                float,
                Ten_4                float,
                Ten_5                float,
                Ten_6                float,
                Ten_7                float,
                Ten_8                float,
                Ten_9                float,
                Ten_10               float,
                Ten_11               float,
                Ten_12               float,
                Ten_13               float,
                Ten_14               float,
                Ten_15               float,
                Ten_16               float,
                Ten_17               float,
                Ten_18               float,
                Ten_19               float,
                Ten_20               float,
                Ten_21               float,
                Ten_22               float,
                Ten_23               float,
                Ten_24               float,
                Ten_25               float,
                Ten_26               float,
                Ten_27               float,
                Ten_28               float,
                Ten_29               float,
                Ten_30               float,
                Ten_31               float,
                Ten_32               float,
                Ten_33               float,
                Ten_34               float,
                Ten_35               float,
                Ten_36               float,
                primary key (Q95_ID),
                FOREIGN KEY (FO_ID) REFERENCES FlowObservatory (FO_ID)
                )ENGINE=InnoDB""",    
    
    'NextReservoirLights':"""CREATE TABLE IF NOT EXISTS NextReservoirLights (
                NRL_ID               int not null auto_increment,
                C_ID                 int,
                NextReservoirLights  varchar(10),
                ReleaseTime          datetime,
                primary key (NRL_ID),
                FOREIGN KEY (C_ID) REFERENCES City (C_ID)
                )ENGINE=InnoDB""",

    'NextWeekP':"""CREATE TABLE IF NOT EXISTS NextWeekP (
                NWP_ID               int not null auto_increment,
                C_ID                 int,
                NextWeekP            int,
                primary key (NWP_ID),
                FOREIGN KEY (C_ID) REFERENCES City (C_ID)
                )ENGINE=InnoDB""",

    'RuleCurve':"""CREATE TABLE IF NOT EXISTS RuleCurve (
                RC_ID                int not null auto_increment,
                R_ID                 int,
                TenDays_No           float,
                UpperLimit           float,
                MidLimit             float,
                LowerLimit           float,
                SeriousLowerLimit    float,
                primary key (RC_ID),
                FOREIGN KEY (R_ID) REFERENCES Reservoir (R_ID)
                )ENGINE=InnoDB""",

    'SimReservoirFlow':"""CREATE TABLE IF NOT EXISTS SimReservoirFlow (
                SRF_ID               int not null auto_increment,
                R_ID                 int,
                TimeStamp            datetime,
                StreamFlow           float,
                PlanWaterDemand      float,
                IrrigationRequirement float,
                WaterRight           float,
                primary key (SRF_ID),
                foreign key (R_ID) references Reservoir (R_ID)
                )ENGINE=InnoDB""",

    'WaterIntakeStructures':"""CREATE TABLE IF NOT EXISTS WaterIntakeStructures (
                WIS_ID               int not null auto_increment,
                StructuresName       varchar(10),
                Q_downstream         float,
                MaxQ                 float,
                primary key (WIS_ID)
                )ENGINE=InnoDB""",

    'ForecastingTime':"""CREATE TABLE IF NOT EXISTS ForecastingTime (
                FT_ID                int not null auto_increment,
                ForecastingTime         datetime,
                primary key (FT_ID)
                )ENGINE=InnoDB""",

    'Light':"""CREATE TABLE IF NOT EXISTS Light(
                Light_ID             int not null auto_increment,
                C_ID                 int,
                FT_ID                int,
                Light_1              varchar(10),
                Light_2              varchar(10),
                Light_3              varchar(10),
                Light_4              varchar(10),
                Light_5              varchar(10),
                Light_6              varchar(10),
                Light_7              varchar(10),
                Light_8              varchar(10),
                Light_9              varchar(10),
                Light_10             varchar(10),
                Light_11             varchar(10),
                Light_12             varchar(10),
                primary key (Light_ID),
                FOREIGN KEY (C_ID) REFERENCES City (C_ID),
                FOREIGN KEY (FT_ID) REFERENCES ForecastingTime (FT_ID)
                )ENGINE=InnoDB""",
    
    'PreWaterLevel':"""CREATE TABLE IF NOT EXISTS PreWaterLevel (
                PWL_ID               int not null auto_increment,
                R_ID                 int,
                FT_ID            int,
                PredictionWaterLevel_1 float,
                PredictionWaterLevel_2 float,
                PredictionWaterLevel_3 float,
                PredictionWaterLevel_4 float,
                PredictionWaterLevel_5 float,
                PredictionWaterLevel_6 float,
                PredictionWaterLevel_7 float,
                PredictionWaterLevel_8 float,
                PredictionWaterLevel_9 float,
                PredictionWaterLevel_10 float,
                PredictionWaterLevel_11 float,
                PredictionWaterLevel_12 float,
                primary key (PWL_ID),
                foreign key (R_ID) references Reservoir (R_ID),
                FOREIGN KEY (FT_ID) REFERENCES ForecastingTime (FT_ID)
                )ENGINE=InnoDB""",

    'PreWaterStorageCapacity':"""CREATE TABLE IF NOT EXISTS PreWaterStorageCapacity (   
                PWSC_ID               int not null auto_increment,
                R_ID                 int,
                FT_ID            int,
                PredictionWaterStorageCapacity_1 float,
                PredictionWaterStorageCapacity_2 float,
                PredictionWaterStorageCapacity_3 float,
                PredictionWaterStorageCapacity_4 float,
                PredictionWaterStorageCapacity_5 float,
                PredictionWaterStorageCapacity_6 float,
                PredictionWaterStorageCapacity_7 float,
                PredictionWaterStorageCapacity_8 float,
                PredictionWaterStorageCapacity_9 float,
                PredictionWaterStorageCapacity_10 float,
                PredictionWaterStorageCapacity_11 float,
                PredictionWaterStorageCapacity_12 float,
                primary key (PWSC_ID),
                foreign key (R_ID) references Reservoir (R_ID),
                FOREIGN KEY (FT_ID) REFERENCES ForecastingTime (FT_ID)
                )ENGINE=InnoDB""",
                
    'PeoplesLivelihoodWater':"""CREATE TABLE IF NOT EXISTS PeoplesLivelihoodWater (
                    PLW_ID               int not null auto_increment,
                    R_ID                 int,
                    PeoplesLivelihoodWater_1 float,
                    PeoplesLivelihoodWater_2 float,
                    PeoplesLivelihoodWater_3 float,
                    PeoplesLivelihoodWater_4 float,
                    PeoplesLivelihoodWater_5 float,
                    PeoplesLivelihoodWater_6 float,
                    PeoplesLivelihoodWater_7 float,
                    PeoplesLivelihoodWater_8 float,
                    PeoplesLivelihoodWater_9 float,
                    PeoplesLivelihoodWater_10 float,
                    PeoplesLivelihoodWater_11 float,
                    PeoplesLivelihoodWater_12 float,
                    PeoplesLivelihoodWater_13 float,
                    PeoplesLivelihoodWater_14 float,
                    PeoplesLivelihoodWater_15 float,
                    PeoplesLivelihoodWater_16 float,
                    PeoplesLivelihoodWater_17 float,
                    PeoplesLivelihoodWater_18 float,
                    PeoplesLivelihoodWater_19 float,
                    PeoplesLivelihoodWater_20 float,
                    PeoplesLivelihoodWater_21 float,
                    PeoplesLivelihoodWater_22 float,
                    PeoplesLivelihoodWater_23 float,
                    PeoplesLivelihoodWater_24 float,
                    PeoplesLivelihoodWater_25 float,
                    PeoplesLivelihoodWater_26 float,
                    PeoplesLivelihoodWater_27 float,
                    PeoplesLivelihoodWater_28 float,
                    PeoplesLivelihoodWater_29 float,
                    PeoplesLivelihoodWater_30 float,
                    PeoplesLivelihoodWater_31 float,
                    PeoplesLivelihoodWater_32 float,
                    PeoplesLivelihoodWater_33 float,
                    PeoplesLivelihoodWater_34 float,
                    PeoplesLivelihoodWater_35 float,
                    PeoplesLivelihoodWater_36 float,
                    primary key (PLW_ID),
                    FOREIGN KEY (R_ID) references Reservoir (R_ID)
                    )ENGINE=InnoDB""",
    
    'IrrigationWaterDemand':"""CREATE TABLE IF NOT EXISTS IrrigationWaterDemand(
                    IWD_ID               int not null auto_increment,
                    R_ID                 int,
                    IrrigationWaterDemand_1 float,
                    IrrigationWaterDemand_2 float,
                    IrrigationWaterDemand_3 float,
                    IrrigationWaterDemand_4 float,
                    IrrigationWaterDemand_5 float,
                    IrrigationWaterDemand_6 float,
                    IrrigationWaterDemand_7 float,
                    IrrigationWaterDemand_8 float,
                    IrrigationWaterDemand_9 float,
                    IrrigationWaterDemand_10 float,
                    IrrigationWaterDemand_11 float,
                    IrrigationWaterDemand_12 float,
                    IrrigationWaterDemand_13 float,
                    IrrigationWaterDemand_14 float,
                    IrrigationWaterDemand_15 float,
                    IrrigationWaterDemand_16 float,
                    IrrigationWaterDemand_17 float,
                    IrrigationWaterDemand_18 float,
                    IrrigationWaterDemand_19 float,
                    IrrigationWaterDemand_20 float,
                    IrrigationWaterDemand_21 float,
                    IrrigationWaterDemand_22 float,
                    IrrigationWaterDemand_23 float,
                    IrrigationWaterDemand_24 float,
                    IrrigationWaterDemand_25 float,
                    IrrigationWaterDemand_26 float,
                    IrrigationWaterDemand_27 float,
                    IrrigationWaterDemand_28 float,
                    IrrigationWaterDemand_29 float,
                    IrrigationWaterDemand_30 float,
                    IrrigationWaterDemand_31 float,
                    IrrigationWaterDemand_32 float,
                    IrrigationWaterDemand_33 float,
                    IrrigationWaterDemand_34 float,
                    IrrigationWaterDemand_35 float,
                    IrrigationWaterDemand_36 float,
                    primary key (IWD_ID),
                    FOREIGN KEY (R_ID) references Reservoir (R_ID)
                    )ENGINE=InnoDB"""
}