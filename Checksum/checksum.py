from functools import reduce

CHECK_SUM = "5dd1"
TCP_DUMP = f"4500_0123_506a_ffff_ffff_{CHECK_SUM}_c0a8_0d01_23c3_1a34"
sections = [int(x, base=16) for x in TCP_DUMP.split("_")]
sum = reduce(lambda x, y: x + y, sections)
carry = bin(sum)[:-16][2:]
sum = bin(sum)[(2 + len(carry)) :]
print(f"Carry:{carry} Sum:{sum}")
checksum = bin(int(sum, base=2) + int(carry, base=2))
checksum = "".join(["0" if x == "1" else "1" for x in checksum[2:]])
print(f"Checksum (hex): {hex(int(checksum, base=2))}")
