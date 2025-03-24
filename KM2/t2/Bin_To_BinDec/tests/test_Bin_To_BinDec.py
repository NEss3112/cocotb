import cocotb
from cocotb.triggers import Timer
from cocotb.regression import TestFactory
import numpy as np


def get_separate_digits(num:int):
    dozens = num // 10
    units = num % 10
    return [dozens,units]

def model_1(inp:int):
    if inp <= 9:
        out = np.binary_repr(inp,width=8)
    else:
        dozens = get_separate_digits(inp)[0]
        units = get_separate_digits(inp)[1]
        out = np.binary_repr(dozens, width=4) + np.binary_repr(units, width=4)

    return out


@cocotb.test(skip = True)
async def test(dut, inp):
    """testing Binary to binary-decimal converter"""
    dut.inp.value = inp

    await Timer(20, units='ns')

    result = dut.outp.value

    trueResult = model_1(inp)

    print("")
    print(f"result for {dut.inp.value} is {result}")
    print("")

    assert result == trueResult, f"{result} is not {trueResult}"


tf = TestFactory(test_function=test)
tf.add_option(name='inp', optionlist=[i for i in range(0,15)])
tf.generate_tests()
