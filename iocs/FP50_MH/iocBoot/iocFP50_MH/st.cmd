#!../../bin/windows-x64/FP50_MH

## You may have to change FP50_MH to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet "IOCNAME" "$(P=$(MYPVPREFIX))JULFP50MH"
epicsEnvSet "IOCSTATS_DB" "$(DEVIOCSTATS)/db/iocAdminSoft.db"
epicsEnvSet "STREAM_PROTOCOL_PATH" "$(TOP)/../../julaboApp/protocol"
epicsEnvSet "TTY" "$(TTY=\\\\\\\\.\\\\COM18)"

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/FP50_MH.dbd"
julaboFL300_registerRecordDeviceDriver pdbbase

drvAsynSerialPortConfigure("L0", "$(TTY)", 0, 0, 0, 0)
asynSetOption("L0", -1, "baud", "4800")
asynSetOption("L0", -1, "bits", "7")
asynSetOption("L0", -1, "parity", "even")
asynSetOption("L0", -1, "stop", "1")

## Load record instances
dbLoadRecords("db/FP50_MH.db","P=$(IOCNAME):, PORT=L0")
#dbLoadRecords("$(IOCSTATS_DB)","IOC=$(IOCNAME)")

cd ${TOP}/iocBoot/${IOC}
iocInit

