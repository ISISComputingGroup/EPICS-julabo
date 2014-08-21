#Note that the IOC needs to be running and that prefix needs to be altered to the appropriate system for the test being run
#These tests are for the Julabo FL300 IOC, and require the simulated DB files to be in place, they will not test communcation with an actual device
#Written by K Baker November 2013 for the ISIS facility
import unittest
import time
import os
from epics import PV

#These are the items to set at the moment - the rest will sort itself out - this should be moved in time into an XML format to allow for easier creation and use - or at least parts of it
#Get the MYPVPREFIX from the environment varioables if it exists, assume that his is the correct one to use, otherwise use a programmed default
try:
    PVPREFIX = os.environ['MYPVPREFIX']
except KeyError:
    PVPREFIX = 'NDW1032:kvlb23:'
    
#Assign a name to the IOC in use (this would echo the IOCNAME elements in the st.cmd for the IOC under test that are not in MYPVPREFIX
IOCNAME = 'JULFL300'

#Set a delay variable, hopefully this will allow for creating an unstable test environment at times
delay = 2

#Below is a list of the tests
TESTS = {}
TESTS[1] = ('Equal','VERSION','SIM:VERSION','','')
TESTS[2] = ('Equal','VERSION','SIM:VERSION','Malte','')
TESTS[3] = ('Equal','STATUS','SIM:STATUS','','')
TESTS[4] = ('Equal','STATUS','SIM:STATUS','Ophelia','')
TESTS[5] = ('Equal','SIM:STATUS','STATUS','Rufus','')
TESTS[6] = ('Equal','MODE','MODE:SP','','')
TESTS[7] = ('Expected Value','MODE:SP','MODE','0','0')
TESTS[8] = ('Expected Value','MODE:SP','MODE','1','1')
TESTS[9] = ('Value Error','MODE','','Ekua','')
TESTS[10] = ('Value Error','MODE:SP','','Leo','')
TESTS[11] = ('Equal','TEMP:SP','TEMP:SP:RBV','','')
TESTS[12] = ('Equal','TEMP','TEMP:SP','','')
TESTS[13] = ('Value Error','TEMP','','Masozi','')
TESTS[14] = ('Value Error','TEMP:SP','','Reino','')
TESTS[15] = ('Value Error','TEMP:SP:RBV','','Paulino','')
TESTS[16] = ('Expected Value','TEMP:SP','TEMP:SP:RBV','10','10.0')
TESTS[17] = ('Expected Value','TEMP:SP','TEMP','10','10.0')
TESTS[18] = ('Expected Value','TEMP:SP','TEMP:SP:RBV','0','0.0')
TESTS[19] = ('Expected Value','TEMP:SP','TEMP','0','0.0')
TESTS[20] = ('Expected Value','TEMP:SP','TEMP:SP:RBV','2.3','2.3')
TESTS[21] = ('Expected Value','TEMP:SP','TEMP','8.4','8.4')

#This is to simplify the use of storage for test reulsts
testdir = 'C:\EPICS\support\julabo\iocs\FL300\Test Logs'

#DO NOT CHANGE ANYTHING BELOW THIS UNLESS ALTERING TESTING METHODOLOGY - IF YOU ARE JUST WRITING A TEST CASE THE ABOVE IS ALL THAT SHOULD NEED CHANGING
#Set up the test log file
log_file = 'test_log.txt'
logf = open(log_file, 'w')
runner = unittest.TextTestRunner(logf, verbosity=1)

#Class for the simplification of PV creation
class pvrec:
    pvinst = ''
    val = ''
    
    def initpv(self, postfix):
        name = prefix + postfix
        pvrec.pvinst = PV(name)
       
#Build the whole prefix to use
prefix = PVPREFIX + IOCNAME + ':'

#Set up the testing suite
suite = unittest.TestSuite()
loader = unittest.TestLoader()

#Get into simulate mode and test for this
simname = prefix + 'SIM'
simpv = PV(simname)
sim = simpv.get()
intosim = False
if (sim != 1):
    print 'Putting into simulate mode'
    intosim = True
    simpv.put(1)
    #A sleep of 2 seconds follows every PV.put(), this is to ensure that the database has stabilised again before testing, otherwise there is a chance that a test is run before the record has scanned
    time.sleep(delay)
    sim = simpv.get()

class TestSimulate(unittest.TestCase):
    def test_sim(self):
        self.assertEqual(sim, 1, 'Not in Simulation Mode, unable to test IOC')
simsuite = unittest.TestLoader().loadTestsFromTestCase(TestSimulate)
suite.addTest(simsuite)

#Set up the PVs to use, and create the dictionary for later use
PVSTOUSE = {}

#Get the PV names used from the test cases entered
allpv_names = []
for x,TEST in TESTS.iteritems():
    allpv_names.append(TEST[1])
    if TEST[2] != '':
        allpv_names.append(TEST[2])
#Remove any duplicates   
RECNAMES = set(allpv_names)

#Populate the dictionary with the RECNAMES and the associated PVs
for pvx in RECNAMES:
    testing = pvrec()
    testing.initpv(pvx)
    PVSTOUSE[pvx] = testing.pvinst

#Generate and run the tests
for x,TEST in TESTS.iteritems():
    ttype = TEST[0]
    pv1 = PVSTOUSE[TEST[1]]
    pv2name = TEST[2]
    if pv2name != '':
        pv2 = PVSTOUSE[pv2name]
    setval = TEST[3]
    expval = TEST[4]
    logf.write(('Test %s: %s\n'%(x,TEST)))
    @unittest.skipIf(sim==0,'IOC not in Simulation Mode')
    class IterationTests(unittest.TestCase):
        if ttype =='Equal':
            def test_equal_pv(self):
                if setval != '':
                    pv1.put(setval)
                    time.sleep(delay)
                pv1val = pv1.get()
                pv2val = pv2.get()
                self.assertEqual(pv1val, pv2val, 'The PVs do not match')
        if ttype == 'Expected Value':
            def test_exp_value(self):
                if setval != '':
                    pv1.put(setval)
                    time.sleep(delay)
                pv2val = pv2.get()
                self.assertEqual(('%s'%pv2val), expval, ('%s returned %s which is not equal to %s'%(pv2,pv2val,expval)))
        if ttype == 'Value Error':
            def test_invalid_data(self):
                self.assertRaises(ValueError, pv1.put, setval)
    itersuite = unittest.TestLoader().loadTestsFromTestCase(IterationTests)
    runner.run(itersuite)

logf.close()

#Edit the log file and store in a seperate file - this may require some alterations
log_time = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
edited_log_name = ('%s %s Test Log.txt' % (log_time,IOCNAME))
edited_log = os.path.join(testdir,edited_log_name)
loged = open(edited_log, 'w')
all_res = []
res = []
with open(log_file, 'r') as f:
    for line in f:
        all_res.append(line)

for x in all_res:
    line_start = x[:2]
    #The line starts are limited to those I have noticed so far, more may be required, so keep an eye on the log file as well as the edited file during development
    if line_start in ['Te','OK','As','Ty']:
        res.append(x)

loged.writelines(res)
loged.close()

#If the IOC was put into simulation mode, put it back into device mode
if (intosim):
    print 'Returning to device mode'
    simpv.put(0)