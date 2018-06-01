#!/usr/bin/python3
import sys

#Morse dictionary
morse_code_lookup = {
   # "......":    "_",
    ".-":    "A",
    "-...":    "B",
    "-.-.":    "C",
    "-..":    "D",
    ".":    "E",
    "..-.":    "F",
    "--.":    "G",
    "....":    "H",
    "..":    "I",
    ".---":    "J",
    "-.-":    "K",
    ".-..":    "L",
    "--":    "M",
    "-.":    "N",
    "---":    "O",
    ".--.":    "P",
    "--.-":    "Q",
    ".-.":    "R",
    "...":    "S",
    "-":    "T",
    "..-":    "U",
    "...-":    "V",
    ".--":    "W",
    "-..-":    "X",
    "-.--":    "Y",
    "--..":    "Z",
    ".----":    "1",
    "..---":    "2",
    "...--":    "3",
    "....-":    "4",
    ".....":    "5",
    "-....":    "6",
    "--...":    "7",
    "---..":    "8",
    "----.":    "9",
    "-----":    "0"
}

def try_decode(bit_string):
    if bit_string in morse_code_lookup.keys(): #if valid character
        sys.stdout.write(morse_code_lookup[bit_string]) #output english characters
        sys.stdout.flush()
        dddd = morse_code_lookup[bit_string] #dddd becomes most recent letter
        #open the outbound file and copy the contents
        fmess = open('outbound.txt', 'r')
        contents = fmess.read()
        fmess.close()
        #add the most recent character to the existing contents
        fmess = open('outbound.txt', 'w')
        deets = contents + dddd
        fmess.write(deets)
        fmess.close()   
