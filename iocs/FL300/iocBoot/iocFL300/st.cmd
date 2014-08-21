#!../../bin/windows-x64/FL300

## You may have to change FL300 to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet "IOCNAME" "$(P=$(MYPVPREFIX))JULFL300"
epicsEnvSet "IOCSTATS_DB" "$(DEVIOCSTATS)/db/iocAdminSoft.db"
epicsEnvSet "STREAM_PROTOCOL_PATH" "$(TOP)/../../julaboApp/protocol"
epicsEnvSet "TTY" "$(TTY=\\\\\\\\.\\\\COM18)"

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/FL300.dbd"
FL300_registerRecordDeviceDriver pdbbase

drvAsynSerialPortConfigure("L0", "$(TTY)", 0, 0, 0, 0)
asynSetOption("L0", -1, "baud", "4800")
asynSetOption("L0", -1, "bits", "7")
asynSetOption("L0", -1, "parity", "even")
asynSetOption("L0", -1, "stop", "1")

## Load record instances
dbLoadRecords("db/FL300.db","P=$(IOCNAME):, PORT=L0")
#dbLoadRecords("$(IOCSTATS_DB)","IOC=$(IOCNAME)")

cd ${TOP}/iocBoot/${IOC}
iocInit

