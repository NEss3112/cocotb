SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES ?= rtl/four_bit_adder.v

TOPLEVEL ?=four_bit_adder 

MODULE ?= test_four_bit_adder

export PYTHONPATH=$(shell pwd)/tests

include $(shell cocotb-config --makefiles)/Makefile.sim

.PHONY: clean

clean::
	rm -rf __pycache__ sim_build results.xml tests/__pycache__
