import spockpy
import cv2

pad = spockpy.HoverPad(
	size     = (640, 480),
	position = 'tl',
	deviceID = 1,
	verbose  = True
)
pad.show()

while True:
	event = pad.get()
	
	if event.type == spockpy.Event.SPOCK:
		print('Spock!')
	elif event.type == spockpy.Event.PAPER:
		print('Paper!')
	elif event.type == spockpy.Event.ROCK:
		print('Rock!')
	elif event.type == spockpy.Event.SCISSOR:
		print('Scissor!')
	else:
		print('None!')
