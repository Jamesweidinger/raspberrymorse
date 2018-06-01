import pygame
import time
import gpiozero as gpio
import _thread as thread
from array import array
from pygame.locals import *
from morse_lookup import *
import RPi.GPIO as GPIO

#Morse dictionary for inbound comms
CODE = {' ': ' ',
        "'": '.----.',
        '\n': ' ',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

def read_out():
	file = open('inbound.txt', 'r') #look at what was sent
	thingo = file.read()
	for letter in thingo:
			for symbol in CODE[letter.upper()]: #for each letter play the morse code equivalent
				if symbol == '-':
					dash()
				elif symbol == '.':
					dot()
				elif key_down_time > 0.01: #if button is pressed again, resume normal functions
					time.sleep(0.5)
					return
			time.sleep(0.5)

def decoder_thread():
	global key_up_time
	global buffer
	new_word = False
	while True:
		time.sleep(.01)
		key_up_length = time.time() - key_up_time
		if key_down_length > 3: #if held for >3 play inbound comms 
			read_out()
		elif len(buffer) > 0 and key_up_length >= 1.5: #when inputtign a letter on the buzzer
			new_word = True
			bit_string = "".join(buffer)
			try_decode(bit_string)
			del buffer[:]
		elif new_word and key_up_length >= 4.5: #adds a space between words
			new_word = False
			sys.stdout.write(" ")
			sys.stdout.flush()

#play a dot
def dot(): 
        GPIO.output(buzPin,1)
        time.sleep(0.2)
        GPIO.output(buzPin,0)
        time.sleep(0.2)

#play a dash
def dash():
        GPIO.output(buzPin,1)
        time.sleep(0.5)
        GPIO.output(buzPin,0)
        time.sleep(0.2)
			
pin = 2 #set button pin
key = gpio.Button(pin, pull_up=True)

buzPin=17 #set buzzer pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzPin,GPIO.OUT)
GPIO.setwarnings(False)

DOT = "."
DASH = "-"

key_down_time = 0
key_down_length = 0
key_up_time = 0
buffer = []

thread.start_new_thread(decoder_thread, ())

print("Ready")

while True:
    key.wait_for_press() #listening for a press
    key_down_time = time.time() #record the time when the key went down
    key.wait_for_release()
    key_up_time = time.time() #record the time when the key was released
    key_down_length = key_up_time - key_down_time #get the length of time it was held down for
    buffer.append(DASH if key_down_length > 0.15 else DOT) #add dot or dash to the buffer
