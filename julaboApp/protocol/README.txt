julaboCommon.proto = Commands that are common across all/most julabos

julaboVariable.proto = Commands that are different across certain julabos.
For example: Read external temperature command can be IN_PV_01" or "IN_PV_02"

ISIS Julabos
------------

FL300= use julaboCommon.proto

FP50-MH = use julaboCommon.proto and julaboVariable.proto
    ExtTemp = IN_PV_01, Power = IN_PV_02, HighLimit = IN_SP_01, LowLimit = IN_SP_02

Small, FP50-HP, FP52-SP, FP52-SL = use julaboCommon.proto and julaboVariable.proto
    ExtTemp = IN_PV_02, Power = IN_PV_01, HighLimit = IN_SP_03, LowLimit = IN_SP_04

BIG = use julaboCommon.proto and julaboVariable.proto
    ExtTemp = IN_PV_02, Power = IN_PV_01, HighLimit = IN_SP_01, LowLimit = IN_SP_02
    
FPW55-SL = use julaboCommon.proto and julaboVariable.proto
    ExtTemp = IN_PV_02, Power = IN_PV_01, No HighLimit or LowLimit commands

FB50-HE = 

F25-HD = 

FB50-HL = 

FP50-HC = 