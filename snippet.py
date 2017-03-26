import spockpy
import pyautogui

class App(object):
	class Frame(tk.Frame):
		

if __name__ == '__main__':
	pad = spockpy.HoverPad(size = (640, 480), verbose = True, position = 'tl', deviceID = 0)
	pad.show()

	while True:
		event    = pad.get_event()
 
		position = event.get_tip()
		x, y     = position

		if x != None and y != None:
			pyautogui.moveTo(x, y)