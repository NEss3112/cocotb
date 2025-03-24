SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES ?= rtl/osu035_stdcells.v

TOPLEVEL ?= AND2X1

MODULE ?= test_AND2X1

export PYTHONPATH=$(shell pwd)/tests

include $(shell cocotb-config --makefiles)/Makefile.sim

.PHONY: clean

clean::
	rm -rf __pycache__ sim_build results.xml tests/__pycache__
