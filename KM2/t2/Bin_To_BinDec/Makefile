SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES ?= rtl/b2bcd.v

TOPLEVEL ?=b2bcd 

MODULE ?= test_Bin_To_BinDec

export PYTHONPATH=$(shell pwd)/tests

include $(shell cocotb-config --makefiles)/Makefile.sim

.PHONY: clean

clean::
	rm -rf __pycache__ sim_build results.xml tests/__pycache__
