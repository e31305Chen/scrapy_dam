#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import os
import sys
#path = os.path.abspath("ReservoirState.py").replace("ReservoirState.py","")
#os.system("."+path)
#path = os.path.abspath("dbhelper.py").replace("dbhelper.py","")
#sys.path.append(path)
#os.system("./dam/ReservoirState.py") 可動但抓不到scrapy

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
    os.system("./ReservoirState.py")
    
def ReservoirPastState():
    os.system("./ReservoirPastState.py")
    
def RegionalWaterRegime():
    os.system("./RegionalWaterRegime.py")
    
def Reservoir():
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