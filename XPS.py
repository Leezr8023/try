import sys
import time
import array
from const import delay
sys.path.append(r'C:\Windows\Microsoft.NET\assembly\GAC_64\Newport.XPS.CommandInterface\v4.0_1.3.0.0__9a267756cf640dcf')
import clr
clr.AddReference("Newport.XPS.CommandInterface")
from CommandInterfaceXPS import *
import System
xps = XPS()
class MyXPS:
    def __init__(self):
        address = "192.168.254.254"
        port = 5001

        result = xps.OpenInstrument(address, port, 1000)
        if result == 0:
            print('Connection ', address, ":", port, " => Successful")
        else:
            print('Connection ', address, ":", port, " => failure ", result)
        result,errstring = xps.GroupInitialize('Group1','')
        if result == 0 :
            print('group initialize successful')
        else:
            print('group initialize fail')
        xps.GroupHomeSearch('Group1','')
        xps.GroupMotionEnable('Group1', '')
    def measureMove(self,move):
        move_double = array.array('d', [move])
        xps.GroupMoveAbsolute('Group1', move_double, 1, '')
        time.sleep(delay)
    def GetPosition(self):
        result,postion,errstring = xps.GroupPositionCurrentGet('Group1','',1,'')
        if result == 0:
            print(postion[0])
            return postion[0]
        else:
            print(errstring)
    def close(self):
        xps.CloseInstrument()