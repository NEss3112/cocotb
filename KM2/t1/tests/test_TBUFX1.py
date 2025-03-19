import cocotb
from cocotb.triggers import Timer

def model():
    pass

@cocotb.test(skip=True)
async def test(dut, A, EN):
    """ Testing TBUFX1 cell"""
    dut.A.value = A
    dut.EN.value = EN

    await Timer(10, units="ns")
    result = dut.Y.value
    print("")
    print("Reaction for A = {dut.A.value}, EN = {dut.EN.value} - {result}")
    print("")
    trueResult = model(A,B)
    assert result == trueResult, f"{result} is not {trueResult}"

