import cocotb
from cocotb.triggers import Timer

def model(in0,in1,sel):
    if sel:
        return in0
    elif not sel:
        return in1

def getBinDigit(num, n):
    mask = 1 << n
    maskedNum = num & mask
    binDigit = maskedNum >> n
    return binDigit

@cocotb.test()
async def test_MUX2X1(dut):
    """Testing MUX2X1 cell"""

    numberOfInputs = 3

    for num in range(2**numberOfInputs):
        dut.A.value = getBinDigit(num, 0)
        dut.B.value = getBinDigit(num, 1)
        dut.S.value = getBinDigit(num, 2)

        await Timer(10, units="ns")
        result = dut.Y.value
        print("")
        print(f"Reaction for {dut.A.value}{dut.B.value}{dut.S.value} - {result}")
        print("")
        trueResult = not(model(dut.A.value, dut.B.value, dut.S.value))
        assert result == trueResult, f"{result} is not {trueResult}"
