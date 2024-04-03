from functools import reduce

def get_check_sum(tcpdump:str):
    sections = [int(x, base=16) for x in tcpdump.split("_")]
    sum = reduce(lambda x, y: x + y, sections)
    carry = bin(sum)[:-16][2:]
    sum = bin(sum)[(2 + len(carry)) :]
    print(f"Carry:{carry} Sum:{sum}")
    checksum = bin(int(sum, base=2) + int(carry, base=2))
    checksum = "".join(["0" if x == "1" else "1" for x in checksum[2:]])
    print(f"Checksum (hex): {hex(int(checksum, base=2))}")
    return hex(int(checksum, base=2))[2:]
