#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import os
import sys

def change_working_path():
    path = os.path.abspath("dir.txt").replace("dir.txt","")+"dam"  #Stupie C9 again see pwd you'll know why
    print("Make sure the executed files are under this dir.\n=>",path,"\nIf not, please check the dir.txt is in the right dir!")
    os.chdir(path)

def help():
    print("\n======Run routinely=====")
    print("ReservoirState")
    print("RegionalWaterRegime")
    print("\n======Run once only=====")
    print("ReservoirPastState  \n   => Make sure you go to the \"ReservoirPastState.py\" under spider/ to check the beginning date and the other settings under dam/.")
    print("Reservoir")
    print("\n=====Run all of them to setup=====")
    print("setup")
    print("\n===Dev by CYLin===")
    
def damwra():
    change_working_path()
    os.system("./ReservoirState.py")
    
def ReservoirPastState():
    change_working_path()
    os.system("./ReservoirPastState.py")
    
def ReservoirState():
    change_working_path()
    os.system("./ReservoirState.py")
    
# def start_date():
#     bd = input("Please enter the start crawling date (Default to be \"2005-1-1\")." )
#     if(bd == ""):
#         bd = "2005-1-1"
#     return(bd)
    
# def ReservoirPastState_no_Scrapy(a,b):
#     change_working_path()
#     os.system("./ReservoirPastState.py")
#     print(a)
#     print(b)
    
def RegionalWaterRegime():
    change_working_path()
    os.system("./RegionalWaterRegime.py")
    
def Reservoir():
    change_working_path()
    os.system("./Reservoir.py")

def setup():
    ReservoirState()
    ReservoirPastState()
    RegionalWaterRegime()
    Reservoir()
    
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in ["ReservoirState",
                                            "ReservoirPastState",
                                            "RegionalWaterRegime",
                                            "Reservoir",
                                            "help",
                                            "setup"]:
        f = globals()[sys.argv[1]]
        f()
    # if len(sys.argv) == 4 and sys.argv[1] in ["ReservoirPastState_no_Scrapy"]:
    #     f = globals()[sys.argv[1]]
    #     f(sys.argv[2],sys.argv[3])
    
    else:
        help()
        sys.exit()