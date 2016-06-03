#this script was created to solve the first challenge question in 
#udacity's "Applied Cryptography" course. 

#PROBLEM:
#we are given 2 ciphers, each encrypted using the one time pad(they are XOR'd).
#both of the ciphers were encrypted using the same key
#the characters are in 7 bit ASCII format
#we are asked to decrypt the two ciphers

#MY SOLUTION:
#this program allows the user to guess a string that may be contained within
#the cipher1. it will check every possible position within cipher1, calculating
#a key for that position. it then uses that key to decrypt that same postion within
#cipher 2.
#If the user's guess is contained in the first cipher at a given position,
#then the decryption of the second cipher will be text in plain English
#Through trial and error, this program can be used to piece together the original message

#cipher1 solution - I visualize a time when we will be to robots what dogs are to humans, and I'm rooting for the machines.  (Claude Shannon)
#cipher2 solution - Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin. (John von Neumann)

ASCII_BITS = 7

#cipher1
C1str = "1010110010011110011111101110011001101100111010001111011101101011101000110010011000000101001110111010010111100100111101001010000011000001010001001001010000000010101001000011100100010011011011011011010111010011000101010111111110010011010111001001010101110001111101010000001011110100000000010010111001111010110000001101010010110101100010011111111011101101001011111001101111101111000100100001000111101111011011001011110011000100011111100001000101111000011101110101110010010100010111101111110011011011001101110111011101100110010100010001100011001010100110001000111100011011001000010101100001110011000000001110001011101111010100101110101000100100010111011000001111001110000011111111111110010111111000011011001010010011100011100001011001101110110001011101011101111110100001111011011000110001011111111101110110101101101001011110110010111101000111011001111"
#cipher2
C2str = "1011110110100110000001101000010111001000110010000110110001101001111101010000101000110100111010000010011001100100111001101010001001010001000011011001010100001100111011010011111100100101000001001001011001110010010100101011111010001110010010101111110001100010100001110000110001111111001000100001001010100011100100001101010101111000100001111101111110111001000101111111101011001010000100100000001011001001010000101001110101110100001111100001011101100100011000110111110001000100010111110110111010010010011101011111111001011011001010010110100100011001010110110001001000100011011001110111010010010010110100110100000111100001111101111010011000100100110011111011001010101000100000011111010010110111001100011100001111100100110010010001111010111011110110001000111101010110101001110111001110111010011111111010100111000100111001011000111101111101100111011001111"


ascii_dict = {
    'A': bin(65)[2:],
    'B': bin(66)[2:],
    'C': bin(67)[2:],
    'D': bin(68)[2:],
    'E': bin(69)[2:],
    'F': bin(70)[2:],
    'G': bin(71)[2:],
    'H': bin(72)[2:],
    'I': bin(73)[2:],
    'J': bin(74)[2:],
    'K': bin(75)[2:],
    'L': bin(76)[2:],
    'M': bin(77)[2:],
    'N': bin(78)[2:],
    'O': bin(79)[2:],
    'P': bin(80)[2:],
    'Q': bin(81)[2:],
    'R': bin(82)[2:],
    'S': bin(83)[2:],
    'T': bin(84)[2:],
    'U': bin(85)[2:],
    'V': bin(86)[2:],
    'W': bin(87)[2:],
    'X': bin(88)[2:],
    'Y': bin(89)[2:],
    'Z': bin(90)[2:],
    'a': bin(97)[2:],
    'b': bin(98)[2:],
    'c': bin(99)[2:],
    'd': bin(100)[2:],
    'e': bin(101)[2:],
    'f': bin(102)[2:],
    'g': bin(103)[2:],
    'h': bin(104)[2:],
    'i': bin(105)[2:],
    'j': bin(106)[2:],
    'k': bin(107)[2:],
    'l': bin(108)[2:],
    'm': bin(109)[2:],
    'n': bin(110)[2:],
    'o': bin(111)[2:],
    'p': bin(112)[2:],
    'q': bin(113)[2:],
    'r': bin(114)[2:],
    's': bin(115)[2:],
    't': bin(116)[2:],
    'u': bin(117)[2:],
    'v': bin(118)[2:],
    'w': bin(119)[2:],
    'x': bin(120)[2:],
    'y': bin(121)[2:],
    'z': bin(122)[2:],
    ' ': '0100000'
    }





#converts one set of seven bits into one character
def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + int(e)
    return chr(value)

#returns a copy of the next X characters in a string, starting from a given position
def get_substr(original, num_chars, pos):
    return original[pos * 7:(pos * 7) + num_chars]
    
#takes an ascii string in bit form and converts it to a regular string
def bitpat_to_string(bitpat):
    count = int(len(bitpat) / 7)
    return_string = ""
    
    for i in range(0, count):

        char_in_bits = bitpat[i*7: (i*7)+7]
        
        return_string += bits_to_char(char_in_bits)
    
    return return_string
    
#decrypts part of the second string based on a guess(search_string) about part of the first string
def get_other_string(c1, c2, pos, search_string):
    
    c1int = int(get_substr(c1, int(len(search_string)), pos), 2)
    c2int = int(get_substr(c2, int(len(search_string)), pos), 2)
    
    c_key = c1int ^ int(search_string, 2)
    
    possible_message = c_key ^ c2int
    
    possible_message = bin(possible_message)[2:].zfill(int(len(search_string)))
    
    return bitpat_to_string(possible_message)
    
# checks every position in the cipher for a given string
def check_everywhere_for(search_string):
    for i in range(0, (121 - (int(len(search_string) / 7) - 1) )):
        print(str(i) + ":    " + get_other_string(C1str, C2str, i, search_string))

#turns a string into binary (7 bit ASCII)        
def string_to_ascii(my_string):
    
    bin_string = ""
    
    for char in my_string:
        bin_string += ascii_dict[char]
    return bin_string
    

guess = input("Enter your guess: ")
check_everywhere_for(string_to_ascii(guess))

