import cocotb
from cocotb.triggers import Timer

def model(data):
    lookupTable = {
        0b00:0,
        0b01:0,
        0b10:0,
        0b11:1
    }
    Y = lookupTable[data]
    return Y

def getBinDigit(num, n):
    mask = 1 << n
    maskedNum = num & mask
    binDigit = maskedNum >> n
    return binDigit

@cocotb.test()
async def test_AND2X1(dut):
    """Testing AND2X1 cell"""

    numberOfInputs = 2

    for num in range(2**numberOfInputs):
        dut.A.value = getBinDigit(num, 0)
        dut.B.value = getBinDigit(num, 1)

    await Timer(1, units="ns")
    result = dut.Y.value
    print("")
    print(f"Reaction for {dut.A.value}{dut.B.value} - {result}")
    print("")
    trueResult = model(num)
    assert result == trueResult, f"Result is not {trueResult}"
