import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def AND2X1_test(dut):
    """Testing AND2X1 cell"""

    dut.A.value = 1
    dut.B.value = 0

    await Timer(10, units="ns")

    dut._log.info(f"Output value is {dut.Y.value}")
    assert dut.Y.value == 0, 'Y != 0 !'

