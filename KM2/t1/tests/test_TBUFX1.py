import cocotb
from cocotb.triggers import Timer

def model(A, EN):
    return A if EN else 'z' 

def getBinDigit(num, n):
    mask = 1 << n
    maskedNum = num & mask
    binDigit = maskedNum >> n
    return binDigit

@cocotb.test()
async def test(dut):
    """ Testing TBUFX1 cell"""
    numberOfInputs = 2
    for num in range(2**numberOfInputs):
        dut.A.value = getBinDigit(num,1)
        dut.EN.value = getBinDigit(num,2)

    await Timer(10, units="ns")
    result = dut.Y.value
    print("")
    print("Reaction for A = {dut.A.value}, EN = {dut.EN.value} - {result}")
    print("")
    trueResult = model(dut.A.value,dut.EN.value)
    assert result == trueResult, f"{result} is not {trueResult}"

