#!../../bin/windows-x64/FL300

## You may have to change FL300 to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet "IOCNAME" "$(P=$(MYPVPREFIX))JULFL300"
epicsEnvSet "IOCSTATS_DB" "$(DEVIOCSTATS)/db/iocAdminSoft.db"
epicsEnvSet "STREAM_PROTOCOL_PATH" "$(TOP)/../../julaboApp/protocol"

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/FL300.dbd"
FL300_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure ("L0", "127.0.0.1:9999")

## Load record instances
dbLoadRecords("db/FL300.db","P=$(IOCNAME):, PORT=L0")
#dbLoadRecords("$(IOCSTATS_DB)","IOC=$(IOCNAME)")

cd ${TOP}/iocBoot/${IOC}
iocInit

