#Makefile at top of application tree
TOP = .
include $(TOP)/configure/CONFIG
ACTIONS += kit zip
DIRS := $(DIRS) $(filter-out $(DIRS), configure)
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *App))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *app))

include $(TOP)/configure/RULES_TOP


