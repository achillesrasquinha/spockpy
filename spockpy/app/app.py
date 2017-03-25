# imports - standard imports
try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

# imports - third-party imports
from PIL import Image, ImageTk

# imports - module imports
import spockpy
from spockpy.config import AppConfig

class App(object):
	class Frame(tk.Frame):
		def __init__(self,
					 master     = None,
					 windowSize = AppConfig.WINDOW_SIZE):
			self.master = master

			tk.Frame.__init__(self, master)

			self.createUI()

		def createUI(self):
			width, height = AppConfig.WINDOW_SIZE
			currentRow    = 0

			size          = AppConfig.VIDEO_PANEL_SIZE
			self.video    = tk.Label(self.master,
									 width  = size[0],
									 height = size[1])

			self.video.grid(row    = currentRow,
							column = 0,
							sticky = tk.E + tk.W)

	def __init__(self,
				 windowSize = AppConfig.WINDOW_SIZE):
		self.windowSize  = windowSize
		width, height    = self.windowSize

		self.root        = tk.Tk()
		self.root.title('%s v%s' % (AppConfig.NAME, AppConfig.VERSION))
		self.root.geometry('{width}x{height}'.format(
			width  = width,
			height = height
		))

		self.frame       = App.Frame(
			master       = self.root,
			windowSize   = self.windowSize
		)

		self.capture     = spockpy.Capture()
		self.thread      = threading.Thread(target = self.videoloop)

	def run(self):
		self.thread.start()
		self.root.mainloop()

	def videoloop(self):
		while True:
			frame   = self.capture.read()
			image   = Image.fromarray(frame)

			imagetk = ImageTk.PhotoImage(image)

			self.frame.video.configure(image = imagetk)
