import cocotb
from cocotb.triggers import Timer
from cocotb.regression import TestFactory

def model(A,B,C):
    return not(A or B or C)


@cocotb.test(skip = True)
async def test(dut, A,B,C):
    """Testing NOR3X1 module"""
    dut.A.value = A
    dut.B.value = B
    dut.C.value = C

    await Timer(10, units = "ns")
    result = dut.Y.value
    print(" ")
    print("Reaction for {dut.A.value}{dut.B.value}{dut.C.value} - {result}")
    print(" ")

    trueResult = model(A,B,C)
    assert result == trueResult, f"{result} is not {trueResult}"

tf = TestFactory(test_function = test)
tf.add_option(name = 'A', optionlist=[0,1])
tf.add_option(name = 'B', optionlist=[0,1])
tf.add_option(name = 'C', optionlist=[0,1])
tf.generate_tests()
