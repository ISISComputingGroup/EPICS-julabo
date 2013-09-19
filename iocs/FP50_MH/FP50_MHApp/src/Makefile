TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = FP50_MH
# FP50_MH.dbd will be created and installed
DBD += FP50_MH.dbd

# FP50_MH.dbd will be made up from these files:
FP50_MH_DBD += base.dbd

FP50_MH_DBD += stream.dbd
FP50_MH_DBD += asyn.dbd
FP50_MH_DBD += drvAsynSerialPort.dbd
FP50_MH_DBD += drvAsynIPPort.dbd
FP50_MH_DBD += devIocStats.dbd

FP50_MH_LIBS += stream
FP50_MH_LIBS += asyn devIocStats  

# FP50_MH_registerRecordDeviceDriver.cpp derives from FP50_MH.dbd
FP50_MH_SRCS += FP50_MH_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
FP50_MH_SRCS_DEFAULT += FP50_MHMain.cpp
FP50_MH_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#FP50_MH_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
FP50_MH_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

