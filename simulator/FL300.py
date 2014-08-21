import re
from random import randint

class JulaboFL300:
    def __init__(self):
        self.TEMP = 0.0
        self.TEMP_SP = 0.0
        self.MODE = 0   #0 or 1 = Off, On
        self.VERSION = "JULABO FL300 Simulator, ISIS"
        self.STATUS = "Some kind of status message here"
        
    def check_command(self, comstr):       
        if comstr == "IN_PV_00":
            #Get actual value
            return str(self.TEMP + randint(-2,2)/10.0)
        elif comstr == "IN_SP_00":
            #Get setpoint value
            return str(self.TEMP_SP)
        elif comstr.startswith("OUT_SP_00 "):
            #Set setpoint
            m = re.match("OUT_SP_00 ([0-9]*\.?[0-9]+)", comstr)
            if not m is None:
                if len(m.groups()) > 0:
                    try:
                        self.TEMP_SP = float(m.groups()[0])
                        self.TEMP = self.TEMP_SP
                    except:
                        #The cast to float failed for some reason
                        pass
        elif comstr == "IN_MODE_05":
            #Get whether in circulate
            return str(self.MODE)
        elif comstr == "OUT_MODE_05 0":
            #Set mode to off
            self.MODE = 0
        elif comstr == "OUT_MODE_05 1":
            #Set mode to off
            self.MODE = 1
        elif comstr == "VERSION":
            #Get version
            return self.VERSION
        elif comstr == "STATUS":
            return self.STATUS
        
        return None