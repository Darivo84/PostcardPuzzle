"""
Description:    Conversion for the front of the postcard!
                
"""

decimal = int(0x377ABCAF271C00030241DD5F17000000000000005800000000000000BAF0646A00221BC9C273209CAA0F0A552E8172D58300000104060001091700070B01000123030101055D000001000C1100080A01D1DA43C200000501111B0064006F006E0074006600750063006B0069007400750070000000140A010080F1F4CEAC5ED1001506010020808081000000)


convert = int(
    input("Convert into: [1] Binary, [2] Octal, [3] Hexadecimal: \n"))


if convert == 1:
    print("Converted to Binary \n", bin(decimal))
elif convert == 2:
    print("Converted to Octal \n", oct(decimal))
elif convert == 3:
    print("Converted to Hexadecimal \n", hex(decimal))
else:
    print("Please review your selection.")
