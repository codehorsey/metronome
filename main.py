from playsound import playsound
import time
import argparse

def get_bpm(bpm):
	return 60.0/bpm

def play(current, bpm):
	playsound('b2.mp3', bpm)
	while time.time() - current <= bpm:
		pass

def main():

	parser = argparse.ArgumentParser(description='Enter BPM.')
	parser.add_argument('--bpm', type=float, default=60.0, help='Enter BPM')
	args = parser.parse_args()
	bpm = get_bpm(args.bpm)

	# Beep 10 times, enter current time
	for i in range(10):
		play(time.time(), bpm)	
		
if __name__ == '__main__':
	main()
