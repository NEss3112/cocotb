SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES ?= rtl/array_multiplier.v

TOPLEVEL ?=array8 

MODULE ?= test_array_multiplier

export PYTHONPATH=$(shell pwd)/tests

include $(shell cocotb-config --makefiles)/Makefile.sim

.PHONY: clean

clean::
	rm -rf __pycache__ sim_build results.xml tests/__pycache__
