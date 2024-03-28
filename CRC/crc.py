def flip(x: int, bits: int = 16) -> int:
    """
    Flips the bits of an integer. It will only flip the lower `bits` bits.
    """
    result = 0
    for i in range(bits):
        # Reflect reg
        result <<= 1
        temp = x & (0x0001 << i)
        if temp:
            result |= 0x0001
    return result


def crc16(
    data: bytearray,
    poly: int = 0x8005,
    init: int = 0x0000,
    ref_in: bool = True,
    ref_out: bool = True,
    xor_out: int = -0x0000,
    debug: bool = False,
    disable_poly_xor: bool = False,
) -> int:
    """
    Calculates CRC-16 using the division approach with bitwise message XOR-ing.
    """
    reg = init

    for byte in data:
        if not ref_in:
            byte = flip(byte, 8)

        for _ in range(8):
            # Process all 8 bits one at a time
            reg <<= 1  # Shift register left by one bit
            reg |= byte & 0x01  # Shift data bit into the register one at a time

            # If a 1 shifts out of the 16-bit register, XOR with polynomial
            if not disable_poly_xor:
                if reg & 0x010000:
                    reg ^= poly

            # Prepare next bit to shift into the register
            byte >>= 1

            if debug:
                reg_str = f"{reg:032b}"
                print(
                    f"{reg_str[-17:-16]} {reg_str[-16:-12]} {reg_str[-12:-8]} "
                    f"{reg_str[-8:-4]} {reg_str[-4:]} < {byte:08b}"
                )

    # Post-invert (optional)
    if ref_out:
        reg = flip(reg, 16)

    # XOR with final value (optional)
    reg ^= xor_out

    return reg


# Example usage:
data_to_check = [0,1,0,1]
crc_value = crc16(data_to_check)
print(f"CRC-16 value: {crc_value:04X}")
