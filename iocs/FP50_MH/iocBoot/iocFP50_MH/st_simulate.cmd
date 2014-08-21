#!../../bin/windows-x64/FP50_MH

## You may have to change FP50_MH to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet "IOCNAME" "$(P=$(MYPVPREFIX))JULFP50MH"
epicsEnvSet "IOCSTATS_DB" "$(DEVIOCSTATS)/db/iocAdminSoft.db"
epicsEnvSet "STREAM_PROTOCOL_PATH" "$(TOP)/../../julaboApp/protocol"

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/FP50_MH.dbd"
FP50_MH_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure ("L0", "127.0.0.1:9999")

## Load record instances
dbLoadRecords("db/FP50_MH.db","P=$(IOCNAME):, PORT=L0")
#dbLoadRecords("$(IOCSTATS_DB)","IOC=$(IOCNAME)")

cd ${TOP}/iocBoot/${IOC}
iocInit

