#Note that the IOC needs to be running and that prefix needs to be altered to the appropriate system for the test being run
#These tests are for the Julabo FP50 MH IOC, and require the simulated DB files to be in place, they will not test communcation with an actual device
#Written by K Baker October 2013 for the ISIS facility
import unittest
import time
from epics import PV

#Set up a prefix - this will need to be altered as appropriate, and under automation should be the MYPVPREFIX value in ISIS, plus the IOC name
prefix = 'NDW1032:kvlb23:JULFP50MH:'

#Set up the PVs to use
#This has been done with each one seperatly for understandability at present, and to record which records had simulated pairings
name = prefix + 'SIM'
simpv = PV(name)
name = prefix + 'VERSION'
verpv = PV(name)
name = prefix + 'SIM:VERSION'
simverpv = PV(name)
name = prefix + 'STATUS'
statpv = PV(name)
name = prefix + 'SIM:STATUS'
simstatpv = PV(name)
name = prefix + 'POWER'
powpv = PV(name)
name = prefix + 'SIM:POWER'
simpowpv = PV(name)
name = prefix + 'HIGHLIMIT'
hilimpv = PV(name)
name = prefix + 'SIM:HIGHLIMIT'
simhilimpv = PV(name)
name = prefix + 'LOWLIMIT'
lolimpv = PV(name)
name = prefix + 'SIM:LOWLIMIT'
simlolimpv = PV(name)
name = prefix + 'MODE'
modepv = PV(name)
name = prefix + 'MODE:SP'
modesppv = PV(name)
name = prefix + 'TEMP'
temppv = PV(name)
name = prefix + 'TEMP:SP'
tempsppv = PV(name)
name = prefix + 'TEMP:SP:RBV'
tempsprbvpv = PV(name)
name = prefix + 'EXTTEMP'
exttemppv = PV(name)

#Set a delay variable, hopefully this will allow for creating an unstable test environment at times
delay = 2

#Get into simulate mode if appropriate
sim = simpv.get()
intosim = False
if (sim != 1):
    print 'Putting into simulate mode'
    intosim = True
    simpv.put(1)
	#A sleep of 2 seconds follows every PV.put(), this is to ensure that the database has stabilised again before testing, otherwise there is a chance that a test is run before the record has scanned
    time.sleep(delay)
    sim = simpv.get()

#Test for Simulation mode
class TestSimulate(unittest.TestCase):
    def test_sim(self):
        self.assertEqual(sim, 1, 'Not in Simulation Mode, unable to test IOC')
simsuite = unittest.TestLoader().loadTestsFromTestCase(TestSimulate)

#Test the Version
version = verpv.get()
simversion = simverpv.get()
#If the system isn't in simulation mode skip these test cases, repeated for each set of cases
@unittest.skipIf(sim==0,'IOC not in Simulation Mode')
class TestVersion(unittest.TestCase):
    def test_version_default(self):
		#Compare the record with the data held in the appropriate simulated record
        self.assertEqual(version, simversion, 'The version is not the Simulated Version')
    def test_version_unaltered(self):
		#Attempt to rewrite the record value, this should revert to the simulated value
        verpv.put('Miley')
        time.sleep(delay)
        version = verpv.get()
        self.assertEqual(version, simversion, 'The version is not the Simulated Version')
versuite = unittest.TestLoader().loadTestsFromTestCase(TestVersion)

#Test the Status
status = statpv.get()
simstatus = simstatpv.get()
@unittest.skipIf(sim==0,'IOC not in Simulation Mode')
class TestStatus(unittest.TestCase):
    def test_status_default(self):
		#Compare the record with the data held in the appropriate simulated record
        self.assertEqual(status, simstatus, 'The status is not the Simulated Status')
    def test_status_unaltered(self):
		#Attempt to rewrite the record value, this should revert to the simulated value
        statpv.put('Bethuel')
        time.sleep(delay)
        status = statpv.get()
        self.assertEqual(status, simstatus, 'The status is not the Simulated Status')
    def test_status_sim_altered(self):
		#Attempt to rewrite the simulated value, this should update the record value
        simstatpv.put('Still Simulated')
        time.sleep(delay)
        status = statpv.get()
        self.assertEqual(status, simstatus, 'The status is not the Simulated Status')
statsuite = unittest.TestLoader().loadTestsFromTestCase(TestStatus)

#Test the Power
power = powpv.get()
simpower = simpowpv.get()
@unittest.skipIf(sim==0,'IOC not in Simulation Mode')
class TestPower(unittest.TestCase):
    def test_power_default(self):
		#Compare the record with the data held in the appropriate simulated record
        self.assertEqual(power, simpower, 'The power is not the Simulated Power')
    def test_power_invalid_data_type(self):
		#Verify that writing an invalid data type will raise a ValueError
        self.assertRaises(ValueError, powpv.put, 'Simon')
    def test_power_sim_altered(self):
		#Attempt to rewrite the simulated value, this should update the record value
        simpowpv.put('25')
        time.sleep(delay)
        power = powpv.get()
        self.assertEqual(power, simpower, 'The power is not the Simulated Power')
powersuite = unittest.TestLoader().loadTestsFromTestCase(TestPower)

#Test the high limit
hilimit = hilimpv.get()
simhilimit = simhilimpv.get()
@unittest.skipIf(sim==0,'IOC not in Simulation Mode')
class Testhilimit(unittest.TestCase):
    def test_hilimit_default(self):
		#Compare the record with the data held in the appropriate simulated record
        self.assertEqual(hilimit, simhilimit, 'The high limit is not the Simulated High Limit')
    def test_hilimit_invalid_data_type(self):
		#Verify that writing an invalid data type will raise a ValueError
        self.assertRaises(ValueError, hilimpv.put, 'Marcelyn')
    def test_hilimit_sim_altered(self):
		#Attempt to rewrite the simulated value, this should update the record value
        simhilimpv.put('2000')
        time.sleep(delay)
        hilimit = hilimpv.get()
        self.assertEqual(hilimit, simhilimit, 'The high limit is not the Simulated High Limit')
hilimitsuite = unittest.TestLoader().loadTestsFromTestCase(Testhilimit)

#Test the low limit
lolimit = lolimpv.get()
simlolimit = simlolimpv.get()
@unittest.skipIf(sim==0,'IOC not in Simulation Mode')
class Testlolimit(unittest.TestCase):
    def test_lolimit_default(self):
		#Compare the record with the data held in the appropriate simulated record
        self.assertEqual(lolimit, simlolimit, 'The low limit is not the Simulated Low Limit')
    def test_lolimit_invalid_data_type(self):
		#Verify that writing an invalid data type will raise a ValueError
        self.assertRaises(ValueError, lolimpv.put, 'Manon')
    def test_lolimit_sim_altered(self):
		#Attempt to rewrite the simulated value, this should update the record value
        simlolimpv.put('10')
        time.sleep(delay)
        lolimit = lolimpv.get()
        self.assertEqual(lolimit, simlolimit, 'The low limit is not the Simulated Low Limit')
lolimitsuite = unittest.TestLoader().loadTestsFromTestCase(Testlolimit)

#Test the Mode
mode = modepv.get()
modesp = modesppv.get()
@unittest.skipIf(sim==0,'IOC not in Simulation Mode')
class TestMode(unittest.TestCase):
    def test_mode_default(self):
		#Verify that the readbacks relate to the present setpoints
        self.assertEqual(mode, modesp, 'The mode is not the same as the mode setpoint')
    def test_mode_on(self):
		#Verify that the readbacks relate to a known setpoint
        modesppv.put(1)
        time.sleep(delay)
        mode = modepv.get()
        modesp = modesppv.get()
        self.assertEqual(mode, 1, 'The mode is not On')
        self.assertEqual(modesp, 1, 'The mode setpoint is not On')
    def test_mode_off(self):
		#Verify that the readbacks relate to a known setpoint
        modesppv.put(0)
        time.sleep(delay)
        mode = modepv.get()
        modesp = modesppv.get()
        self.assertEqual(mode, 0, 'The mode is not Off')
        self.assertEqual(modesp, 0, 'The mode setpoint is not Off')
    def test_mode_invalid_data(self):
		#Verify that writing an invalid data type will raise a ValueError
        self.assertRaises(ValueError, modesppv.put, 'Mitrodora')
        self.assertRaises(ValueError, modepv.put, 'Lina')
modesuite = unittest.TestLoader().loadTestsFromTestCase(TestMode)

#Test the Temps
temp = temppv.get()
tempsp = tempsppv.get()
tempsprbv = tempsprbvpv.get()
exttemp = exttemppv.get()
@unittest.skipIf(sim==0,'IOC not in Simulation Mode')
class TestTemp(unittest.TestCase):
    def test_temp_default(self):
		#Verify that the readbacks relate to the present setpoints
        self.assertEqual(tempsprbv, tempsp, 'The readback value for the temperature setpoint is not the same as the temperature setpoint')
        self.assertEqual(temp, tempsp+0.2, 'The temperature value is not the value expected')
        self.assertEqual(exttemp, tempsp+25.2, 'The external temperature value is not the value expected')
    def test_mode_invalid_data(self):
		#Verify that writing an invalid data type will raise a ValueError
        self.assertRaises(ValueError, tempsppv.put, 'Aletha')
        self.assertRaises(ValueError, tempsppv.put, 'Isidora')
        self.assertRaises(ValueError, tempsppv.put, 'Dinko')
        self.assertRaises(ValueError, tempsppv.put, 'Heimirich')
    def test_temp_zero(self):
		#Verify that the readbacks relate to a known setpoint
        tempsppv.put(0)
        time.sleep(delay)
        temp = temppv.get()
        tempsp = tempsppv.get()
        tempsprbv = tempsprbvpv.get()
        exttemp = exttemppv.get()
        self.assertEqual(tempsp, 0, 'The temperature setpoint is not the value expected')
        self.assertEqual(tempsprbv, 0, 'The readback value for the temperature setpoint is not the same as the temperature setpoint')
        self.assertEqual(temp, 0.2, 'The temperature value is not the value expected')
        self.assertEqual(exttemp, 25.2, 'The external temperature value is not the value expected')
    def test_temp_ten(self):
		#Verify that the readbacks relate to a known setpoint
        tempsppv.put(10)
        time.sleep(delay)
        temp = temppv.get()
        tempsp = tempsppv.get()
        tempsprbv = tempsprbvpv.get()
        exttemp = exttemppv.get()
        self.assertEqual(tempsp, 10, 'The temperature setpoint is not the value expected')
        self.assertEqual(tempsprbv, 10, 'The readback value for the temperature setpoint is not the same as the temperature setpoint')
        self.assertEqual(temp, 10.2, 'The temperature value is not the value expected')
        self.assertEqual(exttemp, 35.2, 'The external temperature value is not the value expected')
tempsuite = unittest.TestLoader().loadTestsFromTestCase(TestTemp)

#Build the overall test suite and run it
suite = unittest.TestSuite([simsuite,versuite,statsuite,powersuite,hilimitsuite,lolimitsuite,modesuite,tempsuite])
unittest.TextTestRunner(verbosity=2).run(suite)

#If the IOC was put into simulation mode, put it back into device mode
if (intosim):
    print 'Returning to device mode'
    simpv.put(0)
    time.sleep(delay)

#As yet this is not being automated, and so this print and wait for input ensures that the user has an opprotunity to read the test results
print('Press Enter to exit')
raw_input('...')
exit()