import cocotb
from cocotb.triggers import Timer
from cocotb.regression import TestFactory
import numpy as np


def model(a,b):
    return a * b


@cocotb.test(skip = True)
async def test(dut,a,b):
    """testing array multiplier converter"""
    dut.a.value = a
    dut.b.value = b

    await Timer(20, units='ns')

    result = dut.c.value

    trueResult = model(dut.a.value,dut.b.value)

    print("")
    print(f"result for {int(dut.a.value)} * {int(dut.b.value)} = {int(result)}")
    print("")

    assert result == trueResult, f"{result} is not {trueResult}"


tf = TestFactory(test_function=test)
tf.add_option(name='a', optionlist=[i for i in range(0,2**8)])
tf.add_option(name='b', optionlist=[i for i in range(0,2**8)])
tf.generate_tests()
