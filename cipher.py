plugboard = {
    'A': 'M', 'M': 'A',
    'F': 'G', 'G': 'F',
    'H': 'Z', 'Z': 'H',
    'K': 'L', 'L': 'K',
    'Q': 'R', 'R': 'Q',
    'U': 'T', 'T': 'U',
}

plugboard = {

}

def offset_letter(letter, offset):
    start = ord('A')
    # mod 26 to prevent overflow (z would end up offsetting to "{", but instead goes to "a" in unicode)
    offset = (ord(letter) - start + offset) % 26
    return chr(start + offset)

def letter_to_alphabet_position(letter):
    return ord(letter) - ord('A') + 1

def swap(letter):
    return plugboard.get(letter, letter)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BETA = "LEYJVCNIXWPBQMDRTAKZGFUHOS"
GAMMA = "FSOKANUERHMBTIYCWLQPZXVGJD"
I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
V = "VZBRGITYUPSDNHLXAWMJQOFECK"
VI = "JPGVOUMFYQBENHZRDKASXLICTW"
VII = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
VIII = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
UKW_B = "ENKQAUYWJICOPBLMDXZVFTHRGS"
UKW_C = "RDOBJNTKVEHMLFCWZAXGYIPSUQ"

# im too lazy to write this with classes or something

betaPosition = letter_to_alphabet_position("A")
gammaPosition = letter_to_alphabet_position("A")
rotorIPos = letter_to_alphabet_position("A")
rotorIIPos = letter_to_alphabet_position("A")
rotorIIIPos = letter_to_alphabet_position("Z")
rotorIVPos = letter_to_alphabet_position("A")
rotorVPos = letter_to_alphabet_position("A")
rotorVIPos = letter_to_alphabet_position("A")
rotorVIIPos = letter_to_alphabet_position("A")
rotorVIIIPos = letter_to_alphabet_position("A")

betaStellung = 1
gammaStellung = 1
rotorIStellung = 1
rotorIIStellung = 1
rotorIIIStellung = 1
rotorIVStellung = 1
rotorVStellung = 1
rotorVIStellung = 1
rotorVIIStellung = 1
rotorVIIIStellung = 1

rotorITurnover = {letter_to_alphabet_position("Z"), letter_to_alphabet_position("M")}
rotorIITurnover = {letter_to_alphabet_position("Z"), letter_to_alphabet_position("M")}
rotorIIITurnover = {letter_to_alphabet_position("Z"), letter_to_alphabet_position("M")}
rotorIVTurnover = {letter_to_alphabet_position("Z"), letter_to_alphabet_position("M")}
rotorVTurnover = {letter_to_alphabet_position("Z"), letter_to_alphabet_position("M")}
rotorVITurnover = {letter_to_alphabet_position("Z"), letter_to_alphabet_position("M")}
rotorVIITurnover = {letter_to_alphabet_position("Z"), letter_to_alphabet_position("M")}
rotorVIIITurnover = {letter_to_alphabet_position("Z"), letter_to_alphabet_position("M")}

rotorI = {
    "RotorMap": I,
    "Position": rotorIPos,
    "Stellung": rotorIStellung,
    "Turnover": rotorITurnover
}

rotorII = {
    "RotorMap": II,
    "Position": rotorIIPos,
    "Stellung": rotorIIStellung,
    "Turnover": rotorIITurnover
}

rotorIII = {
    "RotorMap": III,
    "Position": rotorIIIPos,
    "Stellung": rotorIIIStellung,
    "Turnover": rotorIIITurnover
}

rotorIV = {
    "RotorMap": IV,
    "Position": rotorIVPos,
    "Stellung": rotorIVStellung,
    "Turnover": rotorIVTurnover
}

rotorV = {
    "RotorMap": V,
    "Position": rotorVPos,
    "Stellung": rotorVStellung,
    "Turnover": rotorVTurnover
}

rotorVI = {
    "RotorMap": VI,
    "Position": rotorVIPos,
    "Stellung": rotorVIStellung,
    "Turnover": rotorVITurnover
}

rotorVII = {
    "RotorMap": VII,
    "Position": rotorVIIPos,
    "Stellung": rotorVIIStellung,
    "Turnover": rotorVIITurnover
}

rotorVIII = {
    "RotorMap": VIII,
    "Position": rotorVIIIPos,
    "Stellung": rotorVIIIStellung,
    "Turnover": rotorVIIITurnover
}

ukw_b = {
    "RotorMap": UKW_B,
}

ukw_c = {
    "RotorMap": UKW_C,
}

beta = {
    "RotorMap": BETA,
    "Position": betaPosition,
    "Stellung": betaStellung
}

gamma = {
    "RotorMap": GAMMA,
    "Position": gammaPosition,
    "Stellung": gammaStellung
}

def bruh(input, rotor):
    print(input)
    new = offset_letter(input, rotor["Position"] - 1 + -(rotor["Stellung"] - 1))
    print(new)
    new = rotor["RotorMap"][alphabet.find(new)]
    print(new)
    new = offset_letter(new, -(rotor["Position"] - 1 + -(rotor["Stellung"]- 1)))
    print(new)
    return new

def bruh_rev(input, rotor):
    new = offset_letter(input, rotor["Position"] - 1 + -(rotor["Stellung"] - 1))
    new = alphabet[rotor["RotorMap"].find(new)]
    new = offset_letter(new, -(rotor["Position"] - 1 + -(rotor["Stellung"]- 1)))
    return new

word = ""

for letter in "SIGMA SIGMA":
    print("LETTER:", letter)

    if letter.isalpha():
        letter = str.upper(letter)
        letter = swap(letter)

        rotorIII["Position"] = rotorIII["Position"] + 1

        if rotorIII["Position"] > 26:
            rotorIII["Position"] = 1

        if rotorIII["Position"] == rotorIII["Turnover"]:
            rotorIII["Position"] = rotorIII["Position"] + 1

        if rotorII["Position"] > 26:
            rotorII["Position"] = 1

        # double stepping mechanism in enigma
        if rotorII["Position"] == rotorIII["Turnover"]:
            rotorII["Position"] = rotorII["Position"] + 1
            rotorI["Position"] = rotorI["Position"] + 1

        if rotorI["Position"] > 26:
            rotorI["Position"] = 1

        if rotorII["Position"] > 26:
            rotorII["Position"] = 1

        letter = bruh(letter, rotorIII)
        letter = bruh(letter, rotorII)
        letter = bruh(letter, rotorI)
        letter = bruh(letter, beta)

        letter = ukw_b["RotorMap"][alphabet.find(letter)]

        letter = bruh_rev(letter, beta)
        letter = bruh_rev(letter, rotorI)
        letter = bruh_rev(letter, rotorII)
        letter = bruh_rev(letter, rotorIII)

        new = swap(letter)
    else:
        new = letter

    word = word + new

print(word)