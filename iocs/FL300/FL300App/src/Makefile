TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = FL300
# FL300.dbd will be created and installed
DBD += FL300.dbd

# FL300.dbd will be made up from these files:
FL300_DBD += base.dbd

FL300_DBD += stream.dbd
FL300_DBD += asyn.dbd
FL300_DBD += drvAsynSerialPort.dbd
FL300_DBD += drvAsynIPPort.dbd
FL300_DBD += devIocStats.dbd

FL300_LIBS += stream
FL300_LIBS += asyn devIocStats  

# FL300_registerRecordDeviceDriver.cpp derives from FL300.dbd
FL300_SRCS += FL300_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
FL300_SRCS_DEFAULT += FL300Main.cpp
FL300_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#FL300_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
FL300_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

