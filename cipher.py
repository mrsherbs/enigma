alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
UTW_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

plugboard = {
    'A': 'M', 'M': 'A',
    'F': 'G', 'G': 'F',
    'H': 'Z', 'Z': 'H',
    'K': 'L', 'L': 'K',
    'Q': 'R', 'R': 'Q',
    'U': 'T', 'T': 'U',
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

# E J K C H B X J N Q D I
rotorIPos = letter_to_alphabet_position("Z")
rotorIIPos = letter_to_alphabet_position("Z")
rotorIIIPos = letter_to_alphabet_position("Z")

# B M V
# B L V

rotorIStellung = 16
rotorIIStellung = 12
rotorIIIStellung = 14

rotorITurnover = letter_to_alphabet_position("R") - 1 
rotorIITurnover = letter_to_alphabet_position("F") - 1
rotorIIITurnover = letter_to_alphabet_position("W")

word = ""

for letter in "LFEQYQF":
    print("LETTER:", letter)

    letter = str.upper(letter)
    letter = swap(letter)

    rotorIIIPos = rotorIIIPos + 1

    if rotorIIIPos > 26:
        rotorIIIPos = 1

    if rotorIIIPos == rotorIIITurnover:
        rotorIIPos = rotorIIPos + 1

    if rotorIIPos > 26:
        rotorIIPos = 1

    # double stepping mechanism in enigma
    if rotorIIPos == rotorIITurnover:
        rotorIIPos = rotorIIPos + 1
        rotorIPos = rotorIPos + 1

    if rotorIPos > 26:
        rotorIPos = 1

    if rotorIIPos > 26:
        rotorIIPos = 1

    new = offset_letter(letter, rotorIIIPos - 1 + -(rotorIIIStellung - 1))
    new = III[alphabet.find(new)]
    new = offset_letter(new, -(rotorIIIPos - 1 + -(rotorIIIStellung - 1)))
    
    new = offset_letter(new, rotorIIPos - 1 + -(rotorIIStellung - 1))
    new = II[alphabet.find(new)]
    new = offset_letter(new, -(rotorIIPos - 1 + -(rotorIIStellung - 1)))

    new = offset_letter(new, rotorIPos - 1 + -(rotorIStellung - 1))
    new = I[alphabet.find(new)]
    new = offset_letter(new, -(rotorIPos - 1 + -(rotorIStellung - 1)))

    new = UTW_B[alphabet.find(new)]

    new = offset_letter(new, rotorIPos - 1 + -(rotorIStellung - 1))
    new = alphabet[I.find(new)]
    new = offset_letter(new, -(rotorIPos - 1 + -(rotorIStellung - 1)))

    new = offset_letter(new, rotorIIPos - 1 + -(rotorIIStellung - 1))
    new = alphabet[II.find(new)]
    new = offset_letter(new, -(rotorIIPos - 1 + -(rotorIIStellung - 1)))

    new = offset_letter(new, rotorIIIPos - 1 + -(rotorIIIStellung - 1))
    new = alphabet[III.find(new)]
    new = offset_letter(new, -(rotorIIIPos - 1 + -(rotorIIIStellung - 1)))

    new = swap(new)

    word = word + new

print(word)