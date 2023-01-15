#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rom_num = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    num = 0
    i = 0
    while i < len(roman_string):
        current = roman_string[i]
        if i == len(roman_string) - 1:
            num += rom_num[current]
            break
        nxt = roman_string[i + 1]
        if rom_num[current] >= rom_num[nxt]:
            num += rom_num[current]
        else:
            num += rom_num[nxt] - rom_num[current]
            i += 1
        i += 1
    return num
