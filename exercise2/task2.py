def asciiToBitRep(chars):
    for char in chars:
        ascii_value = ord(char)
        if 0 <= ascii_value <= 127:
            bit_representation = format(ascii_value, "08b")
            print(f"Character: '{char}'")
            print(f"- ASCII representation: {bit_representation}")
        else:
            print(f"Character: '{char}'")
            print("- Not in ASCII range")


test_chars2 = ["1", "€"]
test_chars = ["2", "$", "å"]
asciiToBitRep(test_chars)
