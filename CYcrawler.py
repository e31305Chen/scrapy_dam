#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import os
import sys

def change_working_path():
    path = os.path.abspath("dir.txt").replace("dir.txt","")+"dam"  #Stupie C9 again see pwd you'll know why
    print("Make sure the executed files are under this dir.\n=>",path,"\nIf not, please check the dir.txt is in the right dir!")
    os.chdir(path)

def help():
    print("======Run routinely=====")
    print("ReservoirState")
    print("RegionalWaterRegime")
    print("======Run once only=====")
    print("ReservoirPastState  \n=> Make sure you go to the \"ReservoirPastState.py\" under spider/ to check the begining date and the other settings under dam/.")
    print("Reservoir")
    print("=====Run all of them to setup=====")
    print("setup")
    print("===Dev by CYLin===")
    
def ReservoirState():
    change_working_path()
    os.system("./ReservoirState.py")
    
def ReservoirPastState():
    change_working_path()
    os.system("./ReservoirPastState.py")
    
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
    
    else:
        help()
        sys.exit()