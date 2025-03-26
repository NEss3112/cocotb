import cocotb
from cocotb.triggers import Timer
from cocotb.regression import TestFactory
import numpy as np


def model(A,B):
    return A + B


@cocotb.test(skip = True)
async def test(dut, A,B):
    """testing four bit adder converter"""
    dut.A.value = A
    dut.B.value = B

    await Timer(20, units='ns')

    result = dut.SUM.value

    trueResult = model(dut.A.value,dut.B.value)

    print("")
    print(f"result for {int(dut.A.value)} + {int(dut.B.value)} = {int(result)}")
    print("")

    assert result == trueResult, f"{result} is not {trueResult}"


tf = TestFactory(test_function=test)
tf.add_option(name='A', optionlist=[i for i in range(0,7)])
tf.add_option(name='B', optionlist=[i for i in range(0,7)])
tf.generate_tests()
