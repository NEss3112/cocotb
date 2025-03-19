import cocotb
from cocotb.triggers import Timer

def model(in0,in1,in2):
    return not((in0 and in1) or in2)


def getBinDigit(num, n):
    mask = 1 << n
    maskedNum = num & mask
    binDigit = maskedNum >> n
    return binDigit

@cocotb.test()
async def test_AOI21X1(dut):
    """Testing AOI21X1 cell"""

    numberOfInputs = 3

    for num in range(2**numberOfInputs):
        dut.A.value = getBinDigit(num, 0)
        dut.B.value = getBinDigit(num, 1)
        dut.C.value = getBinDigit(num, 2)

        await Timer(10, units="ns")
        result = dut.Y.value
        print("")
        print(f"Reaction for {dut.A.value}{dut.B.value}{dut.C.value} - {result}")
        print("")
        trueResult = model(dut.A.value, dut.B.value, dut.C.value)
        assert result == trueResult, f"{result} is not {trueResult}"
