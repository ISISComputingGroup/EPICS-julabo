import re

class JulaboFP50_MH:
    def __init__(self):
        self.TEMP = 0.0
        self.TEMP_SP = 0.0
        self.EXT_TEMP = 0.0
        self.MODE = 0   #0 or 1 = Off, On
        self.VERSION = "JULABO FP50_MH Simulator, ISIS"
        self.STATUS = "What should this return?"
        self.POWER = 45
        self.HIGH_LIMIT = 100
        self.LOW_LIMIT = -20
        
    def check_command(self, comstr):       
        if comstr == "IN_PV_00":
            #Get actual value
            return str(self.TEMP)
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
                        #Set the "actual value" to the sp plus a little
                        self.TEMP = self.TEMP_SP + 0.1
                        #Set the external temp to the sp minus a bit
                        self.EXT_TEMP = self.TEMP_SP - 0.5
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
        elif comstr == "IN_PV_02":
            return str(self.POWER)
        elif comstr == "IN_PV_01":
            return str(self.EXT_TEMP)
        elif comstr == "IN_SP_01":
            return str(self.HIGH_LIMIT)
        elif comstr == "IN_SP_02":
            return str(self.LOW_LIMIT)
        
        return None